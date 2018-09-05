import os
import argparse
import hashlib


def create_args_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--filepath', required=True)
    return parser

dir = 'C:\\projects\\devman\\new\\dublicates\\test_dir'

def create_abs_filepaths(top_root_path):
    abs_filepaths = []
    for root_dir, nested_dir, files_in_nested_dir in os.walk(top_root_path):
        for file in files_in_nested_dir:
            abs_filepaths.append(os.path.join(root_dir, file))
    return abs_filepaths


def define_file_hash_md5(abs_filepath, blocksize=4096):
    file_hash_md5 = hashlib.md5()
    print(file_hash_md5)
    with open(abs_filepath, "rb") as opened_file:
        for block in iter(lambda: opened_file.read(blocksize), b''):
            file_hash_md5.update(block)
    return file_hash_md5.hexdigest()


def detect_dublicates(abs_filepaths_list):
    dublicated_files = []
    non_dublicated_files = []

for filepath in create_abs_filepaths(dir):
    print(filepath, define_file_hash_md5(filepath))

