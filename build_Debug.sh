#!/bin/bash

[ ! -d "./build" ] && mkdir build

cd ./build

conan install .. -s build_type=Debug --build=missing

cmake .. -DCMAKE_TOOLCHAIN_FILE=conan_toolchain.cmake

cmake --build . --config Debug

$SHELL
