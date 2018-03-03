import argparse
import filecmp
import fileinput
import glob
import hashlib
import os
import pathlib
import shutil
import tempfile


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
    print(folder_path_to_save_in)
    print(file_name+'.hash')
    print(file_hashed)


def pathname_finder(file):
    folder_path_to_save_in = os.path.dirname(os.path.realpath(file))
    file_name = os.path.basename(file)
    return folder_path_to_save_in, file_name


def my_glob(p, args, s):
    for file in glob.iglob('{}/{}/{}'.format(p, s, args.filename), recursive=args.flag_recursive):
        if file.is_dir():
            fileinput.nextfile()
        elif pathlib.PurePosixPath(args.filename).suffix == '.hash':
            internal_hash_check(file)


def internal_hash_check(file):
    with open(file, 'r') as f:
        for line in f:
            fp = tempfile.TemporaryFile()
            for temp_line in fileinput.input(fp):
                fp.write(hash_make(temp_line, hashlib.sha384()))
                if filecmp.cmp(file, fp):
                    continue
                else:
                    raise NameError('hashes do not match')
                    log = open('log.txt', 'w')
                    shutil.copy2(fp, log)
                    log.close()
                    fp.close()


