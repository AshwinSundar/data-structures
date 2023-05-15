# OPTIONAL:
# print function
# DONE type annotations
# DONE find, return node
# AVL tree, derives from BinarySearchTree

# Short code review:
# One mistake made during interview was attempting to implement the "insertNode" logic in BST. It should be implemented in Node (as below)

from typing import Union, Optional # since there's no `number` type in python, for Union(int, float)
from pampy import match, _ # pattern matching

class Node:
	def __init__(self, val: Union[int, float], parentNode: Union['Node', 'AvlNode'] = None, leftNode: Union['Node', 'AvlNode'] = None, rightNode: Union['Node', 'AvlNode'] = None) -> None: # type 'Node' in quotes as a way to forward-declare the class
		self.val = val
		self.parent = parentNode
		self.left = leftNode
		self.right = rightNode

	def addChild(self, childNode: Union['Node', 'AvlNode']) -> None:
		if childNode.val < self.val:
			if self.left is None:
				self.left = childNode
				childNode.parent = self
			else:
				self.left.addChild(childNode)
		else:
			if self.right is None:
				self.right = childNode
				childNode.parent = self
			else:
				self.right.addChild(childNode)

	def find(self, val: Union[int, float]) -> Optional['Node']:
		if self.val == val: return self
		elif val < self.val:
			if self.left is None: return None
			else: return self.left.find(val)	
		else:
			if self.right is None: return None
			else: return self.right.find(val)	


class BinarySearchTree:
	def __init__(self, node: Node) -> None: # Node type doesn't need to be in quotes here, because Node Class was already declared above
		self.head = node 

	def insertNode(self, node: Node) -> None:
		if self.head is None: self.head = node
		else: self.head.addChild(node)

# extends Node, computes balance factor for each subtree
class AvlNode(Node):
	def __init__(self, val: Union[int, float], parentNode: 'Node' = None, leftNode: 'Node' = None, rightNode: 'Node' = None) -> None: # type 'Node' in quotes as a way to forward-declare the class
		self.val = val
		self.parent = parentNode
		self.left = leftNode
		self.right = rightNode
		
	def computeBal(self):
		return match((self.left, self.right), 
			(AvlNode, None), lambda left: -1 + left.computeBal(),
			(None, AvlNode), lambda right: 1 + right.computeBal(),
			_, 0)

# YOU ARE HERE - let's write the rebalance function and then be done
# make this private as well? 
	def rebalance(self):
		# should first create private rotate_left and rotate_right functions that this uses

	def __rotateRight__(self):
		if self.left is None: return self
		else

	30
  20
10
		
	20
  10  30

	10
	  20
		30
class avlTree(BinarySearchTree):
	def insertNode(self, node: Node) -> None:
		# does same thing as Node.insert, but rebalances at end. actually is that needed? idk
		return self 
 
# Test setup
headNode = Node(3)
bstree = BinarySearchTree(headNode)
child1Node = Node(2)
child2Node = Node(1)
child3Node = Node(4)
child4Node = Node(4.5)
bstree.insertNode(child1Node)
bstree.insertNode(child2Node)
bstree.insertNode(child3Node)
bstree.insertNode(child4Node)

# BinarySearchTree tests
def bstree_test():
	assert bstree.head == headNode
	assert bstree.head.left.val == 2
	assert bstree.head.left.left.val == 1
	assert bstree.head.right.val == 4

	try: bstree.insertNode(3) # must insert type Node, not type int
	except AttributeError: assert True
	else: assert False

# Node tests
def node_test():
	assert headNode.parent == None
	assert headNode.left == child1Node
	assert headNode.right == child3Node

	assert child1Node.parent == headNode
	assert child1Node.left == child2Node
	assert child2Node.right == None
	
	assert child2Node.parent == child1Node
	assert child2Node.left == None
	assert child2Node.right == None

	assert child3Node.parent == headNode
	assert child3Node.left == None
	assert child3Node.right == child4Node

	assert child4Node.parent == child3Node
	assert child4Node.left == None
	assert child4Node.right == None

	assert headNode.find(3) == headNode
	assert headNode.find(2) == child1Node
	assert headNode.find(1) == child2Node
	assert headNode.find(4) == child3Node
	assert headNode.find(4.5) == child4Node

	try: headNode.addChild(5) # must insert type Node, not int
	except AttributeError: assert True
	else: assert False

# AVL tree test:
avln = AvlNode(3)
def avltree_test():
	assert avln.computeBal() == 0

	avln.addChild(AvlNode(2))
	assert avln.computeBal() == -1

	avln.addChild(AvlNode(1))
	assert avln.computeBal() == -2

bstree_test()
node_test()
# avltree_test()

'''
    2
1       3

2 -> Node(1,3,l->next,r->next)
2 -> Node(Node_A, Node_B)

	

====
        
Node(2, leftNode, rightNode)
leftNode(1, null, null)
rightNode(3, null, null)

'''
