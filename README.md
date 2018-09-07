# File Dublicates Searching

The purpose of the script is to find duplicated files in directory tree. <br/>

Script goes recursively into all nested folders and detects dublicates using file hash md5 sum. File with repeated hash is marked as duplication. From 2 files with the same hash those file will be marked as dublicate if it is stored deeper in folders tree. <br/>

File names are not taken into account - dublicates may have different names (the only files content matters).

Pavel Kadantsev, 2018. <br/>
p.a.kadantsev@gmail.com


# Installation and Quickstart

Python 3.5 should be already installed. <br />
Clone this repo on your machnine and run the script by executing ```python duplicates.py <filepath>``` in CLI.


# Example of Script Launch

Successful script launch:

<pre>
<b>>python duplicates.py  C:\projects\devman\new\dublicates\test_dublicates </b>

These are dublicates of files stored higher at tree:

1. Location: C:\projects\devman\new\dublicates\test_dublicates  File: pricelist_june_new.txt
2. Location: C:\projects\devman\new\dublicates\test_dublicates\september        File: price_august.txt
3. Location: C:\projects\devman\new\dublicates\test_dublicates\september        File: price_august_september.txt
</pre>


Running with wrong path (argparses raised raises error):

<pre>
<b>>python dublicates.py -f C:\projects\devman\\new\dublicates\wrong_path </b>
usage: dublictates.py [-h] -f FILEPATH
dublictates.py: error: Path not found.
</pre>


# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
