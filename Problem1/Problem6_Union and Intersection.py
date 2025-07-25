class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

    def duplicate(self):
        copy = LinkedList()
        current = self.head
        while current:
            node = Node(current.value)
            copy.append(node)
            current = current.next
        return copy


def remove_duplicates(llist):
    current1 = llist.head
    while current1:
        current2 = current1.next
        data = current1.value
        while current2:
            temp = current2
            current2 = current2.next
            if temp.value == data:
                llist.remove(temp)
        current1 = current1.next

def union(llist_1, llist_2):
    if llist_1.head is None:
        union = llist_2.duplicate()
        remove_duplicates(union)
        return union

    if llist_2.head is None:
        union = llist_1.duplicate()
        remove_duplicates(union)

    union = llist_1.duplicate()
    last_node = union.head
    while last_node.next is not None:
        last_node = last_node.next
    llist_2_copy = llist_2.duplicate()
    last_node.next = llist_2_copy.head
    remove_duplicates(union)
 
    return union


def intersection(llist_1, llist_2):
    if (llist_1.head is None or llist_2.head is None):
        return LinkedList()
 
    intersection = LinkedList()
    current1 = llist_1.head
    while current1:
        current2 = llist_2.head
        data = current1.value
        while current2:
            if current2.value == data:
                node = Node(data)
                intersection.append(node)
                break
            current2 = current2.next
        current1 = current1.next
    remove_duplicates(intersection)
 
    return intersection


# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
print (intersection(linked_list_1,linked_list_2))

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
print (intersection(linked_list_3,linked_list_4))