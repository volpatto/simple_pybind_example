# Simple pybind example

| Plataform                               	| Build status 	|
|-----------------------------------------	|--------------	|
| Ubuntu 14.04 LTS and Mac OS X 10.13.3 	|  [![Build Status](https://travis-ci.com/volpatto/simple_pybind_example.svg?branch=master)](https://travis-ci.com/volpatto/simple_pybind_example)            	|
| Ubuntu 16.04 LTS and Windows 2019       	|  [![Build Status](https://dev.azure.com/volpatto/volpatto/_apis/build/status/volpatto.simple_pybind_example?branchName=master)](https://dev.azure.com/volpatto/volpatto/_build/latest?definitionId=3&branchName=master)            	|

## TL;DR

Here, a simple example about how to bind C++ code in Python is provided. The structure try to be not invasive as much as possible concerning the C++ extension. 

## Now a longer description

My idea is provide a structure to bind a C++ extension code to a Python base code. The C++ library (here, the extension we want to bind) can be anything that compiles standalone with its own `CMakeLists` (I use `CMake` here, so deal with it), and is exposed as a library that can be linked by others `CMakeLists`s.
The structural design aims to plug this extension in the Python base code by providing a binding interface using
[pybind11](https://github.com/pybind/pybind11). Pursuing a generic purpose, I separate the binding module from the C++ extension code. Why? Well, my big and bold target here is to be not invasive while binding, so the binding duty is out of the
C++ target library. Let's dive in to understand it better.

The basic tree structure of the package directory is shown below:

```console
├── CMakeLists.txt
├── LICENSE
├── python_package
│   ├── bindings
│   │   ├── bindings.cpp
│   │   └── CMakeLists.txt
│   ├── cpp_binding
│   │   └── example_binding.cpython-37m-x86_64-linux-gnu.so
│   ├── _cpp_package
│   │   ├── CMakeLists.txt
│   │   ├── example_cpp.cpp
│   │   └── example_cpp.hpp
│   ├── foo_module.py
│   └── __init__.py
├── README.md
├── setup.cfg
├── setup.py
└── tests
    └── test_foo.py
```

A generic python package named (guess what?! wait for it) `python_package` is our Python module. Inside it, 
all the Python lib stuff is located. Here, just for simplifying things, we consider that there is only one Python module (`foo_module.py`). 
Now, beside Python modules, I inserted the C++ extension. Just as a note, it could be placed out of `python_package` dir, say, `external` or `lib` dirs, for example. Since it's only an extension, not a huge C++ lib actually, I do prefer to put it beside Python modules (personal tastes, you know). The C++ extension is in `_cpp_package` dir. The binding interface is
placed in `binding` dir, with a proper `binding.cpp` file which does all the witchcraft with `pybing11`. An important point
here is to take a look in the `CMakeLists.txt` (actually all the `CMakeLists.txt` worth it, do not underestimate `CMake`'s
evil power) to get a glance of how to use pybind on a target link library.

After all the compilation and linking processes, a shared library will be generated in `cpp_binding` dir.
It can be imported from a python script from this point. But how we could pack it in a Python package? Well, the `setup.py` will do the 
trick for you. You could install it with:

```console
python setup.py develop
```

or

```console
python setup.py install
```

or even with the beloved `pip`:

```console
pip install -e ./
```

Everything above will install the Python package with the C++ extension for you (in a development mode, btw, but working). The
`setup.py` is heavily based on the [official pybind11 cmake example](https://github.com/pybind/cmake_example) and
in this [helpful post here](https://www.benjack.io/2018/02/02/python-cpp-revisited.html). To be honest, 
I must say that these two sources inspired me also in several others features I aimed to reach here. So kudos to the authors!

## Tests

With everything working properly, here come the goodies: Testing C++ codes with Python with the delightful `pytest`.

> "- Oh! Do you mean that there is no `Boost.Test` or `Catch2`?! Wtf, man?! They are great!"

Yeah, I agree. But Python can make things faster (polemical pause, awkward silence). Watch out, I didn't say what will get faster!
In my humble and pretty insignificant opinion, testing things with `pytest` is easier than testing in C++. It could turn the
testing creation stage quickier (of course, if you have good and well designed bindings available).

Examples of tests are provided in `tests` dir. The tests are performed using `pytest`, but could be any other Python test lib.

If you want to see tests working, I defined an alias for it in `setup.cfg` file, just run the below command in your 
terminal:

```console
python setup.py test
```

## Prerequisites

I create isolated environments with [conda](https://conda.io/en/latest/). You can use and create an environment with all the
requirement just doing in the repo root:

```console
conda env create -f environment.yml
```

This will create an environment named `cpp-bindings`. Activate it and you will got all that you need.

> "- Oh! I don't use conda! I even don't know how to use it. Wait, I even don't know what is conda! What could I do?"

Well, no problem. Be sure that you have the following things properly installed in your system (or anything you prefer rather than `conda env`s):

* clangdev >=6.0 (I use `clang` compiler here, but things *should* work OK with `g++` as well)
* cmake
* make
* pybind11 (this one is the most important! you have to be able to find it with CMake's `find_package` command)
* pytest (to run the tests)
* pytest-runner
* python >=3.6.7 (Python greater than 3.7 would be nice!)

You could use Python `virtualenv`s as well, I think it wouldn't be a problem (but I won't do it, if you do you tell me).

## Contributing

> "- Oh! I think you did a terrible work here. This repo is a piece of LOVE!" (edited due to educational reasons)

Thank you! You are very nice! I think you are also a great coder, probably far better than myself (I try my best, I 
promise). If you have any suggestion, correction, improvements or anything that could increase the quality of the content
of the present repo, please feel free to open an issue or, even better, send a PR. I will **really** appreciate that!

## Usage

> "- Oh! I think this repo is a good starting point for a project I have in mind! Can I use it?!"

Don't say more. Free software, MIT license. If it help you in any way, I will be very happy! At least I help someone! This way I am contributing to a better world.

## Contact

My name is Diego Volpatto, feel free to contact me through the email dtvolpatto@gmail.com. However, there is no guarantee
that I can help you.
