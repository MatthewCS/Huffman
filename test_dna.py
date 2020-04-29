from huffman import huffman

input = "AGGAGGTACTAGATGGCGGATGAGATAACGTAAAA"
tree = huffman(input)
tree.encode(input)
byte_len = int(len(tree.encoded_data) / 8 + 0.5)
space_saved = int(100 - len(tree.encoded_data) / (8 * len(input)) * 100)

print("INPUT:   " + input)
print("Original length, in bytes: " + str(len(input)))
print("Original length, in bits:  " + str(8 * len(input)))
print()
print("ENCODED: " + tree.encoded_data)
print("Encoded length, in bytes: ~" + str(byte_len))
print("Encoded length, in bits:   " + str(len(tree.encoded_data)))
print()
print("Space saved: {0}%".format(space_saved))
