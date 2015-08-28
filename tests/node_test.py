import unittest
import coveralls
import stringtree

class TestNode(unittest.TestCase):

  def testInit(self):
    node = stringtree.Node(1,2)
    self.assertEqual(node.char,1)
    self.assertEqual(node.value,2)

  def testAddHorizontal(self):
    nodea = stringtree.Node(3,2)
    nodeb = stringtree.Node(4,4)
    nodec = stringtree.Node(1,1)

    nodea.add_horizontal(nodeb)
    nodea.add_horizontal(nodec)

    self.assertEqual(nodea.left.char,1)
    self.assertEqual(nodea.right.char,4)

  def testAddHorizontalNew(self):
    nodea = stringtree.Node(3,3)
    nodeb = nodea.add_horizontal_new(2,2)
    nodec = nodea.add_horizontal_new(4,4)

    self.assertEqual(nodea.left.char,2)
    self.assertEqual(nodea.right.char,4)

  def testAddVertical(self):
    nodea = stringtree.Node('a',3)

