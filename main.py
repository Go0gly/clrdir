#!/usr/bin/env python3
import sys, os

# Variables
args = sys.argv[1::]
ignore_list = []
keywords = ("-h", "--help", "-i", "--ignore", "-rm", "--rmdir")
path = None
rmdir = False

# Processing arguments
for index,arg in enumerate(args):
    if index == 0 and arg not in keywords:
        path = arg
    elif arg == "-h" or arg == "--help":
        print("clrdir [DIRECTORY: REQUIRED - path] [-i, --ignore: OPTIONAL - args] [-rm, --rmdir: OPTIONAL - toggle] [-h, --help: OPTIONAL - toggle]")
        print("DIRECTORY -- The directory that gets cleared")
        print("-i, --ignore [args] -- Files/directories to ignore when clearing the directory")
        print("-rm, --rmdir -- Off by default, deletes the specified directory if on")
        print("-h, --help -- Prints this menu")
    elif arg == "-i" or arg == "--ignore":
        for _ in args[index+1::]:
            if _ not in keywords:
                ignore_list.append(_)
            else:
                break
    elif arg == "-rm" or arg == "--rmdir":
        rmdir = True

def clrdir(path: str, ignore_list: list, rmdir: bool):
    original_path = os.getcwd()
    os.chdir(path)
    for file in os.listdir():
        if file in ignore_list:
            continue
        else:
            try:
                os.remove(file)
            except IsADirectoryError:
                clrdir(file, ignore_list, True)
    os.chdir(original_path)
    if rmdir:
        try:
            os.rmdir(path)
        except:
            pass

clrdir(path, ignore_list, rmdir)