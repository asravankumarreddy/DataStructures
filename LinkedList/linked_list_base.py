import time
from time import perf_counter

class Node:
    def __int__(self, value= None, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

class LinkedList:
    def __int__(self):
        self.head = None

    def insert(self):   # Create a node
        pass

    def delete(self):   # Delete a node
        pass

# Create a Linked List object
LL = LinkedList

# Create a first node with 3 assigned to head
n1 = Node(3)        #Creating node values
n3 = Node(4)
n2 = Node(7)

LL.head = n1
n1.next = n2    #N1 next value is N2

# assign the N2 node head to N1 Next
n2.next = n3    #n2.next --> n3
n2.prev = n1    #N2 prev value is N1

# assign the N3 node to N2 Next
n3.prev = n2    #n2 <-- n3.prev. n3 Next --> None





