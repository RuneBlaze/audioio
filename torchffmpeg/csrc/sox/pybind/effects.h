#ifndef TORCHFFMPEG_PYBIND_SOX_EFFECTS_H
#define TORCHFFMPEG_PYBIND_SOX_EFFECTS_H

#include <torch/extension.h>

namespace torchffmpeg {
namespace sox_effects {

auto apply_effects_fileobj(
    py::object fileobj,
    const std::vector<std::vector<std::string>>& effects,
    c10::optional<bool> normalize,
    c10::optional<bool> channels_first,
    c10::optional<std::string> format)
    -> c10::optional<std::tuple<torch::Tensor, int64_t>>;

} // namespace sox_effects
} // namespace torchffmpeg

#endif
