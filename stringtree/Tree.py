from Node import Node

class Tree(object):

  def __init__(self):
    self.clear()

  def __setitem__(self, key, value):
    if self.root == None:
      self.root = Node(None,key[0])
    node = self.root.add_vertical(key)

    node.value = value

  def __getitem__(self, key):
    if self.root == None:
      return False
    node = self.root.find_vertical(key)
    if node == None:
      raise KeyError
    return node.value

  def has_key(self, key):
    if self.root == None:
      return False
    node = self.root.find_vertical(key)
    return node != None and node.value != None

  def __del__(self, key):
    self.delete(key)

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

  def __len__(self):
    if self.root == None:
      return 0

    len = 0
    for node in self.root.walk():
      if node.value!=None:
        len += 1

    return len

  def partials(self, key):
    if self.root == None:
      return
    node = self.root.find_vertical(key)
    if node == None or node.down == None:
      return
    for node in node.down.walk():
      if node.value != None:
        yield node.to_s()
