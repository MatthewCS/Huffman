from bitarray import  bitarray
from huffman import huffman
import json
import sys


def encode(input_filepath):

    with open(input_filepath, "r") as inf:

        raw_data = inf.read()

        tree = huffman(raw_data)
        tree.encode(raw_data)
        return tree


def write(output_filepath, tree):

    with open(output_path+".data", "wb") as outf:

        bitarray(tree.encoded_data).tofile(outf)

    with open(output_path+".keys", "w") as outf:

        json.dump(tree.data, outf)


if __name__ == "__main__":

    if len(sys.argv) < 3:

        print("Too few arguments given!")
        print("Please format your command like this:")
        print("    python encode_file.py <Path to input> <Path to output>")
        print()
        print("In the output path, please do not specify a file extension.")
        print("This program will create two output files:")
        print("    <OUTPUT>.data")
        print("    <OUTPUT>.keys")
        print("Both of these files are necessary to decompress our data.")
        exit()


    input_path = sys.argv[1]
    output_path = sys.argv[2]

    print("Encoding {0}...".format(input_path))

    try:
        tree = encode(input_path)
    except FileNotFoundError as fnf:
        print("ERROR: File {0} not found!".format(input_path))

    print("Writing data to {0}.data & {0}.keys...".format(output_path))
    write(output_path, tree)
