.. _backend:

torchffmpeg.backend
==================

.. py:module:: torchffmpeg.backend

Overview
~~~~~~~~

:mod:`torchffmpeg.backend` module provides implementations for audio file I/O functionalities, which are ``torchffmpeg.info``, ``torchffmpeg.load``, and ``torchffmpeg.save``.

.. note::
   Release 2.1 will revise ``torchffmpeg.info``, ``torchffmpeg.load``, and ``torchffmpeg.save`` to allow for backend selection via function parameter rather than ``torchffmpeg.set_audio_backend``, with FFmpeg being the default backend.
   The new logic can be enabled in the current release by setting environment variable ``TORCHFFMPEG_USE_BACKEND_DISPATCHER=1``.
   See :ref:`future_api` for details on the new API.

There are currently two implementations available.

* :py:mod:`"sox_io" <torchffmpeg.backends.sox_io_backend>` (default on Linux/macOS)
* :py:mod:`"soundfile" <torchffmpeg.backends.soundfile_backend>` (default on Windows)

.. note::
   Instead of calling functions in ``torchffmpeg.backend`` directly, please use ``torchffmpeg.info``, ``torchffmpeg.load``, and ``torchffmpeg.save`` with proper backend set with :func:`torchffmpeg.set_audio_backend`.

Availability
------------

``"sox_io"`` backend requires C++ extension module, which is included in Linux/macOS binary distributions. This backend is not available on Windows.

``"soundfile"`` backend requires ``SoundFile``. Please refer to `the SoundFile documentation <https://pysoundfile.readthedocs.io/en/latest/>`_ for the installation.

Common Data Structure
~~~~~~~~~~~~~~~~~~~~~

Structures used to report the metadata of audio files.

AudioMetaData
-------------

.. autoclass:: torchffmpeg.backend.common.AudioMetaData

.. py:module:: torchffmpeg.backend.sox_io_backend

Sox IO Backend
~~~~~~~~~~~~~~

The ``sox_io`` backend is available and default on Linux/macOS and not available on Windows.

I/O functions of this backend support `TorchScript <https://pytorch.org/docs/stable/jit.html>`_.

You can switch from another backend to the ``sox_io`` backend with the following;

.. code::

   torchffmpeg.set_audio_backend("sox_io")

info
----

.. autofunction:: torchffmpeg.backend.sox_io_backend.info

load
----

.. autofunction:: torchffmpeg.backend.sox_io_backend.load

save
----

.. autofunction:: torchffmpeg.backend.sox_io_backend.save

.. py:module:: torchffmpeg.backend.soundfile_backend

Soundfile Backend
~~~~~~~~~~~~~~~~~

The ``"soundfile"`` backend is available when `SoundFile <https://pysoundfile.readthedocs.io/en/latest/>`_ is installed. This backend is the default on Windows.

You can switch from another backend to the ``"soundfile"`` backend with the following;

.. code::

   torchffmpeg.set_audio_backend("soundfile")

info
----

.. autofunction:: torchffmpeg.backend.soundfile_backend.info

load
----

.. autofunction:: torchffmpeg.backend.soundfile_backend.load

save
----

.. autofunction:: torchffmpeg.backend.soundfile_backend.save
