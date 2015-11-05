#!/usr/bin/env python
from pkg.code import commandMapper, globalStateObject

args = [""]
gso = globalStateObject.GlobalStateObject()

while args[0] != commandMapper.END_COMMAND:
  try:
    args = raw_input().split()
    command = commandMapper.getCommand(args[0])
    if not isinstance(command, commandMapper.NoOpCommand):
      command.function(gso, args)
  except (EOFError):
    break
