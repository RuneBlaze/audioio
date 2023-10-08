#pragma once

#include "torchffmpeg/csrc/ffmpeg/ffmpeg.h"
#include "torchffmpeg/csrc/ffmpeg/stream_writer/stream_writer.h"

namespace torchffmpeg::io {
struct CustomIO {
  AVIOContextPtr io_ctx;
  CustomIO(
      void* opaque,
      int buffer_size,
      int (*write_packet)(void* opaque, uint8_t* buf, int buf_size),
      int64_t (*seek)(void* opaque, int64_t offset, int whence));
};

struct StreamWriterCustomIO : private CustomIO, public StreamWriter {
  StreamWriterCustomIO(
      void* opaque,
      const c10::optional<std::string>& format,
      int buffer_size,
      int (*write_packet)(void* opaque, uint8_t* buf, int buf_size),
      int64_t (*seek)(void* opaque, int64_t offset, int whence));
};
} // namespace torchffmpeg::io
