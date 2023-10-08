"""Module to implement logics used for initializing extensions.

The implementations here should be stateless.
They should not depend on external state.
Anything that depends on external state should happen in __init__.py
"""


import os
from functools import wraps
from pathlib import Path

import torch

import torchffmpeg
from torchffmpeg._internal.module_utils import is_module_available

_LIB_DIR = Path(__file__).parent.parent / "lib"


def _get_lib_path(lib: str):
    suffix = "pyd" if os.name == "nt" else "so"
    path = _LIB_DIR / f"{lib}.{suffix}"
    return path


def _load_lib(lib: str) -> bool:
    """Load extension module

    Note:
        In case `torchffmpeg` is deployed with `pex` format, the library file
        is not in a standard location.
        In this case, we expect that `libtorchffmpeg` is available somewhere
        in the search path of dynamic loading mechanism, so that importing
        `_torchffmpeg` will have library loader find and load `libtorchffmpeg`.
        This is the reason why the function should not raising an error when the library
        file is not found.

    Returns:
        bool:
            True if the library file is found AND the library loaded without failure.
            False if the library file is not found (like in the case where torchffmpeg
            is deployed with pex format, thus the shared library file is
            in a non-standard location.).
            If the library file is found but there is an issue loading the library,
            (such as missing dependency) then this function raises the exception as-is.

    Raises:
        Exception:
            If the library file is found, but there is an issue loading the library file,
            (when underlying `ctype.DLL` throws an exception), this function will pass
            the exception as-is, instead of catching it and returning bool.
            The expected case is `OSError` thrown by `ctype.DLL` when a dynamic dependency
            is not found.
            This behavior was chosen because the expected failure case is not recoverable.
            If a dependency is missing, then users have to install it.
    """
    path = _get_lib_path(lib)
    if not path.exists():
        return False
    torch.ops.load_library(path)
    torch.classes.load_library(path)
    return True


def _init_sox():
    _load_lib("libtorchffmpeg_sox")
    import torchffmpeg.lib._torchffmpeg_sox  # noqa

    torch.ops.torchffmpeg.sox_utils_set_verbosity(0)

    import atexit

    torch.ops.torchffmpeg.sox_effects_initialize_sox_effects()
    atexit.register(torch.ops.torchffmpeg.sox_effects_shutdown_sox_effects)


def _init_ffmpeg():
    if not is_module_available("torchffmpeg.lib._torchffmpeg_ffmpeg"):
        raise RuntimeError(
            "torchffmpeg is not compiled with FFmpeg integration. Please set USE_FFMPEG=1 when compiling torchffmpeg."
        )

    try:
        _load_lib("libtorchffmpeg_ffmpeg")
    except OSError as err:
        raise ImportError("FFmpeg libraries are not found. Please install FFmpeg.") from err

    import torchffmpeg.lib._torchffmpeg_ffmpeg  # noqa

    torch.ops.torchffmpeg.ffmpeg_init()
    if torch.ops.torchffmpeg.ffmpeg_get_log_level() > 8:
        torch.ops.torchffmpeg.ffmpeg_set_log_level(8)


def _init_dll_path():
    # On Windows Python-3.8+ has `os.add_dll_directory` call,
    # which is called to configure dll search path.
    # To find cuda related dlls we need to make sure the
    # conda environment/bin path is configured Please take a look:
    # https://stackoverflow.com/questions/59330863/cant-import-dll-module-in-python
    # Please note: if some path can't be added using add_dll_directory we simply ignore this path
    for path in os.environ.get("PATH", "").split(";"):
        if os.path.exists(path):
            try:
                os.add_dll_directory(path)
            except Exception:
                pass


def _check_cuda_version():
    version = torchffmpeg.lib._torchffmpeg.cuda_version()
    if version is not None and torch.version.cuda is not None:
        version_str = str(version)
        ta_version = f"{version_str[:-3]}.{version_str[-2]}"
        t_version = torch.version.cuda.split(".")
        t_version = f"{t_version[0]}.{t_version[1]}"
        if ta_version != t_version:
            raise RuntimeError(
                "Detected that PyTorch and TorchAudio were compiled with different CUDA versions. "
                f"PyTorch has CUDA version {t_version} whereas TorchAudio has CUDA version {ta_version}. "
                "Please install the TorchAudio version that matches your PyTorch version."
            )
    return version


def _fail_since_no_ffmpeg(func):
    @wraps(func)
    def wrapped(*_args, **_kwargs):
        try:
            # Note:
            # We run _init_ffmpeg again just to show users the stacktrace.
            # _init_ffmpeg would not succeed here.
            _init_ffmpeg()
        except Exception as err:
            raise RuntimeError(
                f"{func.__name__} requires FFmpeg extension which is not available. "
                "Please refer to the stacktrace above for how to resolve this."
            ) from err
        # This should not happen in normal execution, but just in case.
        return func(*_args, **_kwargs)

    return wrapped