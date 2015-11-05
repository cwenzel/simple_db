def begin(gso, args):
  gso.dictionaryStack.append({})

def rollback(gso, args):
 gso.unsetVariables = []
 if len(gso.dictionaryStack) > 1:
    gso.dictionaryStack.pop()
 else:
    print("NO TRANSACTION")

def commit(gso, args):
  gso.unsetVariables = []
  if len(gso.dictionaryStack) == 1:
    print("NO TRANSACTION")

  while len(gso.dictionaryStack) > 1:
    topDictionary = gso.dictionaryStack.pop()
    gso.dictionaryStack[len(gso.dictionaryStack) - 1].update(topDictionary)
