import unittest
import coveralls
import stringtree

class TestTree(unittest.TestCase):

  def test_init(self):
    tree = stringtree.Tree()
    self.assertEqual(tree.root, None)

  def test_add_exists(self):
    tree = stringtree.Tree()

    tree.add('one', 4)
    tree.add('two', 5)
    tree.add('three', 6)

    self.assertEqual(tree.root.char, 'o')
    self.assertEqual(tree.root.down.down.value, 4)

    self.assertTrue(tree.exists('one'))
    self.assertTrue(tree.exists('two'))
    self.assertTrue(tree.exists('three'))

    self.assertFalse(tree.exists('o'))
    self.assertFalse(tree.exists('on'))
    self.assertFalse(tree.exists('twow'))
    self.assertFalse(tree.exists('t'))

  def test_delete(self):
    tree = stringtree.Tree()

    tree.add('one', 4)
    tree.add('two', 5)
    tree.add('three', 6)

    tree.delete('two')

    self.assertTrue(tree.exists('one'))
    self.assertFalse(tree.exists('two'))
    self.assertTrue(tree.exists('three'))

  def test_clear(self):
    tree = stringtree.Tree()

    tree.add('one', 4)
    tree.add('two', 5)
    tree.add('three', 6)

    tree.clear()

    self.assertEqual(tree.root, None)

    self.assertFalse(tree.exists('one'))
    self.assertFalse(tree.exists('two'))
    self.assertFalse(tree.exists('three'))

  def test_count(self):
    tree = stringtree.Tree()

    self.assertEqual(tree.count(), 0)

    tree.add('one', 4)
    self.assertEqual(tree.count(), 1)
    tree.add('two', 5)
    self.assertEqual(tree.count(), 2)
    tree.add('three', 6)
    self.assertEqual(tree.count(), 3)
    tree.delete('two')
    self.assertEqual(tree.count(), 2)

