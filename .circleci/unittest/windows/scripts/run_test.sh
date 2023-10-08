#!/usr/bin/env bash

set -ex

eval "$(./conda/Scripts/conda.exe 'shell.bash' 'hook')"
conda activate ./env

this_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
source "$this_dir/set_cuda_envs.sh"

python -m torch.utils.collect_env
env | grep TORCHFFMPEG || true

cd test
pytest --cov=torchffmpeg --junitxml=../test-results/junit.xml -v --durations 20 torchffmpeg_unittest
coverage html
