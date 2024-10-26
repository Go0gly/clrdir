# Table of Contents
- Table of Contents
- Documentation
    - `DIR`
    - `IGNORE_LIST`
    - `RMDIR`
    - `HELP`
- Installation Guide
    - Install Script
    - Manual Install

# Documentation
`clrdir` is a command that intends to improve users' expieriences by providing a command that can clear out a folder of all its contents, it has many arguments, such as:  

`clrdir [DIR] [IGNORE_LIST] [RMDIR] [HELP]`

| Argument | Description | Labels | Required |
|----------|-------------|--------|----------|
| `DIR`    | The directory to remove | None | Yes |
| `IGNORE_LIST` | The list of files to ignore | `-i` `--ignore` | No |
| `RMDIR` | Removes DIR when done | `-rm` `--rmdir` | No
| `HELP` | Prints a help menu | `-h` `--help` | No |

## `DIR`
A required argument which takes a directory path as an argument, the specified directory will then be cleared out  
  
**Example**:
```bash
# Clears out example_dir
clrdir example_dir
```
Where `example_dir` is `DIR`  

## `IGNORE_LIST`
An optional argument that takes multiple files and directories as arguments.
It then goes ignores the given files and directories when clearing out `DIR`. It is initialized by using `-i` or `--ignore`  
  
**Examples**:
```bash
# Clears out example_dir, but doesn't remove ssn.txt, example.json, or ex_dir_2
clrdir example_dir --ignore ssn.txt example.json ex_dir_2
```
This performs the same action, but uses `-i` instead of `--ignore`
```bash
# Clears out example_dir, but doesn't remove ssn.txt, example.json, or ex_dir_2
clrdir example_dir -i ssn.txt example.json ex_dir_2
```

## `RMDIR`
An optional argument that, if declared, will remove `DIR` after done clearing it out, this cannot be used alongside `IGNORE`. `RMDIR` is declared using either `-rm` or `--rmdir`.  
  
**Examples**
```bash
# Clears out example_dir, and removes example_dir when done
clrdir example_dir --rmdir
```
This does the same action but uses `-rm` instead of `--rmdir`
```bash
# Clears out example_dir, and removes example_dir when done
clrdir example_dir -rm
```

## `HELP`
An optional argument that prints out a menu of what each argument does, takes no arguments. Is declared with `--help` or `-h`  
  
**Example**
```bash
clrdir --help # or clrdir -h
```
Would output:
```
clrdir [DIRECTORY: REQUIRED - path] [-i, --ignore: OPTIONAL - args] [-rm, --rmdir: OPTIONAL - toggle] [-h, --help: OPTIONAL - toggle]
DIRECTORY -- The directory that gets cleared
-i, --ignore [args] -- Files/directories to ignore when clearing the directory
-rm, --rmdir -- Off by default, deletes the specified directory if on
-h, --help -- Prints this menu
```

# Installation Guide
If you want to install `clrdir` directly from source, there are 2 ways to do so. You can do so by using the install script, or by manually installing it. Both of which are covered by this installation guide.  
  
This guide assumes you have both git and python installed on your system. If you don't, install python [here](https://www.python.org/downloads/), and install git [here](https://git-scm.com/downloads)  

First, run these two commands to make sure you're in the right directory
```bash
git clone https://github.com/Go0gly/clrdir.git
cd clrdir
```

## Install Script
If you want to use the installation script to install `clrdir`, then run the following depending on your operating system.  

**Linux/MacOS**
```bash
sudo sh install_unix.sh
```

## Manual Install
If you want to do a manual install of `clrdir`, then you should decide whether you want to customize your installation of `clrdir`. If you don't want any customization, then you should probably just run the install script.  

First, you should think of what you want to name the command. And run the following command
```bash
mv main.py YOUR_CUSTOM_COMMAND_NAME
```
where YOUR_CUSTOM_COMMAND_NAME is the command name you have chosen.  

Next, you need to give `clrdir` permissions to be executed. You can do this by running:
```bash
chmod +x YOUR_CUSTOM_COMMAND_NAME
```
If you want to change the permissions of `clrdir` to something custom, then you might want to do research about `chmod`, but after you run the command above, the default values permissions are currently `rwxr-xr-x`.  

Finally, to move `clrdir` into your path environment, run the following command
```bash
sudo cp YOUR_CUSTOM_COMMAND_NAME /usr/bin
```
You can change `/usr/bin` to whatever path you want, but `/usr/bin` is recommended. To see which directories you have in your path environment, run the following command
```bash
# NOT REQUIRED TO INSTALL
echo $PATH
```
You will see something along the lines of `/usr/bin:/usr/local/bin`, these are all different paths that are separated by a `:`.