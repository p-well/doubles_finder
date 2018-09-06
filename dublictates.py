import os
import argparse
import hashlib
import datetime


dirpath = 'C:\\projects\\devman\\new\\dublicates\\test_dir'

def create_args_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--filepath', required=True)
    return parser


def create_abs_filepaths(top_root_path):
    abs_filepaths = []
    for root_dir, nested_dir, files_in_nested_dir in os.walk(top_root_path):
        for file in files_in_nested_dir:
            abs_filepaths.append(os.path.join(root_dir, file))
    return abs_filepaths


def define_file_hash_md5(abs_filepath, blocksize=4096):
    file_hash_md5 = hashlib.md5()
    with open(abs_filepath, "rb") as opened_file:
        for block in iter(lambda: opened_file.read(blocksize), b''):
            file_hash_md5.update(block)
    return file_hash_md5.hexdigest()


def check_file_dublication(filepath,
                           file_hash_md5,
                           dublicated_filepaths_list,
                           non_dublicated_filehashes_list):
    if file_hash_md5 in non_dublicated_filehashes_list:
        dublicated_filepaths_list.append(filepath)
    else:
        non_dublicated_filehashes_list.append(file_hash_md5)
    return dublicated_filepaths_list


def print_report(dublicated_filepaths_list):
    if not dublicated_filepaths_list:
        print('Dublicates not found.')
    else:
        print('\nThese are dublicates of files stored higher at tree:\n')
        for counter, filepath in enumerate(dublicated_filepaths_list, start=1):
            file_location, filename = os.path.split(filepath)
            print('{}. Location: {}\tFile: {}'.format(
                counter,
                file_location,
                filename))


def main(top_root_path):
    dublicated_filepaths = []
    non_dublicated_filehashes = []
    abs_filepaths_list = create_abs_filepaths(top_root_path)
    for filepath in abs_filepaths_list:
        file_hash_md5 = define_file_hash_md5(filepath)
        check_file_dublication(filepath,
                               file_hash_md5,
                               dublicated_filepaths,
                               non_dublicated_filehashes)
    print_report(dublicated_filepaths)


if __name__ == "__main__":
    main(dirpath)
