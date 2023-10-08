torchffmpeg
==========

.. note::
   Release 2.1 will revise ``torchffmpeg.info``, ``torchffmpeg.load``, and ``torchffmpeg.save`` to allow for backend selection via function parameter rather than ``torchffmpeg.set_audio_backend``, with FFmpeg being the default backend.
   The new API can be enabled in the current release by setting environment variable ``TORCHFFMPEG_USE_BACKEND_DISPATCHER=1``.
   See :ref:`future_api` for details on the new API.


Current API
-----------

I/O functionalities
~~~~~~~~~~~~~~~~~~~

Audio I/O functions are implemented in :ref:`torchffmpeg.backend<backend>` module, but for the ease of use, the following functions are made available on :mod:`torchffmpeg` module. There are different backends available and you can switch backends with :func:`set_audio_backend`.


Please refer to :ref:`backend` for the detail, and the :doc:`Audio I/O tutorial <../tutorials/audio_io_tutorial>` for the usage.

.. function:: torchffmpeg.info(filepath: str, ...)

   Fetch meta data of an audio file. Refer to :ref:`backend` for the detail.

.. function:: torchffmpeg.load(filepath: str, ...)

   Load audio file into torch.Tensor object. Refer to :ref:`backend` for the detail.

.. function:: torchffmpeg.save(filepath: str, src: torch.Tensor, sample_rate: int, ...)

   Save torch.Tensor object into an audio format. Refer to :ref:`backend` for the detail.

.. currentmodule:: torchffmpeg

Backend Utilities
~~~~~~~~~~~~~~~~~

.. autofunction:: list_audio_backends

.. autofunction:: get_audio_backend

.. autofunction:: set_audio_backend


.. _future_api:

Future API
----------

In the next release, each of ``torchffmpeg.info``, ``torchffmpeg.load``, and ``torchffmpeg.save`` will allow for selecting a backend to use via parameter ``backend``.
The functions will support using any of FFmpeg, SoX, and SoundFile, provided that the corresponding library is installed.
If a backend is not explicitly chosen, the functions will select a backend to use given order of precedence (FFmpeg, SoX, SoundFile) and library availability.

Note that only FFmpeg and SoundFile will support file-like objects.

These functions can be enabled in the current release by setting environment variable ``TORCHFFMPEG_USE_BACKEND_DISPATCHER=1``.

.. currentmodule:: torchffmpeg._backend

.. autofunction:: info
   :noindex:

.. autofunction:: load
   :noindex:

.. autofunction:: save
   :noindex:
