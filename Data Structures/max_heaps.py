"""
Max Heap

Complete binary tree

Every node is > or = its parent

            25
          /    \
        16      24
       /   \   /
      5    11 19

Biggest number is always at the top and readily to be removed

Remove Max in O(log n)

Easy to implement using a Python list

- in a list, there is an index assigned to each node

 1  2  3  4  5  6
25 16 24  5 11 19

Accessing "5"

index = 4

Access parent index of "5"

parent(index) = index/2 = 2

left(index) = index * 2 = 8 [doesn't exist in current example]
right(index) = index * 2 + 1 = 9 [also doesn't exist]

"""


"""
MaxHeap Operations

- Push(insert)
- Peek(get max)
- Pop(remove max)


Push - Add value to end of array (list), float it up to proper position

Peek - Return the value at Heap[1]

Pop - Move max to end of array, delete it, bubble down the item at index 1 to
its proper position, return max


"""


"""
Python MaxHeap
"""

class MaxHeap(object):
    """
    A MaxHeap always bubbles the highest value to the top, so it can be removed
    instantly.

    Public functions: push, pop, peek
    Private functions: swap, floatup, bubbledown, str
    """

    def __init__(self, items = []):
        super().__init__()
        self.heap = 0
        for item in items:
            self.append(item)
            self.__float_up(len(self.heap) - 1)

    def push(self, data):
        self.heap.append(data)
        self.__float_up(len(self.heap) - 1)

    def peek(self):
        if self.heap[1]:
            return self.heap[1]
        else:
            return False

    def pop(self):
        if len(self.heap) > 2:
            self.__swap(1, len(self.heap) - 1)
            max = self.heap.pop()
            self.__bubble_down(1)
        elif len(self.heap) == 2:
            max = self.heap.pop()
        else:
            max = False

    def __swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def __float_up(self, index):
        parent = index // 2
        if index <= 1:
            return
        elif self.heap[index] > self.heap[parent]:
            self.__swap(index, parent)
            self.__float_up(parent)

    def __bubble_down(self, index):
        left = index * 2
        right = index * 2 + 1

        largest = index

        if len(self.heap) > left and self.heap[largest] < self.heap[left]:
            largest = left

        if len(self.heap) > right and self.heap[largest] < self.heap[right]:
            largest = right

        if largest != index:
            self.__swap(index, largest)
            self.__bubble_down(largest)

    def __str(self):
        return str(self.heap)
