#ifndef TORCHFFMPEG_PYBIND_SOX_UTILS_H
#define TORCHFFMPEG_PYBIND_SOX_UTILS_H

#include <torch/extension.h>

namespace torchffmpeg {
namespace sox_utils {

auto read_fileobj(py::object* fileobj, uint64_t size, char* buffer) -> uint64_t;

} // namespace sox_utils
} // namespace torchffmpeg

#endif
