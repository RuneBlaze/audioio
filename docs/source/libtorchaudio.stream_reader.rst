.. warning::
   TorchAudio's C++ API is a prototype feature.
   API/ABI backward compatibility is not guaranteed.

torchffmpeg::io::StreamReader
============================

.. doxygenclass:: torchffmpeg::io::StreamReader

Constructors
------------

.. doxygenfunction:: torchffmpeg::io::StreamReader::StreamReader(const std::string &src, const c10::optional<std::string> &format = {}, const c10::optional<OptionDict> &option = {})

Query Methods
-------------

find_best_audio_stream
^^^^^^^^^^^^^^^^^^^^^^
.. doxygenfunction:: torchffmpeg::io::StreamReader::find_best_audio_stream

find_best_video_stream
^^^^^^^^^^^^^^^^^^^^^^
.. doxygenfunction:: torchffmpeg::io::StreamReader::find_best_video_stream

get_metadata
^^^^^^^^^^^^
.. doxygenfunction:: torchffmpeg::io::StreamReader::get_metadata

num_src_streams
^^^^^^^^^^^^^^^
.. doxygenfunction:: torchffmpeg::io::StreamReader::num_src_streams

get_src_stream_info
^^^^^^^^^^^^^^^^^^^

.. doxygenfunction:: torchffmpeg::io::StreamReader::get_src_stream_info

num_out_streams
^^^^^^^^^^^^^^^

.. doxygenfunction:: torchffmpeg::io::StreamReader::num_out_streams

get_out_stream_info
^^^^^^^^^^^^^^^^^^^

.. doxygenfunction:: torchffmpeg::io::StreamReader::get_out_stream_info

is_buffer_ready
^^^^^^^^^^^^^^^

.. doxygenfunction:: torchffmpeg::io::StreamReader::is_buffer_ready

Configure Methods
-----------------

add_audio_stream
^^^^^^^^^^^^^^^^

.. doxygenfunction:: torchffmpeg::io::StreamReader::add_audio_stream

add_video_stream
^^^^^^^^^^^^^^^^
.. doxygenfunction:: torchffmpeg::io::StreamReader::add_video_stream

remove_stream
^^^^^^^^^^^^^
.. doxygenfunction:: torchffmpeg::io::StreamReader::remove_stream

Stream Methods
^^^^^^^^^^^^^^

seek
^^^^
.. doxygenfunction:: torchffmpeg::io::StreamReader::seek

process_packet
^^^^^^^^^^^^^^
.. doxygenfunction:: torchffmpeg::io::StreamReader::process_packet()

process_packet_block
^^^^^^^^^^^^^^^^^^^^
.. doxygenfunction:: torchffmpeg::io::StreamReader::process_packet_block

process_all_packets
^^^^^^^^^^^^^^^^^^^
.. doxygenfunction:: torchffmpeg::io::StreamReader::process_all_packets

fill_buffer
^^^^^^^^^^^
.. doxygenfunction:: torchffmpeg::io::StreamReader::fill_buffer

Retrieval Methods
-----------------

pop_chunks
^^^^^^^^^^

.. doxygenfunction:: torchffmpeg::io::StreamReader::pop_chunks


Support Structures
------------------

Chunk
^^^^^

.. container:: py attribute

   .. doxygenstruct:: torchffmpeg::io::Chunk
      :members:

SrcStreaminfo
^^^^^^^^^^^^^

.. container:: py attribute

   .. doxygenstruct:: torchffmpeg::io::SrcStreamInfo
      :members:

OutputStreaminfo
^^^^^^^^^^^^^^^^

.. container:: py attribute

   .. doxygenstruct:: torchffmpeg::io::OutputStreamInfo
      :members:
