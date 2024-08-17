from typing import Dict, List

### Utilities ###

def get_file_contents(file_name: str) -> List[str]:
  if not file_name.endswith(".txt"):  
    file_name += ".txt"

  file_contents: List[str] = []
  
  try:
    with open(f'./programs/{file_name}', 'r') as file:
      file_contents: List[str] = file.readlines()
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

def get_ram_from_mem_contents(file_contents: List[str]) -> dict[int, int]:
  ram = {}
  curAddress = 0x0000
  for line in file_contents:
    if line[-1] == ":":
      curAddress = int(line.removesuffix("h:"), 16)
      ram[curAddress] = 0x00
    elif curAddress in ram or curAddress - 1 in ram:
      ram[curAddress] = int(line.removesuffix("h"), 16)
      curAddress += 1
  return ram

def find_operation_from_opcode(opcode: int) -> str:
  switch: Dict[int, str] = {
    0x10: "LOD",
    0x11: "STO",
    0x20: "ADD",
    0xFF: "HLT",
  }
  return switch.get(opcode, "ERR")