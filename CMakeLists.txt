cmake_minimum_required(VERSION 2.8 FATAL_ERROR)

project(pythonFFT)

enable_language(C)

set(CMAKE_C_FLAGS "-lfftw3")

include_directories(${PROJECT_SOURCE_DIR}/api)

add_library(
    example
    SHARED
    src/testFFT.c
    )
