#pragma once
#include <torch/torch.h>
#include <torchffmpeg/csrc/ffmpeg/ffmpeg.h>

namespace torchffmpeg {
namespace io {
namespace detail {

//////////////////////////////////////////////////////////////////////////////
// Helper functions
//////////////////////////////////////////////////////////////////////////////
torch::Tensor convert_audio(AVFrame* frame);

torch::Tensor convert_image(AVFrame* frame, const torch::Device& device);

} // namespace detail
} // namespace io
} // namespace torchffmpeg
