import unittest
import coveralls
import stringtree

class TestTree(unittest.TestCase):

  def test_init(self):
    node = stringtree.Tree()
    self.assertEqual(node.root,None)
