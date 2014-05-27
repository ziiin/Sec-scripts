#! /usr/bin/python
'''
This script crawls through the first argument given to it
and prints in the following format:
FILE_PATH :: FILE_TYPE :: DATA-CHECKSUM
[TODO] print MODE :: UID :: GID too
'''
import os
import sys
from stat import *

def crawl (root):
    try:
        root_stat = os.stat (root)
    except OSError as oe:
        print ("OS error({0}), reason: {1}".format(oe.errno, oe.strerror))
    if not S_ISDIR(root_stat.st_mode):
        print ("{0}".format(root))
    else:
        for path in os.listdir(root):
            print ("{0}".format(os.path.join(root, path)))
            crawl (os.path.join(root, path))
    # check if root is file or dir
    # list all files in root
    # list all dirs in root
    # for all dirs in root:
    # recursively call crawl

path = raw_input()
print path
crawl (path)
