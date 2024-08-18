import os
from typing import List
from helpers import get_file_contents, get_ram_from_mem_contents, find_operation_from_opcode, render_mem_map_from_ram
from exceptions import InvalidOpcode, InvalidAddress

# ANSI escape codes for background colors
BG_YELLOW = "\033[43m"
BG_BLUE = "\033[44m"
BG_ORANGE = "\033[48;5;202m"
RESET = "\033[0m"

def main():
  file_name: str = str(input("Enter the file name: ")).strip()
  
  if file_name in ["exit", "quit", "q", "x"]:
    return

  file_contents: List[str] = get_file_contents(file_name)
  ram: dict[int, List[int]] = get_ram_from_mem_contents(file_contents)
  index: int = 0
  
  os.system('clear')
  print(f"\033[38;5;27mInstruction 0\033[0m")
  print()
  print("-" * 10)
  render_mem_map_from_ram(ram)
  print("-" * 10)

  accumulator: int = 0x0000
  
  while index < len(file_contents):
    line: str = file_contents[index]
    if line[-1] == ":" or line[0] == ";": # skip memory address declaration or comments
      index += 1
      continue
    if line == "FFh": # HLT
      break
    # assuming instructions are written correctly in 3 byte sequences
    opcode: int = int(line.removesuffix("h"), 16)
    operation: str = find_operation_from_opcode(opcode)
    address: int = int(file_contents[index+1].removesuffix("h") + file_contents[index+2].removesuffix("h"), 16)
    index += 3

    print()

    print(f"Accumulator value: {accumulator:#04x}")
    
    if address not in ram:
      ram[address] = [0x00]

    if operation == "LOD":
      print(f"{BG_YELLOW}Loading {ram[address][0]:#04x} value from {address:#06x} into accumulator{RESET}")
      accumulator = ram[address][0]
    elif operation == "STO":
      print(f"{BG_YELLOW}Storing {accumulator:#04x} value from accumulator into address {address:#06x} ({ram[address][0]:#04x}){RESET}")
      ram[address][0] = accumulator
    elif operation == "ADD":
      print(f"{BG_YELLOW}Adding {ram[address][0]:#04x} value from {address:#06x} into accumulator{RESET}")
      accumulator += ram[address][0]
    elif operation == "SUB":
      print(f"{BG_YELLOW}Subtracting {ram[address][0]:#04x} value from {address:#06x} from accumulator{RESET}")
      accumulator -= ram[address][0]
    elif operation == "JMP":
      # not implemented
      pass
    elif operation == "JZ":
      try:
        jmp_index: int = ram[address][1]
      except IndexError:
        raise InvalidAddress(f"Value {ram[address][0]} is not declared in original file and cannot be jumped to\nError at address {address}\nError on operation {line}")
      
      if accumulator == 0x00:
        print(f"{BG_ORANGE}Not jumping since accumulator is 0x00{RESET}")
      else:
        index = jmp_index
        print(f"{BG_ORANGE}Jumping to address {int(file_contents[jmp_index].removesuffix("h:"), 16):#06x}{RESET}")

    else:
        raise InvalidOpcode(f"{line} is an invalid opcode")
    
    print()
    input("Press enter to see updated ram")
    os.system('clear')
    print(f"\033[38;5;27mInstruction {(index - 1) // 3 if index > 0 else 0}\033[0m")
    print()
    print("-" * 10)
    render_mem_map_from_ram(ram)
    print("-" * 10)
  
  # final ram memory map
  os.system('clear')
  print(f"\033[38;5;27mFinal Memory Map of RAM\033[0m")
  print()
  print("-" * 10)
  render_mem_map_from_ram(ram)
  print("-" * 10)
  print()

if __name__ == "__main__":
  main()