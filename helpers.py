from typing import Tuple

### Utilities ###

def get_file_contents(file_name: str) -> list[str]:
  memcontents: list[str] = []
  
  try:
    with open(f'./programs/{file_name}', 'r') as file:
      memcontents: list[str] = file.readlines()
  except FileNotFoundError:
    print("File not found")
    print()
  except Exception as e:
    print(f"Error: {e}")
    print()

  return [s.strip() for s in memcontents if s.strip()]

### Memory ###

def render_memory(ram: dict[int, int]) -> None:
  prevAddress = 0
  for address, value in ram.items():
    if prevAddress < address - 1:
      print("...")
    prevAddress = address
    print(f"{address:#06x}: {value:#04x}")

def generate_mem_snapshot(file_contents: list[str]) -> dict[int, int]:
  ram = {}
  curAddress = 0x0000
  for line in file_contents:
    if line[-1] == ":":
      curAddress = int(line.removesuffix("h:"), 16)
      ram[curAddress] = 0x00
    elif curAddress in ram:
      curAddress += 1
      ram[curAddress] = int(line.removesuffix("h"), 16)
  return ram

def to_instructions(memcontents: list[str]) -> list[Tuple[str, int]]:
  # assuming instructions are in order
  i: int = 0
  instructions: list[Tuple[str, int]]
  while i < len(memcontents):
    line: str = memcontents[i]
    if line[-1] == ":":
      i += 1
      continue
    if line == "FFh":
      break
    # assuming instructions are written correctly in 3 byte sequences
    opcode: int = int(line.removesuffix("h"), 16)
    operation: str = find_operation_from_opcode(opcode)
    address: int = int(memcontents[i+1].removesuffix("h") + memcontents[i+2].removesuffix("h"), 16)
    print((operation, address)) 
    i += 3
  return [('', 1)]

def find_operation_from_opcode(opcode: int) -> str:
  switch: dict[int, str] = {
    0x10: "LOD",
    0x11: "STO",
    0x20: "ADD",
    0xFF: "HLT",
  }
  return switch.get(opcode, "ERR")

def print_program_instructions(ram: dict[int, int]) -> None:
  count = 0
  for _, value in ram.items():
    count += 1
    if count % 3 == 2:
      op: str = find_operation_from_opcode(value)
      if op == "HLT":
        break
      print(op)