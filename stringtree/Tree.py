class Tree(object):

  def __init__(self):
    self.clear()

  def add(self, key, value):
    if self.root == None:
      self.root = Node(None,key[0])
    self.root.add_vertical(key,value)

  def exists(self, key):
    if self.root == None:
      return false
    return self.root.find_vertical(key) != None

  def delete(self, key):
    if self.root == None:
      return false
    node = self.root.find_vertical(key)
    if node == None:
      return false
    
    t = node.value
    node.value = None
    return t != None
  
  def clear(self):
    self.root = None

  def walk(self):
    if self.root == None:
      return false
    self.root.walk()