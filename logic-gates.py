from typing import Dict

class Gate:
  def __init__(self, name: str):
    self.name = name
    self.inputs: Dict[str, int]
    self.outputs: Dict[str, int]

  def setInput(self, inputChoice: str, inputValue: int):
    inputChoiceExists = self.inputs.get(inputChoice)
    if inputChoiceExists:
      self.inputs[inputChoice] = inputValue
    else:
      raise ValueError(f"Input choice {inputChoice} does not exist for gate {self.name}")

andGate = Gate("And")
print(andGate.name)