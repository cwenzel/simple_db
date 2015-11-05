import unittest
from ..code import commandMapper

class CommandMapperTest(unittest.TestCase):

  def test_invalid_commands(self):
    self.assertEqual(commandMapper.getCommand('foo'), None)

  def test_valid_commands(self):
    self.assertNotEqual(commandMapper.getCommand('BEGIN').function, None)
    self.assertNotEqual(commandMapper.getCommand('SET').function, None)

  # The end command is special in that it is a known mappable command,
  # but we still want it to return None because it is handled in the main
  def test_end_command(self):
    self.assertEqual(commandMapper.getCommand('END').function, None)

if __name__ == '__main__':
  unittest.main()
