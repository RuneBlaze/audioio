#!/usr/bin/env bash

set -eux

# This script is used by CI to perform smoke tests on installed binaries.

# When `import torchffmpeg` is executed from the root directory of the repo,
# the source `torchffmpeg` directory will shadow the actual installation.
# Changing to this directory to avoid that.
cd -- "$( dirname -- "${BASH_SOURCE[0]}" )"

python smoke_test.py
