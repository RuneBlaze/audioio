#!/usr/bin/env bash

set -e

eval "$(./conda/bin/conda shell.bash hook)"
conda activate ./env

python -m torch.utils.collect_env
env | grep TORCHFFMPEG || true

export PATH="${PWD}/third_party/install/bin/:${PATH}"

declare -a args=(
    '-v'
    '--cov=torchffmpeg'
    "--junitxml=${PWD}/test-results/junit.xml"
    '--durations' '20'
)

cd test
pytest "${args[@]}" torchffmpeg_unittest
coverage html
