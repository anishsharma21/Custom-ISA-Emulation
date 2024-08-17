from typing import Tuple

### Utilities ###

def get_file_contents(file_name: str) -> list[str]:
  if not file_name.endswith(".txt"):  
    file_name += ".txt"
    
  file_contents: list[str] = []
  
  try:
    with open(f'./programs/{file_name}', 'r') as file:
      file_contents: list[str] = file.readlines()
  except FileNotFoundError:
    print("File not found")
    print()
  except Exception as e:
    print(f"Error: {e}")
    print()

  return [s.strip() for s in file_contents if s.strip()]

### Memory ###

def render_mem_map_from_ram(ram: dict[int, int]) -> None:
  prevAddress = 0
  for address, value in ram.items():
    if prevAddress < address - 1:
      print("...")
    prevAddress = address
    print(f"{address:#06x}: {value:#04x}")

def get_ram_from_mem_contents(file_contents: list[str]) -> dict[int, int]:
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

def file_contents_to_instructions(file_contents: list[str]) -> list[Tuple[str, int]]:
  # assuming instructions are in order
  i: int = 0
  instructions: list[Tuple[str, int]] = []
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

def print_instructions(instructions: list[Tuple[str, int]]) -> None:
  for instruction in instructions:
      operation, address = instruction
      print(f"{operation}: {address:#06x}")

def find_operation_from_opcode(opcode: int) -> str:
  switch: dict[int, str] = {
    0x10: "LOD",
    0x11: "STO",
    0x20: "ADD",
    0xFF: "HLT",
  }
  return switch.get(opcode, "ERR")