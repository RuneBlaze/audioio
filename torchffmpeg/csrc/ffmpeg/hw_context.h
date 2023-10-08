#pragma once

#include <torchffmpeg/csrc/ffmpeg/ffmpeg.h>

namespace torchffmpeg::io {

AVBufferRef* get_cuda_context(int index);

void clear_cuda_context_cache();

} // namespace torchffmpeg::io
