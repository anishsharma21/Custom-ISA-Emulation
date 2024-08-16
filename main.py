from helpers import get_file_contents, render_memory, generate_mem_snapshot

while True:
  file_name: str = str(input("Enter the file name: ")).strip()
  
  if file_name in ["exit", "quit", "q", "x"]:
    break

  if not file_name.endswith(".txt"):  
    file_name += ".txt"

  content = get_file_contents(file_name)
  ram = generate_mem_snapshot(content)
  render_memory(ram)
  break