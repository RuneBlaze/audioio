#pragma once
#include <torchffmpeg/csrc/ffmpeg/ffmpeg.h>

namespace torchffmpeg::io {
class PacketWriter {
  AVFormatContext* format_ctx;
  AVStream* stream;
  AVRational original_time_base;

 public:
  PacketWriter(
      AVFormatContext* format_ctx_,
      const StreamParams& stream_params_);
  void write_packet(const AVPacketPtr& packet);
};
} // namespace torchffmpeg::io
