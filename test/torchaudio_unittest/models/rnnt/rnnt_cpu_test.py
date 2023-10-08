import torch
from torchffmpeg_unittest.common_utils import PytorchTestCase
from torchffmpeg_unittest.models.rnnt.rnnt_test_impl import RNNTTestImpl


class RNNTFloat32CPUTest(RNNTTestImpl, PytorchTestCase):
    dtype = torch.float32
    device = torch.device("cpu")


class RNNTFloat64CPUTest(RNNTTestImpl, PytorchTestCase):
    dtype = torch.float64
    device = torch.device("cpu")
