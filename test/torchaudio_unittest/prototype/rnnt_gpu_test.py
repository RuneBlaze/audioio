import torch
from torchffmpeg_unittest.common_utils import PytorchTestCase, skipIfNoCuda
from torchffmpeg_unittest.prototype.rnnt_test_impl import ConformerRNNTTestImpl


@skipIfNoCuda
class ConformerRNNTFloat32GPUTest(ConformerRNNTTestImpl, PytorchTestCase):
    dtype = torch.float32
    device = torch.device("cuda")


@skipIfNoCuda
class ConformerRNNTFloat64GPUTest(ConformerRNNTTestImpl, PytorchTestCase):
    dtype = torch.float64
    device = torch.device("cuda")
