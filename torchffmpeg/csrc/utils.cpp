#include <torch/script.h>
#include <torchffmpeg/csrc/utils.h>

#ifdef USE_CUDA
#include <cuda.h>
#endif

namespace torchffmpeg {

bool is_kaldi_available() {
#ifdef INCLUDE_KALDI
  return true;
#else
  return false;
#endif
}

bool is_rir_available() {
#ifdef INCLUDE_RIR
  return true;
#else
  return false;
#endif
}

c10::optional<int64_t> cuda_version() {
#ifdef USE_CUDA
  return CUDA_VERSION;
#else
  return {};
#endif
}

} // namespace torchffmpeg
