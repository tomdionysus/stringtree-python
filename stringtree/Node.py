class Node(object):

  def __init__(self, up, char, value = None):
    self.left = None
    self.right = None
    self.up = up
    self.down = None
    self.char = char
    self.value = value

  def add_horizontal(self, char):
    if char == self.char:
      return self 

    if char > self.char:
      if self.right == None:
        self.right = Node(self.up, char)
        return self.right
      else:
        return self.right.add_horizontal(char)
    else:
      if self.left == None:
        self.left = Node(self.up, char)
        return self.left
      else:
        return self.left.add_horizontal(char)

  def find_horizontal(self,char):
    if char == self.char:
      return self 

    if char > self.char:
      if self.right == None:
        return None
      else:
        return self.right.find_horizontal(char)
    else:
      if self.left == None:
        return None
      else:
        return self.left.find_horizontal(char)

  def count_left(self):
    x = 0
    while self.left!=None:
      self = self.left
      x += 1
    return x

  def count_right(self):
    x = 0
    while self.right!=None:
      self = self.right
      x += 1
    return x


  def add_vertical(self, key):
    first = True
    for c in key:
      if not first:
        if self.down == None:
          self.down = Node(self,c)
        self = self.down
      self = self.add_horizontal(c)
      first = False

    return self

  def find_vertical(self, key):
    first = True

    for c in key:
      if not first:
        self = self.down
        if self == None:
          return None
      self = self.find_horizontal(c)
      if self == None:
        return None
      first = False

    return self

  def to_s(self):
    s = ""
    while self != None:
      s = self.char + s
      self = self.up
    return s 

  def walk(self, s = ""):
    yield self
    if self.left!=None:
      for i in self.left.walk(s):
        yield i
    if self.down!=None:
      for i in self.down.walk(s):
        yield i
    if self.right!=None:
      for i in self.right.walk(s):
        yield i




