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

def union(llist_1, llist_2):
    """ 
    Input A.set OR B.set that is LL;
    union_set = AuB -> Is in A.set OR B.set;
    - with no duplicates;
    """
    # Is in A.set & B.set, with no duplicates;
    union_set = set() # new set that contains all of the elements that are in A.set OR B.set;
    final_union_set = LinkedList()

    p = llist_1.head
    while p: # O(n) - traversing whole LList
        if p.value not in union_set:
            union_set.add(p.value)
            final_union_set.append(p)
        p = p.next

    p = llist_2.head
    while p: # O(n) - traversing whole LList
        if p.value not in union_set:
            union_set.add(p.value) 
            final_union_set.append(p)
        p = p.next

    return final_union_set


def intersection(llist_1, llist_2):
    """ 
    Input A.set & B.set that is LL;
    intersection_set = AnB -> Is in A.set & B.set; 
    - with no duplicates;
    """
    intersection_set = set() # new set that contains all of the elements that are in A.set AND B.set (both sets);
    final_intersection_set = LinkedList()

    p = llist_1.head
    while p:
        if p.value not in intersection_set:
            intersection_set.add(p.value)
        p = p.next

    p = llist_2.head
    while p:
        if p.value in intersection_set:
            intersection_set.remove(p.value)
            final_intersection_set.append(p)
        p = p.next

    return final_intersection_set


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
# expected return: 3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 21 -> 32 -> 9 -> 1 -> 11

print (intersection(linked_list_1,linked_list_2)) 
# expected return: 4 -> 21 -> 6 

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
# expected return: 3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 23 -> 1 -> 7 -> 8 -> 9 -> 11 -> 21
print (intersection(linked_list_3,linked_list_4))
# expected return: [] as None of elements is in A and B;

# Test case 3

linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = []

for i in element_1:
    linked_list_5.append(i)

for i in element_2:
    linked_list_6.append(i)

print (union(linked_list_5,linked_list_6))
# expected return: AuB = llist1
print (intersection(linked_list_5,linked_list_6))
# expected return: [] as None of elements is in A and B;