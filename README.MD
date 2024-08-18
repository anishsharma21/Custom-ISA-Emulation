# Memory Map Emulator

## Project Overview

Have you ever wondered what it means to 'run' a program? What goes on under the hood? What did the first programs look like visually?

Well, in this project, you can write machine code and watch your program run visually in memory (emulated).

In more technical terms, this project involves emulating the changing memory map (RAM) in a Von Neumann-architected computer as it runs a program, i.e. it shows what happens in a simple computer when a simple (or complex) program is run. Programs are written in a defined format and adhere to a custom Instruction Set Architecture (ISA). When the main program (written in Python) is run, you can specify a program for emulation by its file name and then step forward by pressing `enter`, seeing the operations being performed, a description of each step, and, of course, a map of the memory as it changes over time.

This project is inspired by the incredible book *CODE: The Hidden Language of Hardware and Software*. A must-read for anyone who wants to know how computers really work from the ground up - it's completely beginner-friendly, with no previous knowledge required, and takes you from mere 1s and 0s all the way to building your own computer.

### How do I run it?

Open your terminal and run the following command:

```bash
git clone https://github.com/anishsharma21/Memory-Map-Emulator
```

Then, in the same directory, run the following command:

```bash
python3 main.py
```

You'll be prompted with:

```plaintext
Enter the file name: 
```

There are many pre-written programs you can run and can be found in the `programs` directory. You can type in the full filename, like `p1.txt` or you can just type in `p1`. This way, you don't need to specify the extension, you can simply write the name of your file. 

You can also add your own programs to the `programs` directory. Programs must be written with the `.txt` extension.

P.S. `p7.txt` is pretty interesting to run 👀

If you don't have [python3](https://www.python.org/downloads/) installed, go to this link to install it.

## ISA Specification

### Instruction Set Architecture

| Operation            | Code | Mnemonic |
|----------------------|------|----------|
| Load                 | 10h  | LOD      |
| Store                | 11h  | STO      |
| Add                  | 20h  | ADD      |
| Subtract             | 21h  | SUB      |
| Add with Carry       | 22h  | ADC      |
| Subtract with Borrow | 23h  | SBB      |
| Jump                 | 30h  | JMP      |
| Jump if Zero         | 31h  | JZ       |
| Jump if Carry        | 32h  | JC       |
| Jump if Not Zero     | 33h  | JNZ      |
| Jump if Not Carry    | 34h  | JNC      |
| Halt                 | FFh  | HLT      |

- **A**: Accumulator
- **Memory Range**: [0000h - FFFFh] (64KB memory, 16-bit addresses)

### Machine Code Format

Each program consists of memory address declarations, and memory inputs that follow. 

```plaintext
[ADDRESS]:
##h
##h
```

You declare a memory address, and then bytes that you want to input to create your program.

Further details about creating your own programs can be found in `documentation/isa-raw-format.txt`.

**Endianness**: Big-endian (high-byte stored in lower address)

## Example Program

Here is a simple program that adds 2 numbers together:

```plaintext
0000h:
10h
10h
00h

20h
10h
01h

11h
10h
02h

FFh

1000h:
01h
01h
00h
```

In the above program, the line `0000h` indicates that from here onwards, each newline will correspond to a byte of data the will need to be inputted into memory. In this case, you can see the bytes being inputted in sequences of 3. These are instructions - the first byte is the instruction opcode (see above for the list of opcodes) and the next 2 relate to a 16-bit address in memory. You don't need to add new lines between each instruction sequence, but it makes it easier to read and distinguish between 'instruction code' and 'data'. The memory declared after `0000h` is declared as instructions to be run, while memory after `1000h` is used by the program as memory to be accessed.

This program can be run by choosing `p1.txt` (or just `p1`) as the file when running the main program.

### Description

The program above loads the value at memory `1000h`, then adds the value at memory location `1001h`. It then stores the current accumulator value at address `1002h` before halting.

### Emulation Goals

- `Real-Time Memory Display`: The Python program will display the entire memory set in the terminal, updating in real-time with each instruction cycle.
- `Instruction Highlighting`: Each instruction will be highlighted as the program progresses to show what is happening at each step.

### Contributing

Contributions are welcome! Please fork the repository and submit pull requests.

### License

This project is licensed under the MIT License.

