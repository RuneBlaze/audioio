#ifndef TORCHFFMPEG_PYBIND_SOX_EFFECTS_CHAIN_H
#define TORCHFFMPEG_PYBIND_SOX_EFFECTS_CHAIN_H

#include <torch/extension.h>
#include <torchffmpeg/csrc/sox/effects_chain.h>

namespace torchffmpeg {
namespace sox_effects_chain {

class SoxEffectsChainPyBind : public SoxEffectsChain {
  using SoxEffectsChain::SoxEffectsChain;

 public:
  void addInputFileObj(
      sox_format_t* sf,
      char* buffer,
      uint64_t buffer_size,
      py::object* fileobj);

  void addOutputFileObj(
      sox_format_t* sf,
      char** buffer,
      size_t* buffer_size,
      py::object* fileobj);
};

} // namespace sox_effects_chain
} // namespace torchffmpeg

#endif
