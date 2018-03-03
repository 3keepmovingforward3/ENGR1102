import argparse
import filecmp
import fileinput
import glob
import hashlib
import os
import shutil
import tempfile

import pathlib2

mismatches = 0


def my_parser():
    parser = argparse.ArgumentParser(description='Hash some files')
    parser.add_argument('filename', action="store", type=str)
    parser.add_argument('-r', action='store_true',
                        default=False,
                        dest='flag_recursive',
                        help='Set hashing to recursive')
    args = parser.parse_args()
    if args.flag_recursive:
        s = '**'
    else:
        s = ''

    return parser.parse_args(), s


def hash_make(line, base_hash):
    buf = line.encode('utf-8')
    base_hash.update(buf)
    return base_hash.hexdigest()


def hash_write_to_file(file_hashed, folder_path_to_save_in, file_name):  # right now just printing
    with open('{}.hash'.format(file_name), 'w') as f:
        f.write(file_hashed)
        f.close()


def pathname_finder(file):
    folder_path_to_save_in = os.path.dirname(os.path.realpath(file))
    file_name = os.path.basename(file)
    return folder_path_to_save_in, file_name


def my_glob(p, args, s):
    for file in glob.iglob('{}/{}/{}'.format(p, s, args.filename), recursive=args.flag_recursive):
        if os.path.isdir(file):
            fileinput.nextfile()
        else:
            with os.scandir(os.path.dirname(os.path.realpath(file))) as it:  # pathlib2.PurePosixPath(args.filename).suffix == '.hash':
                for entry in it:
                    if pathlib2.PurePosixPath(entry).suffix == '.hash':
                        


def internal_hash_check(file):
    global mismatches
    fp, path = tempfile.mkstemp(suffix='temp', text=True)  # make the temp file 'fp' at path
    with open(file, 'r') as f:
        for line in fileinput.input(f):
                os.write(fp, hash_make(line, hashlib.sha384()))
                os.close(fp)
                if filecmp.cmp(file, fp):
                    fp.close()
                else:
                    print('hashes do not match')
                    shutil.copy(fp, 'log.txt')
                    fp.close()
                    mismatches += 1

