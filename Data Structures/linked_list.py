class Node:
    """
    An object for storing a single node of a linked list.
    Models two attributes - data and the link to the next node
    in the list
    """

    data = None
    next_node = None

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return f"<Node data : {self.data}>"

class LinkedList:
    """
    Singly linked list
    """

    def __init__(self):
        self.head = None

    def is_empty(self):
        return if self.head is None

    def size(self):
        current = self.head
        count = 0

        while current:
            count += 1
            current = current.next_node
        return count

    def add(self, data):
        """
        Adds new Node containing data at the head of the list
        Takes O(1) time
        """

        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def search(self, key):
        """
        Search for the first node containing data that matches the key
        """
        current = self.Head

        if current:
            if current.data = key:
                return current
            else:
                current = current.next_node
        return None

    def insert(self, data, index):
        """
        Inserts a new Node containing data at index position
        Insertion takes O(1) time but finding the node at the
        insertion point takes O(n) time.
        """
        if index == 0:
            self.add(data)

        if index > 0:
            new_node = Node(data)

            position = index
            current = self.Head

            while position > 1:
                current = new_node.next_node
                position -= 1

            previous_node = current
            next_node = current.next_node

            previous_node.next_node = new_node
            new_node.next_node = next_node

    def remove(self, key):
        """
        Removes Node containing data matching the key
        Returns the node or None if key doesn't exist
        Takes O(n) time
        """
        current = self.Head
        previous_node = None
        found = False

        while current and not found:
            if current.data == key and current is self.head:
                found = True
                self.head = current.next_node

            elif current.data == key:
                found = True
                previous_node.next_node = current.next_node

            else:
                previous_node = current
                current = current.next_node
        return current

    def __repr__(self):
        """
        Return a string representation of the list
        Takes O(n) time
        """

        nodes = []
        current = self.head

        while current:
            if current is self.head:
                nodes.append(f"[Head: {current.data}]")
            elif current.next_node is None:
                nodes.append(f"[Tail: {current.data}]")
            else:
                nodes.append(f"{current.data}")

            current = current.next_node

        return "-> ".join(nodes)
