# flake8: noqa
import torchffmpeg

from . import utils
from .utils import _is_backend_dispatcher_enabled, get_audio_backend, list_audio_backends, set_audio_backend

if _is_backend_dispatcher_enabled():
    from torchffmpeg._backend.utils import get_info_func, get_load_func, get_save_func

    torchffmpeg.info = get_info_func()
    torchffmpeg.load = get_load_func()
    torchffmpeg.save = get_save_func()
else:
    utils._init_audio_backend()
