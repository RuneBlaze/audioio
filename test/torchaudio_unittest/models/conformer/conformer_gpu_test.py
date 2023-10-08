import torch
from torchffmpeg_unittest.common_utils import PytorchTestCase, skipIfNoCuda
from torchffmpeg_unittest.models.conformer.conformer_test_impl import ConformerTestImpl


@skipIfNoCuda
class ConformerFloat32GPUTest(ConformerTestImpl, PytorchTestCase):
    dtype = torch.float32
    device = torch.device("cuda")


@skipIfNoCuda
class ConformerFloat64GPUTest(ConformerTestImpl, PytorchTestCase):
    dtype = torch.float64
    device = torch.device("cuda")
