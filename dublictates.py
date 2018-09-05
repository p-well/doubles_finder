import os
import argparse


def create_args_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--filepath', required=True)
    return parser

dir = 'C:\\projects\\devman\\new\\dublicates'

def create_abs_filepaths(top_root_path):
    abs_filepaths = []
    for root_dir, nested_dir, files_in_nested_dir in os.walk(top_root_path):
        for file in files_in_nested_dir:
            abs_filepaths.append(os.path.join(root_dir, file))
    return abs_filepaths


print(create_abs_filepaths(dir))

