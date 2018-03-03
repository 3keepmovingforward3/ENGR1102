#! /usr/bin/env pypy3

# Benjamin Blouin
# 2/28/2018
#
# This script can find a file by name, e.g. test.py, and also can take
# the wildcard *, e.g. test.py*, and takes a flag -r, for recursive search
# When a match is found, the file is hashed and the hash is saved in a new
# text file in the same folder

import fileinput
import hashlib
import os

import fahmf_functions

base_hash = hashlib.sha384()
p = os.getcwd()
x = fahmf_functions
args, s = x.my_parser()
file = x.my_glob(p, args, s)

for line in fileinput.input(file):
        folder_path_to_save_in, filename = x.pathname_finder(file)
        file_hashed = x.hash_make(line, base_hash)
        x.hash_write_to_file(file_hashed, folder_path_to_save_in, args.filename)
        fileinput.nextfile()
        fileinput.close()
