import dataCommands
import transactionCommands

class Command:
  def __init__(self, function):
    self.function = function

class DataCommand(Command):
  pass

class TransactionCommand(Command):
  pass

class NoOpCommand(Command):
  pass

#data commands
SET_COMMAND = "SET"
GET_COMMAND = "GET"
UNSET_COMMAND = "UNSET"
NUMEQ_COMMAND = "NUMEQUALTO"
END_COMMAND = "END"

#transaction commands
BEGIN_COMMAND = "BEGIN"
ROLLBACK_COMMAND = "ROLLBACK"
COMMIT_COMMAND = "COMMIT"

commandLookups = {SET_COMMAND: DataCommand(dataCommands.setValue),
                  GET_COMMAND: DataCommand(dataCommands.getValue),
                  UNSET_COMMAND: DataCommand(dataCommands.unsetValue),
                  NUMEQ_COMMAND: DataCommand(dataCommands.numEq),
                  END_COMMAND: NoOpCommand(None), #handled in outer loop
                  BEGIN_COMMAND: TransactionCommand(transactionCommands.begin),
                  ROLLBACK_COMMAND: TransactionCommand(transactionCommands.rollback),
                  COMMIT_COMMAND: TransactionCommand(transactionCommands.commit)}

def getCommand(commandString):
  return commandLookups.get(commandString)
