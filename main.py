from typing import Tuple
from helpers import get_file_contents, file_contents_to_instructions

def main():
  while True:
    file_name: str = str(input("Enter the file name: ")).strip()
    
    if file_name in ["exit", "quit", "q", "x"]:
      break

    if not file_name.endswith(".txt"):  
      file_name += ".txt"

    memcontent: list[str] = get_file_contents(file_name)
    instructions: list[Tuple[str, int]] = file_contents_to_instructions(memcontent)
    break

if __name__ == "__main__":
  main()