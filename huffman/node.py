class Node(object):

    value = ""
    frequency = -1
    encoded = ""
    left_node = None
    right_node = None


    def __init__(self, val, freq):

        self.value = val
        self.frequency = freq


    # Using recursion, create a list of values based on this node
    #     and all its children.
    def get_values(self, values=[]):

        if self.left_node:
            self.left_node.get_values(values=values)
        if self.right_node:
            self.right_node.get_values(values=values)

        if self.value:
            values.append([self.value,  self.frequency, self.encoded])

        return values

    # Using a list of values from get_values, create a dictionary
    #     mapping our original value to our encoded value.
    def get_dict(self):

        d = dict()

        for v in self.get_values():
            d[v[0]] = v[2]

        return d


    # Traverse this node and all of its children. We want to find
    #     the encoding for every value in the tree by traversing
    #     it here. This function should always be called before
    #     get_values or get_dict.
    def traverse(self, bits=""):

        if self.value:
            self.encoded = bits
            # print("value: " + self.value)
            # print("encoded: " + self.encoded)

        if self.left_node:
            self.left_node.traverse(bits=bits+"0")

        if self.right_node:
            self.right_node.traverse(bits=bits+"1")


    def __str__(self):

        return "{0}\t : \t{1}".format(self.value, self.frequency)


class HeadNode(Node):

    encoded_data = ""
    data = dict()


    def __init__(self, node):

        super().__init__(node.value, node.frequency)

        self.encoded = node.encoded
        self.left_node = node.left_node
        self.right_node = node.right_node

        self.traverse()


    # Given some input string, use our encoding (self.data) to
    #     transform that string and encode it.
    def encode(self, string):

        self.encoded_data = ""

        for c in string:
            self.encoded_data += self.data[c]
