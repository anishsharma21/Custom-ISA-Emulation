from typing import List, Tuple
from helpers import find_operation_from_opcode

def file_contents_to_instructions(file_contents: List[str]) -> List[Tuple[str, int]]:
  # assuming instructions are in order
  i: int = 0
  instructions: List[Tuple[str, int]] = []
  while i < len(file_contents):
    line: str = file_contents[i]
    if line[-1] == ":": # memory address declaration
      i += 1
      continue
    if line == "FFh": # HLT
      break
    # assuming instructions are written correctly in 3 byte sequences
    opcode: int = int(line.removesuffix("h"), 16)
    operation: str = find_operation_from_opcode(opcode)
    address: int = int(file_contents[i+1].removesuffix("h") + file_contents[i+2].removesuffix("h"), 16)
    instructions.append((operation, address))
    i += 3
  return instructions

def print_instructions(instructions: List[Tuple[str, int]]) -> None:
  for instruction in instructions:
      operation, address = instruction
      print(f"{operation}: {address:#06x}")