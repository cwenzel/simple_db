class GlobalStateObject:
  __sharedState = {}
  def __init__(self):
    self.__dict__ = self.__sharedState
  dictionaryStack = [{}]
  unsetVariables = []
