class FakeStateObject:
  def __init__(self):
    self.dictionaryStack = [{}]
    self.unsetVariables = []
