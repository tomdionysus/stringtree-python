import unittest
import coveralls
import stringtree
import types

class TestTree(unittest.TestCase):

  def test_init(self):
    tree = stringtree.Tree()
    self.assertEqual(tree.root, None)

  def test_add_has_key(self):
    tree = stringtree.Tree()

    tree.add('one', 4)
    tree.add('two', 5)
    tree.add('three', 6)

    self.assertEqual(tree.root.char, 'o')
    self.assertEqual(tree.root.down.down.value, 4)

    self.assertTrue(tree.has_key('one'))
    self.assertTrue(tree.has_key('two'))
    self.assertTrue(tree.has_key('three'))

    self.assertFalse(tree.has_key('o'))
    self.assertFalse(tree.has_key('on'))
    self.assertFalse(tree.has_key('twow'))
    self.assertFalse(tree.has_key('t'))

  def test_delete(self):
    tree = stringtree.Tree()

    tree.add('one', 4)
    tree.add('two', 5)
    tree.add('three', 6)

    tree.delete('two')

    self.assertTrue(tree.has_key('one'))
    self.assertFalse(tree.has_key('two'))
    self.assertTrue(tree.has_key('three'))

  def test_clear(self):
    tree = stringtree.Tree()

    tree.add('one', 4)
    tree.add('two', 5)
    tree.add('three', 6)

    tree.clear()

    self.assertEqual(tree.root, None)

    self.assertFalse(tree.has_key('one'))
    self.assertFalse(tree.has_key('two'))
    self.assertFalse(tree.has_key('three'))

  def test_count(self):
    tree = stringtree.Tree()

    self.assertEqual(len(tree), 0)

    tree.add('one', 4)
    self.assertEqual(len(tree), 1)
    tree.add('two', 5)
    self.assertEqual(len(tree), 2)
    tree.add('three', 6)
    self.assertEqual(len(tree), 3)
    tree.delete('two')
    self.assertEqual(len(tree), 2)

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
