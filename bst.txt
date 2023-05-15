from typing import Union, Optional # since there's no `number` type in python, for Union(int, float)

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

# Skeleton implementation of balance BST (AVL Tree)
# AVLNode add member variable self.balance (to store balance value of node), function computeBalance (to calculate balance of node), functions rotateLeft and rotateRight (to assist with balancing node), and function rebalance (to balance the node using rotateLeft and rotateRight)
'''
from pampy import match, _ # pattern matching
class AvlNode(Node):
	def __init__(self, val: Union[int, float], parentNode: 'Node' = None, leftNode: 'Node' = None, rightNode: 'Node' = None) -> None: # type 'Node' in quotes as a way to forward-declare the class
		self.val = val
		self.parent = parentNode
		self.left = leftNode
		self.right = rightNode
		
	# Uses pattern matching
	def computeBal(self):
		return match((self.left, self.right), 
			(AvlNode, None), lambda left: -1 + left.computeBal(),
			(None, AvlNode), lambda right: 1 + right.computeBal(),
			_, 0)

	def rebalance(self):
		# should first create private rotate_left and rotate_right functions that this uses

	# rotates node left
	def __rotateLeft__(self):

	# rotates node right
	def __rotateRight__(self):

 
class avlTree(BinarySearchTree):
	# Same as BST.insertNode, but rebalances at end
	def insertNode(self, node: Node) -> None:
		if self.head is None: self.head = node
		else: self.head.addChild(node)
		self.rebalance()

	def rebalance(self) -> None:
		# uses Node.rotateLeft and Node.rotateRIght
'''
		
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
'''
def avltree_test():
	avln = AvlNode(3)
	assert avln.computeBal() == 0

	avln.addChild(AvlNode(2))
	assert avln.computeBal() == -1

	avln.addChild(AvlNode(1))
	assert avln.computeBal() == -2
'''

bstree_test()
node_test()
# avltree_test()

