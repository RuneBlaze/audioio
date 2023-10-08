"""Replaces every instance of 'torchffmpeg._backend' with 'torchffmpeg' in torchffmpeg.html.
Temporary hack while we maintain both the existing set of info/load/save functions and the
new ones backed by the backend dispatcher in torchffmpeg._backend.
"""
import sys

if __name__ == "__main__":
    build_dir = sys.argv[1]
    filepath = f"{build_dir}/html/torchffmpeg.html"

    with open(filepath, "r") as f:
        text = f.read()
        text = text.replace("torchffmpeg._backend", "torchffmpeg")

    with open(filepath, "w") as f:
        f.write(text)
