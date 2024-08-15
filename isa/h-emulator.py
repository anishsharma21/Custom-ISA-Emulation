from typing import TextIO

while True:
  file_name: str = str(input("Enter the file name: "))
  
  if file_name in ["exit", "quit", "q", "x"]:
    break
  elif not file_name.endswith == ".txt":
    file_name += ".txt"

  try:
    file: TextIO = open(f'../programs/{file_name}', 'r')
    print(file.read())
    file.close()
  except FileNotFoundError:
    print("File not found")
    print()