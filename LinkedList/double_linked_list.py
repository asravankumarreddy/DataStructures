# 1. Create a Linked List
# 2. Create a Node
#


class ListNode:
    def __int__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None


class MyLinkedList:

    # Initialize Linked List
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    # Get the value on Index-th Node in Linked List, If index is invalid, return -1
    def get(self, index: int) -> int:

        # If Index is less than 0 and more than linked list size, return Negative
        if index < 0 and index >= self.size:
            return -1

        # assign the head to curr variable
        cur = self.head

        # ex: Get the value of index =2, iterate the index till it reaches 2nd index
        # Assign the next values to current value.
        # Initial cur value = 0 index(head), index =1 -> cur.next -> cur.value
        while index != 0:
            cur = cur.next
            index = index - 1

        return cur.value

    # Add a Node of value before the first element of Linked List
    def add_at_head(self, value: int) -> None:
        new_node = ListNode(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head  # New Node Next value is current head value
            self.head.prev = new_node  # current head node previous value is New Node
            self.head = new_node  # new node will become current head
        self.size = self.size + 1

    # Append a Node of value at the end of Linked List
    def add_at_tail(self, value: int) -> None:
        new_node = ListNode(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail  # New node previous value should be current thread
            self.tail.next = new_node  # tail next value should be new node
            self.tail = new_node  # new node will become tail
        self.size += 1

    # add the value at the mentioned index
    def add_at_index(self, index: int, value: int) -> None:

        if 0 < index > self.size:
            return -1
        elif index == 0:
            self.add_at_tail(value)
        elif index == self.size:
            self.add_at_tail(value)
        else:
            cur = self.head
            while index-1 != 0:
                cur = cur.next
                index -= 1
            new_node = ListNode(value)

            # **** Update Order : first: New_node.next, last: New_node.prev
            # 1 & 2. new node.next & cur.next.prev (Two way connection)
            # 3 & 4. current.next & new_node_prev (Two way connection)

            new_node.next = cur.next    # New node next value should be same as current next
            cur.next.prev = new_node    # new node next prev value should have new node
            cur.next = new_node         # current next value should be new Node
            new_node.prev = cur         # new node prev should be current value
            self.size +=1

    # Delete the index-th node of a value, if the index is valid
    def del_at_index(self, index: int) -> None:
        if 0 < index >= self.size:
            return -1
        elif index == 0:            # remove head
            cur = self.head.next    # Assign second value(head.next) to Cur
            if cur:                 # Check the cur is valid
                cur.prev = None     # Remove the prev from previous head
            self.head = self.head.next  # make the head.next as head
            self.size -= 1
            if self.size == 0:
                self.head = None
        elif index == self.size-1:  # Remove tail
            cur = self.tail.prev    # Assign tail.prev to cur
            if cur:                 # check the value is valid or not
                cur.next = None     # tail.next should be None. So, cur.next is None
            self.tail = self.tail.prev  # tail.prev should be tail now
            self.size -= 1
            if self.size == 0:
                self.head = None
        else:
            while index-1 != 0:          # Reach the before index values
                cur = cur.next          # Exit once the cur reached the location of index
                index -= 1
            cur.next = cur.next.next    # cur.next should be removed. So, cur.next will cur.next.next
            cur.next.prev = cur         # cur.next.prev is previously cur.next.next.prev and it should hold cur value
            self.size -= 1





