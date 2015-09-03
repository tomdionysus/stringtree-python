import unittest
import coveralls
import stringtree

class TestNode(unittest.TestCase):

  def test_init(self):
    node = stringtree.Node(1,2,3)
    self.assertEqual(node.up,1)
    self.assertEqual(node.char,2)
    self.assertEqual(node.value,3)

  def test_add_horizontal(self):
    nodea = stringtree.Node(None,'m',3)
    nodeb = nodea.add_horizontal('a')
    nodec = nodea.add_horizontal('z')

    self.assertEqual(nodea.left,nodeb)
    self.assertEqual(nodea.right,nodec)

    noded = nodea.add_horizontal('b')
    nodee = nodea.add_horizontal('y')

    self.assertEqual(nodea.left.right,noded)
    self.assertEqual(nodea.right.left,nodee)

  def test_count_left_count_right(self):
    nodea = stringtree.Node(None,'m',3)
    noded = nodea.add_horizontal('b')
    nodeb = nodea.add_horizontal('a')
    nodee = nodea.add_horizontal('y')
    nodec = nodea.add_horizontal('z')
    nodec = nodea.add_horizontal('A')

    self.assertEqual(nodea.count_left(),3)
    self.assertEqual(nodea.count_right(),2)

  def test_add_vertical(self):

    nodea = stringtree.Node(None,'a')
    last_node = nodea.add_vertical('aardvark',56)

    self.assertEqual(nodea.down.down.down.down.down.down.down,last_node)

    self.assertEqual(nodea.char,'a')
    self.assertEqual(nodea.down.char,'a')
    self.assertEqual(nodea.down.down.char,'r')
    self.assertEqual(nodea.down.down.down.char,'d')
    self.assertEqual(nodea.down.down.down.down.char,'v')
    self.assertEqual(nodea.down.down.down.down.down.char,'a')
    self.assertEqual(nodea.down.down.down.down.down.down.char,'r')
    self.assertEqual(nodea.down.down.down.down.down.down.down.char,'k')

    last_node = nodea.add_vertical('aardtest',56)

    self.assertEqual(nodea.down.down.down.down.left.down.down.down,last_node)

  def test_to_s(self):

    nodea = stringtree.Node(None,'a')
    last_nodeb = nodea.add_vertical('aardtest',32)
    last_noded = nodea.add_vertical('pengiuin',16)
    last_nodea = nodea.add_vertical('aardvark',56)
    last_nodec = nodea.add_vertical('aard',64)

    self.assertEqual(last_nodea.to_s(),'aardvark')
    self.assertEqual(last_nodeb.to_s(),'aardtest')
    self.assertEqual(last_nodec.to_s(),'aard')
    self.assertEqual(last_noded.to_s(),'pengiuin')

