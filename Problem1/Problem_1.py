"""
This problem built upon my prior interaction with algoexpert.io/LRUCacheProblem;
"""
class LRU_Cache:
	def __init__(self, max_size):
		self.cache = {}
		self.max_size = max_size or 5  # As problem's set size;
		self.current_size = 0
		self.list_of_most_recent = DoublyLinkedList()

	def set(self, key, value):
		if key not in self.cache:
			if self.current_size == self.max_size:
				self.evict_least_recent()
			else:
				self.current_size += 1
			self.cache[key] = DoublyLinkedListNode(key, value)
		else:
			self.replace_key(key, value)
		self.update_most_recent(self.cache[key])

	def get(self, key):
		if key not in self.cache:
				return -1
		self.update_most_recent(self.cache[key])
		return self.cache[key].value

	def get_most_recent_key(self):
		if self.list_of_most_recent.head is None:
			return None
		return self.list_of_most_recent.head.key
		
	def evict_least_recent(self):
		key_to_remove = self.list_of_most_recent.tail.key
		self.list_of_most_recent.remove_tail()
		del self.cache[key_to_remove]

	def update_most_recent(self, node):
		self.list_of_most_recent.set_head_to(node)

	def replace_key(self, key, value):
		if key not in self.cache:
			raise Exception("The key is not in the cache!")
		self.cache[key].value = value

	def __repr__(self):
		slot = ''
		for key in self.cache:
			slot += '(Key: ' + str(key) + ', ' + 'Value: ' + str(self.cache[key].value) + ') '
		return slot	


class DoublyLinkedList:
	def __init__(self):
		self.head = None
		self.tail = None

	def set_head_to(self, node):
		if self.head == node:
			return
		elif self.head is None:
			self.head = node
			self.tail = node
		elif self.head == self.tail:
			self.tail.prev = node
			self.head = node
			self.head.next = self.tail
		else:
			if self.tail == node:
				self.remove_tail()
			node.remove_bindings()
			self.head.prev = node
			node.next = self.head
			self.head = node

	def remove_tail(self):
		if self.tail is None:
			return
		if self.tail == self.head:
			self.head = None
			self.tail = None
			return
		self.tail = self.tail.prev
		self.tail.next = None


class DoublyLinkedListNode:
	def __init__(self, key, value):
		self.key = key
		self.value = value
		self.prev = None
		self.next = None

	def remove_bindings(self):
		if self.prev is not None:
			self.prev.next = self.next
		if self.next is not None:
			self.next.prev = self.prev
		self.prev = None
		self.next = None


# Testing;
our_cache = LRU_Cache(5)
print("our_cache has (key : value) pairs of: ", our_cache, '\n') # 5 spots allocated;
# Fill it up & print it;
our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);
print("our_cache has (key : value) pairs of: ", our_cache, '\n') 
# Get some values, and they are tagged as Recently Used; thus not for eviction
# cache hit;
our_cache.get(1)       # returns 1
our_cache.get(2)       # returns 2
# cache miss; as its not present
our_cache.get(9)       # returns -1 because 9 is not present in the cache
print("our_cache has (key : value) pairs of: ", our_cache, '\n')

our_cache.set(5, 5) # will replace the `key:3 value:3`; as Least Recently Used pair;
print("our_cache has (key : value) pairs of: ", our_cache, '\n')


our_cache.set(6, 6) # will replace the `key:4 value:4`; as Least Recently Used pair;
# `(Key: 1 Value: 1) (Key: 2 Value: 2)` - were Recently Used with get();
print("our_cache has (key : value) pairs of: ", our_cache, '\n')


our_cache.get(3)

# Other cases;
# 1st verify the "return 1, 2, -1";
print(our_cache.get(1)) # True;
print(our_cache.get(2)) # True;
print(our_cache.get(9)) # True;

# 2nd check of replacement;
our_cache_test = LRU_Cache(2)
our_cache_test.set(1, 1);
print("our_cache has (key : value) pairs of: ", our_cache_test, '\n') 
our_cache_test.set(2, 2);
print("our_cache has (key : value) pairs of: ", our_cache_test, '\n') 
our_cache_test.set(3, 3); # evicts 1; adds 3
print("our_cache has (key : value) pairs of: ", our_cache_test, '\n') 
our_cache_test.set(4, 4); # evicts 2; adds 4
print("our_cache has (key : value) pairs of: ", our_cache_test, '\n') 
our_cache_test.set(5, 5); # evicts 3; adds 5
print("our_cache has (key : value) pairs of: ", our_cache_test, '\n') 
our_cache_test.set(6, 6); # evicts 4; adds 6
print("our_cache has (key : value) pairs of: ", our_cache_test, '\n') 