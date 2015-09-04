import unittest
import coveralls
import stringtree
import types

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

  def test_partials(self):
    tree = stringtree.Tree()
    strs = (i for i in [
      'abortively', 'aboulia', 'abound', 'about', 'above', 'aboveboard', 
      'abracadabra', 'abrade', 'abrader', 'Abraham', 'abrasion'
    ])

    for s in strs:
      tree.add(s, s)

    # Tests

    gen = tree.partials('ab')
    self.assertTrue(isinstance(gen, types.GeneratorType))

    strs = (i for i in [
      'abortively', 'aboulia', 'abound', 'about', 'above', 'aboveboard', 
      'abracadabra', 'abrade', 'abrader', 'abrasion'
    ])

    for s in strs:
      self.assertEqual(s,gen.next())

    gen = tree.partials('abo')
    self.assertTrue(isinstance(gen, types.GeneratorType))

    strs = (i for i in [
      'abortively', 'aboulia', 'abound', 'about', 'above', 'aboveboard'
    ])

    for s in strs:
      x = gen.next()
      self.assertEqual(s,x)

    gen = tree.partials('abr')
    self.assertTrue(isinstance(gen, types.GeneratorType))

    strs = (i for i in [
      'abracadabra', 'abrade', 'abrader', 'abrasion'
    ])

    for s in strs:
      x = gen.next()
      self.assertEqual(s,x)

    gen = tree.partials('asckas')
    self.assertEqual(sum(1 for i in gen),0)
