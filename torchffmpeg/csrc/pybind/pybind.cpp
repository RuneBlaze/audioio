#include <torch/extension.h>
#include <torchffmpeg/csrc/utils.h>

namespace torchffmpeg {
namespace {

PYBIND11_MODULE(_torchffmpeg, m) {
  m.def("is_kaldi_available", &is_kaldi_available, "");
  m.def("is_rir_available", &is_rir_available, "");
  m.def("cuda_version", &cuda_version, "");
}

} // namespace
} // namespace torchffmpeg
