# Python Data Structures

This repository contains implementations of various basic data structures in Python, including **Stack**, **Queue**, **Linked List**, **Binary Search Tree (BST)**, **Graph**, and **Heap**. These data structures are essential building blocks in computer science and are widely used in algorithms and applications.

## Data Structures Implemented

### 1. Stack
A **stack** is a linear data structure that follows the **Last In, First Out (LIFO)** principle. The operations supported are:
- `push(item)`: Add an item to the top of the stack.
- `pop()`: Remove and return the top item.
- `peek()`: View the top item without removing it.
- `is_empty()`: Check if the stack is empty.
- `size()`: Get the size of the stack.

**[Code](data-structures/stack.py)**

### 2. Queue
A **queue** is a linear data structure that follows the **First In, First Out (FIFO)** principle. The operations supported are:
- `enqueue(item)`: Add an item to the end of the queue.
- `dequeue()`: Remove and return the front item.
- `peek()`: View the front item without removing it.
- `is_empty()`: Check if the queue is empty.
- `size()`: Get the size of the queue.

**[Code](data-structures/queue.py)**

### 3. Linked List
A **linked list** is a linear data structure consisting of nodes where each node contains data and a reference to the next node in the sequence. The operations supported are:
- `append(data)`: Add a new node at the end.
- `display()`: Display the entire linked list.

**[Code](data-structures/linked_list.py)**

### 4. Binary Search Tree (BST)
A **binary search tree (BST)** is a binary tree in which the value of each node is greater than the values of all the nodes in its left subtree and smaller than the values of all the nodes in its right subtree. The operations supported are:
- `insert(key)`: Insert a key into the BST.
- `inorder()`: Perform an inorder traversal and print the elements.

**[Code](data-structures/binary_search_tree.py)**

### 5. Graph (Adjacency List)
A **graph** is a collection of nodes and edges that represent connections between the nodes. It can be represented using an **adjacency list**. The operations supported are:
- `add_edge(u, v)`: Add an edge between nodes `u` and `v`.
- `bfs(start_node)`: Perform a breadth-first search from the start node.

**[Code](data-structures/graph.py)**

### 6. Min-Heap
A **min-heap** is a binary tree in which the parent node is always less than or equal to its children. The operations supported are:
- `insert(element)`: Insert an element into the heap.
- `extract_min()`: Extract and return the minimum element.
- `peek_min()`: View the minimum element without removing it.

**[Code](data-structures/heap.py)**

## How to Use

1. Clone this repository to your local machine using:
   ```bash
   git clone https://github.com/yourusername/python-data-structures.git
 
