import unittest
from cStringIO import StringIO
import sys

import fakeStateObject
from ..code import transactionCommands

class TransactionCommandsTest(unittest.TestCase):

  def test_begin(self):
    fso = fakeStateObject.FakeStateObject()
    fso.dictionaryStack = [{}]
    transactionCommands.begin(fso, None)
    self.assertEqual(len(fso.dictionaryStack), 2)
    transactionCommands.begin(fso, None)
    self.assertEqual(len(fso.dictionaryStack), 3)

  def test_rollback(self):
    fso = fakeStateObject.FakeStateObject()
    fso.dictionaryStack = [{}]

    old_stdout = sys.stdout
    sys.stdout = mystdout = StringIO()

    transactionCommands.rollback(fso, None)

    sys.stdout = old_stdout
    self.assertEqual(mystdout.getvalue(), 'NO TRANSACTION\n')

    fso.unsetVariables = ['a']
    fso.dictionaryStack = [{'a':1}, {'a':2}, {'a':3}]
    transactionCommands.rollback(fso, None)
    self.assertEqual(fso.dictionaryStack[len(fso.dictionaryStack)-1]['a'], 2)
    self.assertEqual(len(fso.unsetVariables), 0)
    transactionCommands.rollback(fso, None)
    self.assertEqual(fso.dictionaryStack[len(fso.dictionaryStack)-1]['a'], 1)

  def test_commit(self):
    fso = fakeStateObject.FakeStateObject()
    fso.dictionaryStack = [{}]

    old_stdout = sys.stdout
    sys.stdout = mystdout = StringIO()

    transactionCommands.commit(fso, None)

    sys.stdout = old_stdout
    self.assertEqual(mystdout.getvalue(), 'NO TRANSACTION\n')

    fso.unsetVariables = ['w']
    fso.dictionaryStack = [{'a':1, 'd': 10}, {'a':2, 'b':9}, {'a':3}]
    transactionCommands.commit(fso, None)
    self.assertEqual(len(fso.unsetVariables), 0)
    self.assertEqual(fso.dictionaryStack[0]['a'], 3)
    self.assertEqual(fso.dictionaryStack[0]['b'], 9)
    self.assertEqual(fso.dictionaryStack[0]['d'], 10)

if __name__ == '__main__':
  unittest.main()
