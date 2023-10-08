.. py:module:: torchffmpeg.models

torchffmpeg.models
=================

.. currentmodule:: torchffmpeg.models

The ``torchffmpeg.models`` subpackage contains definitions of models for addressing common audio tasks.

.. note::
   For models with pre-trained parameters, please refer to :mod:`torchffmpeg.pipelines` module.

Model defintions are responsible for constructing computation graphs and executing them.

Some models have complex structure and variations.
For such models, factory functions are provided.

.. autosummary::
   :toctree: generated
   :nosignatures:
   :template: autosummary/model_class.rst

   Conformer
   ConvTasNet
   DeepSpeech
   Emformer
   HDemucs
   HuBERTPretrainModel
   RNNT
   RNNTBeamSearch
   Tacotron2
   Wav2Letter
   Wav2Vec2Model
   WaveRNN
