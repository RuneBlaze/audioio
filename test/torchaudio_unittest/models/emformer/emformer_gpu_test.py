import torch
from torchffmpeg_unittest.common_utils import PytorchTestCase, skipIfNoCuda
from torchffmpeg_unittest.models.emformer.emformer_test_impl import EmformerTestImpl


@skipIfNoCuda
class EmformerFloat32GPUTest(EmformerTestImpl, PytorchTestCase):
    dtype = torch.float32
    device = torch.device("cuda")


@skipIfNoCuda
class EmformerFloat64GPUTest(EmformerTestImpl, PytorchTestCase):
    dtype = torch.float64
    device = torch.device("cuda")
