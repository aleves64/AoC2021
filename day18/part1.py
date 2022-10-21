import os
from myinput import myinput
from math import floor
from math import ceil

class Node:
	def __init__(self, parent, val = None, left = None, right = None):
		self.left = left
		self.right = right
		self.parent = parent
		self.val = val

def make_tree(l):
	if type(l) != list:
		node = Node(parent=None)
		node.val = l
		return node
	node = Node(parent=None)
	node.left = make_tree(l[0])
	node.left.parent = node
	node.right = make_tree(l[1])
	node.right.parent = node
	return node

def print_tree_iter(node):
	if node:
		if not node.val == None:
			print(node.val, end='')
		else:
			print("[", end='')
			print_tree_iter(node.left)
			print(",", end='')
			print_tree_iter(node.right)
			print("]", end='')

def print_tree(node):
	print_tree_iter(node)
	print()

def get_left_neighbor(node):
	parent = node.parent
	child = node
	while parent and child == parent.left:
		child = parent
		parent = child.parent
	if parent:
		left_neighbor = parent.left
		while left_neighbor.val == None:
			left_neighbor = left_neighbor.right
	else:
		left_neighbor = None
	return left_neighbor

def get_right_neighbor(node):
	parent = node.parent
	child = node
	while parent and child == parent.right:
		child = parent
		parent = child.parent
	if parent:
		right_neighbor = parent.right
		while right_neighbor.val == None:
			right_neighbor = right_neighbor.left
	else:
		right_neighbor = None
	return right_neighbor

def explode(node, depth):
	if not node.val == None:
		return False
	left_exploded = explode(node.left, depth + 1)
	right_exploded = explode(node.right, depth + 1)
	anything_exploded = left_exploded or right_exploded

	if depth > 4:
		left_neighbor = get_left_neighbor(node)
		right_neighbor = get_right_neighbor(node)

		zeronode = Node(parent = node.parent)
		zeronode.val = 0

		if right_neighbor:
			right_neighbor.val += node.right.val
		if left_neighbor:
			left_neighbor.val += node.left.val
		if node == node.parent.left:
			node.parent.left = zeronode
		else:
			node.parent.right = zeronode
		return True
	return anything_exploded


def split(node):
	if not node.val == None:
		val = node.val
		if val > 9:
			leftval = floor(val / 2)
			rightval = ceil(val / 2)
			leftnode = Node(parent=node)
			rightnode = Node(parent=node)
			leftnode.val = leftval
			rightnode.val = rightval
			node.val = None
			node.left = leftnode
			node.right = rightnode
			return True
		return False
	else:
		leftsplits = split(node.left)
		if leftsplits:
			return True
		rightsplits = split(node.right)
		if rightsplits:
			return True
		return False

def reduce(node, depth):
	if not node.val == None:
		return
	reduce(node.left, depth + 1)
	reduce(node.right, depth + 1)
	print(depth)
	while True:
		if explode(node, depth):
			continue
		if split(node):
			continue
		break

def add(node1, node2):
	parent = Node(parent=None)
	parent.left = node1
	parent.right = node2
	node1.parent = parent
	node2.parent = parent
	return parent

def magnitude(node):
	if not node.val == None:
		return node.val
	return 3 * magnitude(node.left) + 2 * magnitude(node.right)

tree = make_tree(myinput[0])
for i in range(1, len(myinput)):
	tree_add = make_tree(myinput[i])
	tree = add(tree, tree_add)
	while True:
		if explode(tree, 1):
			continue
		if split(tree):
			continue
		break
print_tree(tree)
print(magnitude(tree))