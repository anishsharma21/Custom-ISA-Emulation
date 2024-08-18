import os
from typing import List
from helpers import get_file_contents, get_ram_from_mem_contents, find_operation_from_opcode, render_mem_map_from_ram
from exceptions import InvalidOpcode, InvalidAddress

def main():
  file_name: str = str(input("Enter the file name: ")).strip()
  
  if file_name in ["exit", "quit", "q", "x"]:
    return

  file_contents: List[str] = get_file_contents(file_name)
  ram: dict[int, int] = get_ram_from_mem_contents(file_contents)
  os.system('clear')
  render_mem_map_from_ram(ram)

  accumulator: int = 0x0000
  
  i: int = 0
  while i < len(file_contents):
    line: str = file_contents[i]
    if line[-1] == ":" or line[0] == "/": # skip memory address declaration
      i += 1
      continue
    if line == "FFh": # HLT
      break
    # assuming instructions are written correctly in 3 byte sequences
    opcode: int = int(line.removesuffix("h"), 16)
    operation: str = find_operation_from_opcode(opcode)
    address: int = int(file_contents[i+1].removesuffix("h") + file_contents[i+2].removesuffix("h"), 16)
    i += 3

    print()

    # ANSI escape codes for background colors
    BG_YELLOW = "\033[43m"
    RESET = "\033[0m"

    print(f"Accumulator value: {accumulator:#04x}")
    
    if address not in ram:
      ram[address] = 0x00

    if operation == "LOD":
      print(f"{BG_YELLOW}Loading {ram[address]:#04x} value from {address:#06x} into accumulator{RESET}")
      accumulator = ram[address]
    elif operation == "STO":
      print(f"{BG_YELLOW}Storing {accumulator:#04x} value from accumulator into address {address:#06x} ({ram[address]:#04x}){RESET}")
      ram[address] = accumulator
    elif operation == "ADD":
      print(f"{BG_YELLOW}Adding {ram[address]:#04x} value from {address:#06x} into accumulator{RESET}")
      accumulator += ram[address]
    elif operation == "SUB":
      print(f"{BG_YELLOW}Subtracting {ram[address]:#04x} value from {address:#06x} from accumulator{RESET}")
      accumulator -= ram[address]
    elif operation == "JMP":
      jumped: bool = False
      for j in range(len(file_contents) - 1):
          if file_contents[j] == ((f"{address:#04x}")[2:4] + "h") and file_contents[j+1] == ((f"{address:#04x}")[4:6] + "h"):
              i = j
              print(f"Jumping to address {address}")
              jumped = True
              break
      if not jumped:
        raise InvalidAddress(f"Did not jump to address {address}")
    elif operation == "JZ":
      jumped: bool = False
      for j in range(len(file_contents) - 1):
          if file_contents[j] == ((f"{address:#04x}")[2:4] + "h") and file_contents[j+1] == ((f"{address:#04x}")[4:6] + "h") or file_contents[j] == ((f"{address:#04x}")[2:4] + "h") == "ffh":
            if accumulator == 0x00:
              i = j
              print(f"Not jumping since accumulator is 0x00")
            else:
              print(f"Jumping to address {address}")
            jumped = True
            break
      if not jumped:
        raise InvalidAddress(f"Address {address:#06x} was not found\nError on operation {line}")
    else:
        raise InvalidOpcode(f"{line} is an invalid opcode")
    
    print()
    input("Press enter to see updated ram")
    os.system('clear')
    render_mem_map_from_ram(ram)
  
  # final ram memory map
  os.system('clear')
  render_mem_map_from_ram(ram)

if __name__ == "__main__":
  main()