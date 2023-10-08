import torchffmpeg
from torchffmpeg_unittest import common_utils


class BackendSwitchMixin:
    """Test set/get_audio_backend works"""

    backend = None
    backend_module = None

    def test_switch(self):
        torchffmpeg.set_audio_backend(self.backend)
        if self.backend is None:
            assert torchffmpeg.get_audio_backend() is None
        else:
            assert torchffmpeg.get_audio_backend() == self.backend
        assert torchffmpeg.load == self.backend_module.load
        assert torchffmpeg.save == self.backend_module.save
        assert torchffmpeg.info == self.backend_module.info


class TestBackendSwitch_NoBackend(BackendSwitchMixin, common_utils.TorchaudioTestCase):
    backend = None
    backend_module = torchffmpeg.backend.no_backend


@common_utils.skipIfNoSox
class TestBackendSwitch_SoXIO(BackendSwitchMixin, common_utils.TorchaudioTestCase):
    backend = "sox_io"
    backend_module = torchffmpeg.backend.sox_io_backend


@common_utils.skipIfNoModule("soundfile")
class TestBackendSwitch_soundfile(BackendSwitchMixin, common_utils.TorchaudioTestCase):
    backend = "soundfile"
    backend_module = torchffmpeg.backend.soundfile_backend
