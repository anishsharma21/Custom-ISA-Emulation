from typing import Tuple
from helpers import get_file_contents, file_contents_to_instructions

def main():
  file_name: str = str(input("Enter the file name: ")).strip()
  
  if file_name in ["exit", "quit", "q", "x"]:
    return

  file_contents: list[str] = get_file_contents(file_name)
  instructions: list[Tuple[str, int]] = file_contents_to_instructions(file_contents)
  print(instructions)

if __name__ == "__main__":
  main()