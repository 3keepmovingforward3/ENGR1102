#! /usr/bin/env pypy3

# Benjamin Blouin
# 2/28/2018
#
# This script can find a file by name, e.g. test.py, and also can take
# the wild card *, e.g. test.py*, and takes a flag -r, for recursive search
# When a match is found, the file is hashed and the hash is saved in a new
# text file in the same folder

import hashlib
import os

import fahmf_functions

base_hash = hashlib.sha3_512()
x = fahmf_functions
args, s = x.my_parser()
x.my_glob(os.getcwd(), args, s, base_hash)
