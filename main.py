#!/usr/bin/python3
import argparse
import sys
import os
VERSION=1.0

def getSmallerSize(lenFile1,lenFile2):
    if (lenFile1 < lenFile2):
        return lenFile1
    else:
        return lenFile2

def xor(binaryFile1,binaryFile2):
    lenFile1 = len(binaryFile1)
    lenFile2 = len(binaryFile2)
    size = getSmallerSize(lenFile1,lenFile2)
    xord_byte_array = bytearray(size)
    for i in range(size):
        xord_byte_array[i] = binaryFile1[i] ^ binaryFile2[i]
    return xord_byte_array

def writeOutput(binaryOutput,outputNameFile):
    filename = "output"
    if outputNameFile != None:
        filename = outputNameFile
    open(filename, 'wb').write(binaryOutput)

def getOptions():
    parser = argparse.ArgumentParser(add_help=True, formatter_class=argparse.RawTextHelpFormatter,
                                     description=
    """
    Simple xor.                     
    This CLI tool allows you to create a file as the output of a XOR between a file and another..
    Example of minimal command: ./main.py -f1 path/to/first/file -f2 path/to/second/file
    Example of recommended command: ./main.py -f1 path/to/first/file -f2 path/to/second/file -o name/of/the/new/file
    """,
    epilog=
    """
    Created by Prantice with love <3
    Credits to megabeet for the original script : https://www.megabeets.net/xor-files-python/
    """,
    )
    parser.version = "The current version is {}".format(VERSION)
    parser.add_argument('-f1', "--file1", required=True,help="""Absolute path to the first file (Mandatory)""", )
    parser.add_argument('-f2', "--file2", required=True,help="""Absolute path to the second file  (Mandatory)""", )
    parser.add_argument('-o', "--output", required=False,help="""Rename the output file (Default name is output) (Optionnal)""", )
    parser.add_argument('-v', '--version', action='version', help='print the version and exit')

    args = vars(parser.parse_args())
    return args

if __name__ == '__main__':
    args = getOptions()
    binaryFile1 = bytearray(open(args["file1"], 'rb').read())
    binaryFile2 = bytearray(open(args["file2"], 'rb').read())
    output = xor(binaryFile1,binaryFile2)
    writeOutput(output,args["output"])
    exit(0)






