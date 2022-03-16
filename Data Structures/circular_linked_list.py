"""
Circular Linked Lists

Advantage over singly Linked List
- Ideal for modeling continuous looping objects such as Monopoly board
or race track.


"""

class CircularLinkedList:
    """
    Attributes
    - root
    - size

    Methods
    - add
    - find
    - remove
    - print
    """

    def __init__(self, r = None):
        self.root = r
        self.size = 0

    def add(self, d):
        if self.size == 0:
            self.root = Node(d)
            self.root.next_node = self.root
        else:
            new_node = Node(d)
            self.root.next_node = new_node
        self.size += 1

    def find(self, d):
        this_node = self.root
        while True:
            if this_node.data == d:
                return d
            elif this_node.next_node == self.root:
                return False
            this_node = this_node.next_node

    def remove(self, d):
        this_node = self.root
        prev_node = None

        while True:
            if this_node.data == d:
                if prev_node is not None:
                    prev_node.next_node = this_node.next_node
                else:
                    while this_node.next_node != self.root:
                        this_node = this_node.next_node
                    this_node.next_node = self.root.next_node
                    self.root = self.root.next_node
                self.size -= 1
                return True
            elif this_node.next_node == self.root:
                return False
            prev_node = this_node
            this_node = this_node.next_node

    def __repr__(self):
        if self.root is None:
            return
        this_node = self.root
        print(this_node, end="->")
        while this_node.next_node != self.root:
            this_node = this_node.next_node
            print(this_node, end="->")
        print()
