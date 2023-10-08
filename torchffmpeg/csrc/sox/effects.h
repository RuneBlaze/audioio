#ifndef TORCHFFMPEG_SOX_EFFECTS_H
#define TORCHFFMPEG_SOX_EFFECTS_H

#include <torch/script.h>
#include <torchffmpeg/csrc/sox/utils.h>

namespace torchffmpeg {
namespace sox_effects {

void initialize_sox_effects();

void shutdown_sox_effects();

auto apply_effects_tensor(
    torch::Tensor waveform,
    int64_t sample_rate,
    const std::vector<std::vector<std::string>>& effects,
    bool channels_first) -> std::tuple<torch::Tensor, int64_t>;

auto apply_effects_file(
    const std::string& path,
    const std::vector<std::vector<std::string>>& effects,
    c10::optional<bool> normalize,
    c10::optional<bool> channels_first,
    const c10::optional<std::string>& format)
    -> c10::optional<std::tuple<torch::Tensor, int64_t>>;

} // namespace sox_effects
} // namespace torchffmpeg

#endif
