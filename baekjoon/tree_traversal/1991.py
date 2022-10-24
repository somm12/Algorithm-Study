import sys
input = sys.stdin.readline

class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

def preOrder(node):
    print(node.data, end='')
    if node.left != None:
        preOrder(tree[node.left])
    if node.right != None:
        preOrder(tree[node.right])

def inOrder(node):
    if node.left != None:
        inOrder(tree[node.left])
    print(node.data, end='')
    if node.right != None:
        inOrder(tree[node.right])

def postOrder(node):
    if node.left != None:
        postOrder(tree[node.left])
    if node.right != None:
        postOrder(tree[node.right])
    print(node.data, end='')

n = int(input())
tree = {}

for _ in range(n):
    data, left, right = input().split()
    if left == '.':
        left = None
    if right == '.':
        right = None
    tree[data] = Node(data, left, right)

preOrder(tree['A'])
print()
inOrder(tree['A'])
print()
postOrder(tree['A'])