#!/usr/bin/env python3
import subprocess
import sys
import os


# Print an item, takes the item text, if it's the last in the directory, and the preceeding line indentation
def print_item(text, isEnd, line):

    if isEnd:
        print(line + "└── " + text)
    else:
        print(line + "├── " + text)


# Recursively output the contents of the subdirectory
def output_subtree(dirContents, path, depth, isParentEnd, string):

    # Iterate over contents of the directory
    for i in dirContents:

        # Don't output hidden files and directories
        if i[0] == ".":
            continue

        # Determine if the item is the last in the directory
        if i != dirContents[-1]:
            isEnd = False
        else:
            isEnd = True

        # Full path of the new file/dir
        newPath = path + "/" + i

        # If the item is a file, output it
        if os.path.isfile(newPath):
            global numFiles  # need to declare as global before writing to the var
            numFiles = numFiles + 1
            print_item(i, isEnd, string)

        # If the item is a directory, recurse and append to the indentation string
        if os.path.isdir(newPath):
            global numDirs
            numDirs = numDirs + 1

            # Local copy of the indentation string
            temp = string

            # Print the directory title
            print_item(i, isEnd, temp)

            # Determine what to append to the indentation string
            if isEnd:
                temp = string + "    "
            else:
                temp = string + "│   "

            # Recurse, call on the child directory
            output_subtree(os.listdir(newPath), newPath, depth + 1, isParentEnd, temp)


if __name__ == '__main__':

    # If there's an argument
    if len(sys.argv) == 2:
        rootDir = sys.argv[1]  # might need to append os.getcwd() to this
        print(rootDir)
    else:
        rootDir = os.getcwd()
        print(".")

    # Track the number of directories and files
    numDirs = 0
    numFiles = 0

    # Initial indentation string
    line = ""

    # Call recursive function for outputting subtrees
    output_subtree(sorted(os.listdir(rootDir)), rootDir, 1, 0, line)

    # Output num of directories and files
    print("\n" + str(numDirs) + " directory, " if numDirs == 1 else "\n" + str(numDirs) + " directories, ", end="")
    print(str(numFiles) + " file, " if numFiles == 1 else str(numFiles) + " files")
