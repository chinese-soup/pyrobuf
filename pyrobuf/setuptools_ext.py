"""Setuptools integration."""
import os
import sys

from pyrobuf.compile import Compiler

if sys.version_info.major == 3:
    basestring = str
    _FileExistsError = FileExistsError
else:
    _FileExistsError = OSError

pyrobuf_proto3_val = False

def add_pyrobuf_module(dist, pyrobuf_module):
    dir_name = "pyrobuf/_" + pyrobuf_module
    package = "{}_{}".format(dist.get_name(), pyrobuf_module)
    try:
        os.makedirs(os.path.join(dir_name, package))
    except _FileExistsError:
        pass
    compiler = Compiler([pyrobuf_module], out=dir_name, package=package, proto3=pyrobuf_proto3_val)
    compiler.extend(dist)


def pyrobuf_modules(dist, attr, value):
    assert attr == 'pyrobuf_modules'
    if isinstance(value, basestring):
        value = [value]

    for pyrobuf_module in value:
        add_pyrobuf_module(dist, pyrobuf_module)


def pyrobuf_proto3(dist, attr, value):
    assert attr == 'pyrobuf_proto3'
    if isinstance(value, bool):
        pyrobuf_proto3_val = value
