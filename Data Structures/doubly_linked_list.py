class Node:
    """
    An object for storing a single node of a linked list.
    Models two attributes - data and the link to the next node
    in the list
    """

    def __init__(self, data, next_node = None, prev_node = None):
        self.data = data
        self.next_node = next_node
        self.prev_node = prev_node

    def __repr__(self):
        return f"<Node data : {self.data}>"

class DoublyLinkedList:
    """
    Doubly Linked List object has 3 attributes:
    root node that defaults to None
    tail node that also defaults to None
    size that defaults to 0

    Attributes:
    Root - pointer to the beginning of the list
    Tail - pointer to the end of the list
    Size - number of nodes in the list

    Operations:
    find(data) - Iterates through the nodes until it finds the data passed in.
    If the data is found, return the data, else return None

    add(data) - Receives piece of data, creates a new Node, setting the new Node
    as the root and increment size

    remove(data) - Needs pointers to this_node and prev_node. If it finds the
    data, needs to check if it is in the root_node before deciding how to bypass
    the deleted node

    repr or print - Iterates the list and prints the nodes


    """

    def __init__(self, root = None, tail = None):
        self.root = root
        self.tail = tail
        self.size = 0

    def add(self, data):
        new_node = Node(data, next_node = self.root, prev_node = None)
        if self.root is not None:
            self.root.prev_node = new_node
        
        self.root = new_node
        self.size += 1


    def find(self, data):
        this_node = self.root

        while this_node is not None:
            if this_node.data == data:
                return data
            else:
                this_node = this_node.next_node
        return None

    def remove(self, data):
        this_node = self.root
        prev_node = None

        while this_node is not None:
            if this_node.data == data:
                if prev_node is not None:
                    prev_node.next_node = this_node.next_node
                else:
                    self.root = this_node.next_node
                self.size -= 1
            else:
                prev_node = this_node
                this_node = this_node.next_node
        return False

    def __repr__(self):
        this_node = self.root

        while this_node is not None:
            print(this_node, end = ' -> ')
            this_node = this_node.next_node

        print('None')
