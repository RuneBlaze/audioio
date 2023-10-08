import torch
from torchffmpeg_unittest.common_utils import PytorchTestCase
from torchffmpeg_unittest.models.hdemucs.hdemucs_test_impl import CompareHDemucsOriginal, HDemucsTests


class HDemucsFloat32CPUTest(HDemucsTests, CompareHDemucsOriginal, PytorchTestCase):
    dtype = torch.float32
    device = torch.device("cpu")
