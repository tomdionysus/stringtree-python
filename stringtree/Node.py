class Node(object):

  def __init__(self, char = None, value = None):
    self.left = None
    self.right = None
    self.up = None
    self.down = None
    self.char = char
    self.value = value

  def add_horizontal(self, node):
    if node.char < self.char:
      if self.left == None:
        self.left = node
      else:
        self.left.add_horizontal(node)
    else:
      if self.right == None:
        self.right = node
      else:
        self.right.add_horizontal(node)

  def add_horizontal_new(self, char, value):
    node = Node(char, value)
    self.add_horizontal(node)
    return node

  def add_vertical(self, key, value, offset = 0):
    node = add_horizontal_new(c, None)
    
    while c<key.length:
      c = key[offset]
      offset += 1

    node.value = value
    return node




