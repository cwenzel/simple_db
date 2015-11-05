import unittest
from cStringIO import StringIO
import sys

from ..code import dataCommands
import fakeStateObject

class DataCommandsTest(unittest.TestCase):

  def test_setValue(self):
    fso = fakeStateObject.FakeStateObject()
    fso.dictionaryStack = [{'a',1},{'b':10}]
    dataCommands.setValue(fso, ['SET', 'a', 15])
    dataCommands.setValue(fso, ['SET', 'b', 99])
    self.assertEqual(fso.dictionaryStack[1]['a'], 15)
    self.assertEqual(fso.dictionaryStack[1]['b'], 99)

  def test_getValue1(self):
    fso = fakeStateObject.FakeStateObject()
    fso.dictionaryStack = [{'a':5, 'b':10, 'c':100}]

    old_stdout = sys.stdout
    sys.stdout = mystdout = StringIO()

    dataCommands.getValue(fso, ['GET', 'a'])
    dataCommands.getValue(fso, ['GET', 'b'])
    dataCommands.getValue(fso, ['GET', 'c'])
    dataCommands.getValue(fso, ['GET', 'c'])
    dataCommands.getValue(fso, ['GET', 'z'])

    sys.stdout = old_stdout

    self.assertEqual(mystdout.getvalue(), '5\n10\n100\n100\nNULL\n')

  def test_getValue2(self):
    fso = fakeStateObject.FakeStateObject()
    fso.dictionaryStack = [{'a':1}, {'a':2}, {'a':3}]

    old_stdout = sys.stdout
    sys.stdout = mystdout = StringIO()

    dataCommands.getValue(fso, ['GET', 'a'])

    sys.stdout = old_stdout

    self.assertEqual(mystdout.getvalue(), '3\n')

  def test_getValue3(self):
    fso = fakeStateObject.FakeStateObject()
    fso.dictionaryStack = [{'a':1}, {'a':2}, {'a':3}]
    fso.unsetVariables.append('a')
    old_stdout = sys.stdout
    sys.stdout = mystdout = StringIO()

    dataCommands.getValue(fso, ['GET', 'a'])

    sys.stdout = old_stdout

    self.assertEqual(mystdout.getvalue(), 'NULL\n')

  def test_unsetValue1(self):
    fso = fakeStateObject.FakeStateObject()
    fso.dictionaryStack = [{'a':5,'b':10,'c':100}]

    dataCommands.unsetValue(fso, ['UNSET', 'a'])
    self.assertEqual(fso.dictionaryStack[0].get('a'), None)
    self.assertEqual(fso.dictionaryStack[0].get('b'), 10)

    # test a double unset
    dataCommands.unsetValue(fso, ['UNSET', 'a'])
    self.assertEqual(fso.dictionaryStack[0].get('a'), None)

  def test_unsetValue2(self):
    fso = fakeStateObject.FakeStateObject()
    fso.dictionaryStack = [{'a':1},{'a':2},{'a':3}]

    dataCommands.unsetValue(fso, ['UNSET', 'a'])
    self.assertEqual(fso.dictionaryStack[2].get('a'), None)
    self.assertEqual(fso.unsetVariables.count('a'), 1)

  def test_numEq1(self):
    fso = fakeStateObject.FakeStateObject()
    fso.dictionaryStack = [{'a': 5, 'b' : 10, 'c' : 100, 'd': 5}]

    old_stdout = sys.stdout
    sys.stdout = mystdout = StringIO()

    dataCommands.numEq(fso, ['NUMEQUALTO', 5])
    dataCommands.numEq(fso, ['NUMEQUALTO', 1])
    dataCommands.numEq(fso, ['NUMEQUALTO', 10])

    sys.stdout = old_stdout

    self.assertEqual(mystdout.getvalue(), '2\n0\n1\n')

  def test_numEq2(self):
    fso = fakeStateObject.FakeStateObject()
    fso.dictionaryStack = [{'a':5},{'b':10},{'c':10},{'d':5}]

    old_stdout = sys.stdout
    sys.stdout = mystdout = StringIO()

    dataCommands.numEq(fso, ['NUMEQUALTO', 5])
    dataCommands.numEq(fso, ['NUMEQUALTO', 1])
    dataCommands.numEq(fso, ['NUMEQUALTO', 10])

    sys.stdout = old_stdout

    self.assertEqual(mystdout.getvalue(), '2\n0\n2\n')

  def test_numEq3(self):
    fso = fakeStateObject.FakeStateObject()
    fso.dictionaryStack = [{'a': 5, 'b' : 10, 'c' : 10, 'd': 5}]
    fso.unsetVariables.append('b')
    old_stdout = sys.stdout
    sys.stdout = mystdout = StringIO()

    dataCommands.numEq(fso, ['NUMEQUALTO', 5])
    dataCommands.numEq(fso, ['NUMEQUALTO', 1])
    dataCommands.numEq(fso, ['NUMEQUALTO', 10])

    sys.stdout = old_stdout

    self.assertEqual(mystdout.getvalue(), '2\n0\n1\n')


if __name__ == '__main__':
  unittest.main()
