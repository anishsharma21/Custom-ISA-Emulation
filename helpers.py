### Utilities ###

def get_file_contents(file_name: str) -> list[str]:
  contents: list[str] = []
  
  try:
    with open(f'./programs/{file_name}', 'r') as file:
      contents: list[str] = file.readlines()
  except FileNotFoundError:
    print("File not found")
    print()
  except Exception as e:
    print(f"Error: {e}")
    print()

  return [s.strip() for s in contents if s.strip()]

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

def run_program(init_ram: dict[int, int]) -> None:
  instructions: list[list[str | int]] = [[]]
  for _, value in init_ram.items():
    cur_instruction_length = len(instructions[-1])
    if cur_instruction_length == 0:
      instructions[-1][cur_instruction_length] = find_operation_from_opcode(value)
    elif cur_instruction_length in [1, 2]:
      instructions[-1][cur_instruction_length] = value

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