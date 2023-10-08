#pragma once
#include <torchffmpeg/csrc/ffmpeg/ffmpeg.h>

namespace torchffmpeg {
namespace io {
class PacketBuffer {
 public:
  void push_packet(AVPacket* packet);
  std::vector<AVPacketPtr> pop_packets();
  bool has_packets();

 private:
  std::deque<AVPacketPtr> packets;
};
} // namespace io
} // namespace torchffmpeg
