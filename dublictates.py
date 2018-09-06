iimport os
import argparse
import hashlib
import datetime


dir = 'C:\\Temp\\'

def create_args_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--filepath', required=True)
    return parser


def create_abs_filepaths(top_root_path):
    abs_filepaths = []
    for root_dir, nested_dir, files_in_nested_dir in os.walk(top_root_path):
        #print(files_in_nested_dir)
        for file in files_in_nested_dir:
#            print(file)
            abs_filepaths.append(os.path.join(root_dir, file))
    return abs_filepaths


def define_file_hash_md5(abs_filepath, blocksize=4096):
    file_hash_md5 = hashlib.md5()
    with open(abs_filepath, "rb") as opened_file:
        for block in iter(lambda: opened_file.read(blocksize), b''):
            file_hash_md5.update(block)
    return file_hash_md5.hexdigest()



def main(abs_filepaths_list):
    dublicated_filepaths = []
    non_dublicated_files_hashes = []
    for filepath in abs_filepaths_list:
        file_hash_md5 = define_file_hash_md5(filepath)
        if file_hash_md5 in non_dublicated_files_hashes:
            dublicated_filepaths.append(filepath)
        else:
            non_dublicated_files_hashes.append(file_hash_md5)
    return dublicated_filepaths


#for filepath in create_abs_filepaths(dir):
#    define_file_hash_md5(filepath)
#    print(filepath, define_file_hash_md5(filepath))
dt_start = datetime.datetime.now()
abs_filepaths_list = create_abs_filepaths(dir)
#print(main(abs_filepaths_list))
dt_finish = datetime.datetime.now()
delta = dt_finish - dt_start
print(delta)
