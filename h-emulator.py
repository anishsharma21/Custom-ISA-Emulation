while True:
  file_name: str = str(input("Enter the file name: ")).strip()
  
  if file_name in ["exit", "quit", "q", "x"]:
    break

  if not file_name.endswith(".txt"):  
    file_name += ".txt"

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

  contents = [s.strip() for s in contents if s.strip()]
  
  ram = {}
  curAddress = 0x0000
  for line in contents:
    if line[-1] == ":":
      curAddress = int(line.removesuffix("h:"), 16)
      ram[curAddress] = 0x00
    elif curAddress in ram:
      curAddress += 1
      ram[curAddress] = int(line.removesuffix("h"), 16)

  prevAddress = 0
  for address, value in ram.items():
    if prevAddress < address - 1:
      print("...")
    prevAddress = address
    print(f"{address:#06x}: {value:#06x}")

  break