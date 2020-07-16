# python3

import sys
import threading
from copy import deepcopy
from collections import deque


class Node():
    def __init__(self, name: int, parent: int, children=[]):
        self.name = name
        self.parent = parent
        self.children = children
    
    def add_child(self, child):
        children = deepcopy(self.children)
        children.append(child)
        self.children = children
    
    def add_parent(self, parent):
        self.parent = parent


def compute_height(n, parents):
    root = -1
    nodes = []
    for i in range(n):
        nodes.append(Node(i, parents[i]))
    
    for child in range(n):
        parent_index = nodes[child].parent
        if parent_index == -1:
            root = child
        else:
            nodes[parent_index].add_child(nodes[child]) 
    
    return height2(nodes, root)


def print_mas(mas):
    for elem in mas:
        print("NAME", elem.name)
        print("PAR", elem.parent)
        for child in elem.children:
            print("CHILD", elem.name, child)


def height(nodes, parent):
    children = nodes[parent].children
    if children:
        max_height = 0
        for child in children:
            max_height = max(max_height, height(nodes, child.name))
        return 1 + max_height
    else:
        return 1


def height2(nodes, root):
    h = 1
    children = deque(nodes[root].children)
    while True:
        size = len(children)
        if not size:
            return h
        while size:
            child = children.popleft()
            children.extend(nodes[child.name].children)
            size -= 1
        h += 1
    return h


def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height(n, parents))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()