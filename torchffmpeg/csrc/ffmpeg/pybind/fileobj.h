#pragma once
#include <torch/extension.h>
#include <torchffmpeg/csrc/ffmpeg/ffmpeg.h>

namespace torchffmpeg {
namespace io {

struct FileObj {
  py::object fileobj;
  int buffer_size;
  AVIOContextPtr pAVIO;
  FileObj(py::object fileobj, int buffer_size, bool writable);
};

} // namespace io
} // namespace torchffmpeg
