### Utilities ###

def get_file_contents(file_name: str) -> list:
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

def render_memory(ram: dict):
  prevAddress = 0
  for address, value in ram.items():
    if prevAddress < address - 1:
      print("...")
    prevAddress = address
    print(f"{address:#06x}: {value:#04x}")

def generate_mem_snapshot(file_contents: list[str]) -> dict:
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

def run_program(init_ram: dict) -> dict:
  return {}