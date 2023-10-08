cmake_minimum_required(VERSION 3.5)

project(libtorchffmpeg-cpp-example)

SET(BUILD_SOX ON CACHE BOOL "Build libsox into libtorchffmpeg")

SET(BUILD_KALDI OFF CACHE BOOL "Build Kaldi into libtorchffmpeg")
SET(BUILD_RNNT ON CACHE BOOL "Build RNN transducer into libtorchffmpeg")
SET(BUILD_TORCHFFMPEG_PYTHON_EXTENSION OFF CACHE BOOL "Build Python binding")

find_package(Torch REQUIRED)
message("libtorchffmpeg CMakeLists: ${TORCH_CXX_FLAGS}")
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} ${TORCH_CXX_FLAGS}")

add_subdirectory(../.. libtorchffmpeg)
add_subdirectory(augmentation)
add_subdirectory(speech_recognition)
