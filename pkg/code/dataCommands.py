import collections
import copy

def setValue(gso, args):
  if len(args) == 3:
    dictionary = gso.dictionaryStack[len(gso.dictionaryStack)-1]
    dictionary[args[1]] = args[2]

def getValue(gso, args):
  def loopStack(stack, key):
    dictionary = stack.pop()
    value = dictionary.get(key)
    if value is not None:
      print(value)
    elif len(stack) > 0:
      loopStack(stack, key)
    else:
      print("NULL")

  if len(args) == 2:
    if gso.unsetVariables.count(args[1]) > 0:
      print("NULL")
    else:
      loopStack(list(gso.dictionaryStack), args[1])

def unsetValue(gso, args):
  if len(args) == 2:
    if (gso.dictionaryStack[len(gso.dictionaryStack)-1].get(args[1]) is not None):
      del gso.dictionaryStack[len(gso.dictionaryStack)-1][args[1]]
    gso.unsetVariables.append(args[1])

def numEq(gso, args):
  def loopStack(stack, key):
    dictionary = stack.pop()
    for unset in gso.unsetVariables:
      if dictionary.get(unset) != None:
        del dictionary[unset]
    c = collections.Counter(dictionary.values())
    count = c[key]
    if len(stack) > 0:
      return count + loopStack(stack, key)
    else:
      return count
  if len(args) == 2:
    print(loopStack(copy.deepcopy(gso.dictionaryStack), args[1]))
