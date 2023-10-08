.. warning::
   TorchAudio's C++ API is prototype feature.
   API/ABI backward compatibility is not guaranteed.

torchffmpeg::io::StreamWriter
============================

.. doxygenclass:: torchffmpeg::io::StreamWriter

Constructors
------------

.. doxygenfunction:: torchffmpeg::io::StreamWriter::StreamWriter(const std::string &dst, const c10::optional<std::string> &format = {})

Config methods
--------------

add_audio_stream
^^^^^^^^^^^^^^^^

.. doxygenfunction:: torchffmpeg::io::StreamWriter::add_audio_stream

add_video_stream
^^^^^^^^^^^^^^^^

.. doxygenfunction:: torchffmpeg::io::StreamWriter::add_video_stream

set_metadata
^^^^^^^^^^^^

.. doxygenfunction:: torchffmpeg::io::StreamWriter::set_metadata

Write methods
-------------

open
^^^^

.. doxygenfunction:: torchffmpeg::io::StreamWriter::open

close
^^^^^

.. doxygenfunction:: torchffmpeg::io::StreamWriter::close

write_audio_chunk
^^^^^^^^^^^^^^^^^

.. doxygenfunction:: torchffmpeg::io::StreamWriter::write_audio_chunk

write_video_chunk
^^^^^^^^^^^^^^^^^

.. doxygenfunction:: torchffmpeg::io::StreamWriter::write_video_chunk

flush
^^^^^

.. doxygenfunction:: torchffmpeg::io::StreamWriter::flush
