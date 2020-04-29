from bitarray import bitarray
from huffman import decode
import json
import sys


def write(output_filepath, string):

    with open(output_filepath, "w") as outf:

        outf.write(string)


def read(input_filepath):

    with open(input_filepath+".data", "rb") as inf:

        a = bitarray()
        a.fromfile(inf)
        string = a.to01()

    with open(input_filepath+".keys", "r") as inf:

        data = json.load(inf)

    return string, data


if __name__ == "__main__":

    if len(sys.argv) < 3:

        print("Too few arguments given!")
        print("Please format your command like this:")
        print("    python encode_file.py <Path to input> <Path to output>")
        print()
        print("In the output path, please do not specify a file extension.")
        print("This program will create two input files:")
        print("    <INPUT>.data")
        print("    <INPUT>.keys")
        print("Both of these files are necessary to decompress our data.")
        exit()


    input_path = sys.argv[1]
    output_path = sys.argv[2]
    bin_string = ""
    data = dict()

    print("Reading {0}.data & {0}.keys...".format(input_path))

    try:
        bin_string, data = read(input_path)
    except FileNotFoundError as fnf:
        print("ERROR: File {0} not found!".format(input_path))

    print("Decoding the file...")
    decoded = decode(bin_string, data)

    print("Writing out to {0}...".format(output_path))
    write(output_path, decoded)
