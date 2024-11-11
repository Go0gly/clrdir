#!/usr/bin/env python3
import sys, os

# Variables
args = sys.argv[1::]
ignore_list = []
keywords = ("-h", "--help", "-i", "--ignore", "-rm", "--rmdir")
path = None
rmdir = False

# Processing arguments
if len(args) == 0:
    print(f"\033[31;1mError\033[m: No directory provided")
    sys.exit(1)

for index,arg in enumerate(args):
    if index == 0 and arg not in keywords:
        path = arg
    elif arg == "-h" or arg == "--help":
        print(f"Usage: {sys.argv[1]} <DIRECTORY> [OPTIONS]")
        print("\tDIRECTORY -- The directory that gets cleared")
        print("\tOPTIONS:")
        print("\t\t-i, --ignore [args] -- Files/directories to ignore when clearing the directory")
        print("\t\t-rm, --rmdir -- Off by default, deletes the specified directory if on")
        print("\t\t-h, --help -- Prints this menu")
    elif arg == "-i" or arg == "--ignore":
        for _ in args[index+1::]:
            if _ not in keywords:
                ignore_list.append(_)
    elif arg == "-rm" or arg == "--rmdir":
        rmdir = True

def clrdir(path: str, ignore_list: list, rmdir: bool):
    original_path = os.getcwd()
    try:
        os.chdir(path)
    except:
        print(f"\033[31;1mError\033[m: Unable to change directory to {path}")
        sys.exit(1)
    for file in os.listdir():
        if file in ignore_list:
            continue
        else:
            try:
                os.remove(file)
            except IsADirectoryError:
                clrdir(file, ignore_list, True)
                print(f"Entering {file}")
            else:
                print(f"Deleting {file}")
    os.chdir(original_path)
    if rmdir:
        try:
            os.rmdir(path)
        except:
            pass

clrdir(path, ignore_list, rmdir)