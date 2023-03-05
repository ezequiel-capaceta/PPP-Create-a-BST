#Part 1: Create a BSTNode class
class BSTNode:
  def __init__(self, data = None, left = None, right = None):
    self.data = data
    self.left = left
    self.right = right
  def __str__(self):
    return str(self.data)
  def __repr__(self):
    return str(self.data)


#Part 2: Create a BST class
  #Part 3: Add functionality to your BST class

class BST:
  def __init__(self, root=None):
    self.root = root
    self.contents = []