#!/bin/bash/python3

# Get the Python file name from the environment variable
pyfile=$PYFILE

# Compile the Python file
python -m py_compile $pyfile

# Rename the compiled file
pycfile=${pyfile%.*}.pyc
mv $pycfile ${pycfile}c
