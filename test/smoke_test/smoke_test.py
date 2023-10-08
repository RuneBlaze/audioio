"""Run smoke tests"""

import argparse

import torchffmpeg  # noqa: F401
import torchffmpeg.compliance.kaldi  # noqa: F401
import torchffmpeg.datasets  # noqa: F401
import torchffmpeg.functional  # noqa: F401
import torchffmpeg.models  # noqa: F401
import torchffmpeg.pipelines  # noqa: F401
import torchffmpeg.sox_effects  # noqa: F401
import torchffmpeg.transforms  # noqa: F401
import torchffmpeg.utils  # noqa: F401


def ffmpeg_test():
    from torchffmpeg.io import StreamReader  # noqa: F401


def main() -> None:
    parser = argparse.ArgumentParser()

    # Warning: Please note this option should not be widely used, only use it when absolutely necessary
    parser.add_argument("--no-ffmpeg", dest="ffmpeg", action="store_false")

    options = parser.parse_args()
    if options.ffmpeg:
        ffmpeg_test()


if __name__ == "__main__":
    main()
