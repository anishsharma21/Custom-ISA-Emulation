from typing import TextIO

while True:
  file_name: str = str(input("Enter the file name: "))
  
  if file_name in ["exit", "quit", "q", "x"]:
    break
  elif not file_name.endswith == ".txt":
    file_name += ".txt"

  try:
    file: TextIO = open(f'./programs/{file_name}', 'r')
    contents: list[str] = file.readlines()
    contents = [s.removesuffix('\n') for s in contents if s != "\n" and s != ""]
    ram = {}
    meminput = False
    curAddress = 0x0000
    for line in contents:
      if line[-1] == ":":
        curAddress = int(line.removesuffix("h:"), 16)
        meminput = True
        ram[curAddress] = 0x00
      elif meminput:
        ram[curAddress] = int(line.removesuffix("h"), 16)
        curAddress += 1

    prevAddress = 0
    for address, value in ram.items():
      if prevAddress < address - 1:
        print("...")
      prevAddress = address
      print(f"{hex(address)}: {hex(value)}")

    file.close()
    break
  except FileNotFoundError:
    print("File not found")
    print()