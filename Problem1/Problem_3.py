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

# Encoding:
def insert_to_list(node, sorted_frequencies):
	for index, element in enumerate(sorted_frequencies):
		if node.value < element.value:
			sorted_frequencies.insert(index, node)
			break
		elif index == len(sorted_frequencies) - 1:
			sorted_frequencies.append(node)
			break


def encode(root, string, characters):
	if root.left is None and root.right is None:
		characters[root.key] = string
	else:
		if root.left is not None:
			encode(root.left, string + "0", characters)
		if root.right is not None:
			encode(root.right, string + "1", characters)


def huffman_encoding(data):
    if data is None or data == '':
        return data, None

    else:
    	frequencies = get_char_frequency(data) # count
    	sorted_frequencies = sort_frequency(frequencies) # sort
    	map_frequency = list(map(lambda x: Node(x[0], x[1]), sorted_frequencies))
    	tree = None

    	while len(map_frequency) > 1:
    		first_element = map_frequency.pop(0)
    		second_element = map_frequency.pop(0)
    		root_node = Node(first_element.value + second_element.value, 
    						first_element.value + second_element.value)
    		root_node.left = first_element
    		root_node.right = second_element
    		insert_to_list(root_node, map_frequency)
    		if len(map_frequency) == 0:
    			tree = Tree(root_node)
    	if tree is None:
    		if len(map_frequency) == 1:
    			first_element = map_frequency.pop(0)
    			tree = Tree(Node(first_element.value, first_element.value))
    			tree.root.left = Node(first_element.key, first_element.value)

    	characters_encoded = {}
    	encode(tree.root, "", characters_encoded)
    	string_encoded = ""
    	for char in data:
    		string_encoded += characters_encoded[char]
    	return string_encoded, tree


# Decoding:
def decode(data, root, index, string_to_decode):
    	if root.left is None and root.right is None:
    		string_to_decode += root.key
    		return index, string_to_decode
    	elif data[index] == "0":
    		return decode(data, root.left, index + 1, string_to_decode)
    	else: 
    		return decode(data, root.right, index + 1, string_to_decode)


def huffman_decoding(data, root): # changed param from tree to root;
    if root is None:
    	return data
    
    index = 0
    string_to_decode = ""
    while index <= len(data) - 1:
    	index, string_to_decode = decode(data, root, index, string_to_decode)
    return string_to_decode



''' Helper functions '''
def get_char_frequency(data):    
    frequency = {}
    for char in data:
        frequency[char] = frequency.get(char, 0) + 1
    return frequency


def sort_frequency(data):
	items = list(data.items())
	items.sort(key=lambda x: x[1])
	return items


if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree.root) # changed the tree -> tree.root;

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))


    one_word = "Bird"

    print("The size of the one_word data is: {}\n".format(sys.getsizeof(one_word)))
    print("The content of the one_word data is: {}\n".format(one_word))

    encoded_data, tree = huffman_encoding(one_word)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree.root)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print("The content of the decoded data is: {}\n".format(decoded_data))


    empty_string = ""

    print("The size of the empty_string is: {}\n".format(sys.getsizeof(empty_string)))
    print("The content of the empty_string is: {}\n".format(empty_string))

    encoded_data, tree = huffman_encoding(empty_string) # expected return None;