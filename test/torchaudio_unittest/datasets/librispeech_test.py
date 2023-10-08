from torchffmpeg.datasets import librispeech
from torchffmpeg_unittest.common_utils import TorchaudioTestCase
from torchffmpeg_unittest.datasets.librispeech_test_impl import LibriSpeechTestMixin


class TestLibriSpeech(LibriSpeechTestMixin, TorchaudioTestCase):
    librispeech_cls = librispeech.LIBRISPEECH
