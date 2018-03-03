import argparse
import os


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
    print(file_name)
    print(file_hashed)


def pathname_finder(file):
    folder_path_to_save_in = os.path.dirname(os.path.realpath(file))
    file_name = os.path.basename(file)
    return folder_path_to_save_in, file_name
