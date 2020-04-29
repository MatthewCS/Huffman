import copy
from .node import *

# Calculate the frequency of characters in a given input
def frequency(input):

    # create a dictionary
    freq = dict()

    # then, calculate the frequency of each character
    for character in input:
        if character in freq:
            freq[character] += 1
        else:
            freq[character] = 1

    return freq


# Sort the frequencies out, from least frequent to most frequent
def priority_queue(freq):

    # convert our dictionary to a list
    queue = [item for item in freq.items()]
    # sort our list by frequency
    # NOTE: to do this, we just need to sort our queue by the second
    #       item in each entry of our queue
    queue.sort(key = lambda e: e[1])
    return queue


# From a given priority queue of frequencies, create a priority
#     queue of nodes.
def queue_to_nodes(queue):

    # Empty list of nodes
    nodes = []
    for item in queue:
        nodes.append(Node(item[0], item[1]))

    return nodes


# From a list of nodes, generate a binary tree of nodes based
#     on frequency. Return the head node.
def build_tree(nodes, verbose=False):

    while len(nodes) > 1:

        if verbose:
            print("===== NODES LIST =====")
            for n in nodes:
                print(n)


        # Create a nwe node.
        #
        # Remove the two smallest nodes from our list. They will
        #     be the branches from the node we create.
        #
        # We also want our new node to be given a frequency equal
        #     to the sum of our branches.
        #
        # Afterwards, we append our new node to the list of nodes.
        left_node = nodes.pop(0)
        right_node = nodes.pop(0)
        freq = left_node.frequency + right_node.frequency

        new_node = Node("", freq)
        new_node.left_node = left_node
        new_node.right_node = right_node

        # Insert our frequency into our list of nodes, but
        #     maintain order!
        insert_index = 0
        while (len(nodes) > insert_index
               and nodes[insert_index].frequency < freq):

            insert_index += 1

        if insert_index == len(nodes):
            nodes.append(new_node)
        else:
            nodes.insert(insert_index, new_node)

    # The only node left will be the head of our tree.
    return HeadNode(nodes[0])


def huffman(input):

    f = frequency(input)
    q = priority_queue(f)
    n = queue_to_nodes(q)
    t = build_tree(n)
    return t


def decode(string, data):

    index = 0
    output = ""
    length = len(string)

    while index < length:

        current_char = ""

        for key, val in data.items():

            if string.startswith(val, index):
                current_char = key

        output += current_char
        index += len(data[current_char])

    return output
