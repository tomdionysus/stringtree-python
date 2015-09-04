from Node import Node

class Tree(object):

  def __init__(self):
    self.clear()

  def add(self, key, value):
    if self.root == None:
      self.root = Node(None,key[0])
    node = self.root.add_vertical(key)

    node.value = value

  def exists(self, key):
    if self.root == None:
      return False
    node = self.root.find_vertical(key)
    return node != None and node.value != None

  def delete(self, key):
    if self.root == None:
      return False
    node = self.root.find_vertical(key)
    if node == None or node.value == None:
      return False
    
    node.value = None
    return True
  
  def clear(self):
    self.root = None

  def walk(self):
    if self.root == None:
      return
    self.root.walk()

  def count(self):
    if self.root == None:
      return 0

    count = 0
    for node in self.root.walk():
      if node.value!=None:
        count += 1

    return count
