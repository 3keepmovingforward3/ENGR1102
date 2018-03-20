import argparse
import filecmp
import fileinput
import glob
import hashlib
import os
import shutil


mismatches = 0
args=[]

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
    with open('{}/{}.hash'.format(folder_path_to_save_in, file_name), 'w') as f:
        f.write(file_hashed)
        f.close()


def pathname_finder(file):
    folder_path_to_save_in = os.path.dirname(os.path.realpath(file))
    file_name = os.path.basename(file)
    return folder_path_to_save_in, file_name


def my_glob(p, args, s, base_hash):
    for file in glob.iglob('{}/{}/{}'.format(p, s, args.filename), recursive=args.flag_recursive):
        if os.path.isdir(file):
            fileinput.nextfile()
        else:
            with os.scandir(os.path.dirname(os.path.realpath(file))) as it:
                for entry in it:
                    if pathlib2.PurePath(entry).suffix == '.hash':
                        internal_hash_check(entry, args)
        for line in fileinput.input(file):
            folder_path_to_save_in, filename = pathname_finder(file)
            file_hashed = hash_make(line, base_hash)
            hash_write_to_file(file_hashed, folder_path_to_save_in, args.filename)
            fileinput.nextfile()


def internal_hash_check(file, args):
    global mismatches
    fp = open('{}/temp.txt'.format(os.path.dirname(os.path.realpath(file))), 'w+')  # make the temp file 'fp' at path
    f = open('{}/{}'.format(os.path.dirname(os.path.realpath(file)), args.filename), 'r')
    fhash = open('{}/{}.hash'.format(os.path.dirname(os.path.realpath(file)), args.filename), 'r')
    fp.write(hash_make(f.read(), hashlib.sha384()))
    fp.close()
    fhash.close()
    if filecmp.cmp(fhash, fp):
        fp.close()
    else:
        print('hashes do not match')
        shutil.copy(fp, 'log.txt')
        fp.close()
        mismatches += 1
    return
