#! /usr/bin/env python3

#Benjamin Blouin
#2/28/2018
#
#This script can find a file by name, e.g. test.py, and also can take
#the wildcard *, e.g. test.py*, and takes a flag -r, for recursive search
#When a match is found, the file is hashed and the hash is saved in a new 
#text file in the same folder

import hashlib, fileinput, pathlib,os,glob,argparse
from sys import argv


def myParser():
    parser = argparse.ArgumentParser(description='Hash some files')
    parser.add_argument('filename', action="store", type=str)
    parser.add_argument('-r', action='store_true',
                        default=False,
                        dest='flag_recursive',
                        help='Set hashing to recursive')    
    args = parser.parse_args()
    if args.flag_recursive == True:
        s = '**'
    else:
        s=''    
    
    return(parser.parse_args(),s)

def process(line,hasher):
    buf = line.encode('utf-16')
    hasher.update(buf)
    return((hasher.hexdigest()))

args,s = myParser()
hasher = hashlib.sha384()
p = os.getcwd()

for file in glob.glob('{}/{}/{}'.format(p,s,args.filename),recursive=args.flag_recursive):
    for line in fileinput.input(file):
        full_path = os.path.realpath(file)
        folder_path_to_save_in = os.path.dirname(full_path)
        l = os.path.basename(file)
        theHash = process(line,hasher)
        f = open('{}/{}-hash-sha384.txt'.format(folder_path_to_save_in,l),'w')
        f.write(theHash)
        print(full_path)
        print(theHash)
        f.close()
        fileinput.nextfile()
        fileinput.close()
