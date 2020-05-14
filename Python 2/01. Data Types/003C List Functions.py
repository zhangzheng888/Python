"""
Data Type: Lists

List Functions (Python 2.7)

Delete or Remove Elements in Lists

Using the keyword del, one or more items from a list can be removed, even the list itself
"""

# Deleting list items
example_del_list = ['p', 'r', 'o', 'b', 'l', 'e', 'm']

# delete one item
del example_del_list[2]

print example_del_list

# delete multiple items
del example_del_list[1:5]

print example_del_list

# delete entire list
del example_del_list

# Error: List not defined
print example_del_list

"""
remove() method to remove the given item

pop() method to remove an item at the given index

The pop() method removes and returns the last item if index is not provided. This helps us
implement lists as stacks (first in, last out data structure).

The clear() method works to empty a list.
"""

my_examples_list = ['p','r','o','b','l','e','m']
my_examples_list.remove('p')

# Output: ['r', 'o', 'b', 'l', 'e', 'm']
print my_examples_list

# Output: 'o'
print my_examples_list.pop(1)

# Output: ['r', 'b', 'l', 'e', 'm']
print my_examples_list

# Output: 'm'
print my_examples_list.pop()

# Output: ['r', 'b', 'l', 'e']
print my_examples_list

my_examples_list.clear()

# Output: []
print my_examples_list

"""
Here are some other functions which is part of the list module:

append() - Add an element to the end of the list
extend() - Add all elements of a list to the another list
insert() - Insert an item at the defined index
remove() - Removes an item from the list
pop() - Removes and returns an element at the given index
clear() - Removes all items from the list
index() - Returns the index of the first matched item
count() - Returns the count of number of items passed as an argument
sort() - Sort items in a list in ascending order
reverse() - Reverse the order of items in the list
copy() - Returns a shallow copy of the list

"""

# Python list methods
example_list = [3, 8, 1, 6, 0, 8, 4]

# Output: 1
print example_list.index(8)

# Output: 2
print example_list.count(8)

example_list.sort()

# Output: [0, 1, 3, 4, 6, 8, 8]
print example_list

example_list.reverse()

# Output: [8, 8, 6, 4, 3, 1, 0]
print example_list

"""
List Membership

The keyword in checks if an item exists in a list or not
"""

my_check_list = ['t', 'a, 'c', 'o', 'm', 'a']

# Output: True
print 'p' in my_check_list

# Output: False
print 'a' in my_check_list

# Output: True
print 'c' not in my_check_list

"""
Iterating Through a List
Using a for loop we can iterate through each item in a list.
"""

for fruit in ['apple','banana','mango']:
    print "I like", fruit
