import hashlib
import datetime

def calc_hash(self):
      sha = hashlib.sha256()
      hash_str = "We are going to encode this string of data!".encode('utf-8')
      sha.update(hash_str)
      return sha.hexdigest()

class Block:
    def __init__(self, timestamp, data, previous_hash):
      self.timestamp = timestamp
      self.data = data
      self.previous_hash = previous_hash
      self.hash = self.calc_hash()


    def calc_hash(self):
    	sha = hashlib.sha256()
    	hash_str = (str(self.data).encode('utf-8') +
    				str(self.previous_hash).encode('utf-8') +
    				str(self.timestamp).encode('utf-8'))
    	sha.update(hash_str)
    	return sha.hexdigest()
	
    def __str__(self):
    	return "\nBlockhash: {}\nTimestamp: {}\nData: {}\nPrevious Hash: {}\n".format(self.hash, self.timestamp, self.data, self.previous_hash)


class Node(object):
	def __init__(self, data, previous_hash):
		self.block = Block(datetime.datetime.utcnow(), data, previous_hash)
		self.next = None
		self.tail = None


class BlockChain(object):
	def __init__(self):
		self.head = None
		self.tail = None

	def add_block(self, data=None):
		if data == None:
			print("Empty block cannot be stored!")
			return
		if not self.head:
			self.head = Node(data, None)
			self.tail = self.head
		else:
			self.tail.next = Node(data, self.tail.block.hash)
			self.tail = self.tail.next

	def __str__(self):
		if self.head == None:
			return "Empty blockchain"
		current_node = self.head
		output = ""
		while current_node:
			output += str(current_node.block)
			current_node = current_node.next
		return output


# Test cases:
block_chain = BlockChain()
block_chain.add_block("One block")
block_chain.add_block("Two block")
block_chain.add_block("Three block")


current_block = block_chain.head
print(block_chain)
# Expected output: prints the 3 block

print(current_block.block)
# Outputs the first block data

current_block = current_block.next
print(current_block.block)
# Outputs the second block data


print('\n_____________________________\n')
block_chain = BlockChain()

print(block_chain)
# Expected output: Blockchain is empty


print('\n_____________________________\n')
block_chain = BlockChain()

block_chain.add_block()
block_chain.add_block("This block only")
block_chain.add_block()

print(block_chain)
# Expected output: prints 1 block only