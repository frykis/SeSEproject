[![Build Status](https://travis-ci.org/bast/python-cffi-demo.svg?branch=master)](https://travis-ci.org/bast/python-cffi-demo/builds)
[![License](https://img.shields.io/badge/license-%20BSD--3-blue.svg)](../master/LICENSE)


# python-cffi-demo

- Inspired by Armin Ronacher's ["Beautiful Native Libraries"](http://lucumr.pocoo.org/2013/8/18/beautiful-native-libraries/)


## How to build this demo

```
mkdir build
cd build
cmake ..
make
cd ..
PROJECT_BUILD_DIR=$PWD/build PROJECT_INCLUDE_DIR=$PWD/api PYTHONPATH=$PWD/api py.test test/test.py
```


## Annotated tree

```
.
|-- CMakeLists.txt     # CMake which ties the project together
|-- LICENSE
|-- README.md
|-- api
|   |-- example.h      # C interface to the C code
|   `-- example.py     # CFFI layer
|-- requirements.txt   # required Python modules
|-- src
|   `-- example.c    # Ccode
`-- test
    `-- test.py        # Python code calling C functions
```
