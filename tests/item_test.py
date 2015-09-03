import unittest
import coveralls
import stringtree

class TestTree(unittest.TestCase):

  def test_init(self):
    node = stringtree.Item(1,2,3)
    self.assertEqual(node.key,1)
    self.assertEqual(node.value,2)
    self.assertEqual(node.offset,3)
