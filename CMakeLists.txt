cmake_minimum_required(VERSION 2.8 FATAL_ERROR)

project(pythonFFT)

enable_language(C)

set(CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} ${PROJECT_SOURCE_DIR}/cmake)

find_package(FFTW REQUIRED)

include_directories(${PROJECT_SOURCE_DIR}/api)
include_directories(${FFTW_INCLUDES})

add_library(
    example
    SHARED
    src/testFFT.c
    )

target_link_libraries(example ${FFTW_LIBRARIES})
