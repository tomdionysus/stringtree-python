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


  def add_vertical(self, key, value):
    offset = 0
    while offset<len(key):
      self = self.add_horizontal(key[offset])
      offset += 1
      if self.down == None:
        break
      self = self.down

    # TODO: This be ugly but it works. Refactor after coffee
    # and possibly clue injection.
    if offset==len(key):
      self.up.value = value
      return self.up

    while offset<len(key):
      self.down = Node(self, key[offset])
      self = self.down
      offset += 1

    self.value = value
    return self

  def to_s(self):
    s = ""
    while self != None:
      s = self.char + s
      self = self.up
    return s 

  def walk(self, s = ""):
    if self.value != None:
      yield [s+self.char,self.value]
    if self.left!=None:
      self.left.walk(s)
    if self.down!=None:
      self.down.walk(s+self.char)
    if self.right!=None:
      self.right.walk(s)




