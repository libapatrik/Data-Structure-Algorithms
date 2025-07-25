import sys


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None


class Tree:
    def __init__(self, root):
        self.root = root


def huffman_encoding(data):
    # if data is missing;
    if data is None or data == '':
        print('Invalid data...')
        return None



def huffman_decoding(data, tree):
    pass




''' Helper functions '''
    # for character : frequency use dictionary;
def get_frequency(data):    
    frequency = {}
    for character in data:
        if character in frequency:
            frequency[character] += 1
        else:
            frequency[character] = 1

    freq = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
    return freq

"""
if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))
    """