def begin(gso, args):
  gso.dictionaryStack.append({})

def rollback(gso, args):
  gso.unsetVariables = []
  if len(gso.dictionaryStack) > 1:
    gso.dictionaryStack.pop()
  else:
    print("NO TRANSACTION")

def commit(gso, args):
  if len(gso.dictionaryStack) == 1:
    print("NO TRANSACTION")

  while len(gso.dictionaryStack) > 1:
    topDictionary = gso.dictionaryStack.pop()
    gso.dictionaryStack[len(gso.dictionaryStack) - 1].update(topDictionary)
  for unset in gso.unsetVariables:
   if gso.dictionaryStack[0].get(unset) != None:
     del gso.dictionaryStack[0][unset]
  gso.unsetVariables = []
