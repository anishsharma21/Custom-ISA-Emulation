# Memory Map Emulation

## Project Overview

Have you ever wondered what it means to 'run' a program? What goes on under the hood? What did the first programs look like visually?

This project involves emulating the changing memory map (RAM) in a Von Neumann architected computer as it runs a program, i.e. it shows what happening in a simple computer when a simple (or complex) program is run. Programs are written in a defined format and adhere to a custom Instruction Set Architecture (ISA). When the main program (written in Python) is run, you can specify a program for emulation by its file name, and then step forwards and backwards through the program lifecycle with the `f` and `b` keys.

This project is inspired by the incredible book *CODE: The Hidden Language of Hardware and Software*. A must read for anyone who wants to know how computers really work - completely beginner friendly, no previous knowledge required, and takes you from mere 1's and 0's all the way to building your own computer.

## ISA Specification

### Instruction Set Architecture for Relay-Powered Von Neumann Architecture

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

### Operation Format

- **ISA Format**: `[MNEMONIC] [DESTINATION].[SOURCE]`
- **Machine Language Format**: 
  - `[ADDRESS]: [OPCODE]`
  - `[ADDRESS]: [HIGH-BYTE]`
  - `[ADDRESS]: [LOW-BYTE]`

- **Endianness**: Big-endian (high-byte stored in lower address)

## Example Program

### Description

This program loads the value at memory `0021h`, then adds the value at memory location `0023h`. It then stores the current accumulator value at address `0025h`. Next, it loads the value at address `0020h`, adds the value at address `0022h`, and stores the current accumulator value at address `0024h` before halting.

### Machine Language Instructions

```plaintext
0000h: 10h 00h 21h
0003h: 20h 00h 23h
0006h: 11h 00h 25h
0009h: 10h 00h 20h
000Ch: 22h 00h 22h
000Fh: 11h 00h 24h
0012h: FFh
```

### Emulation Goals

- `Real-Time Memory Display`: The Python program will display the entire memory set in the terminal, updating in real-time with each instruction cycle.
- `Instruction Highlighting`: Each address will be highlighted as the program progresses to show what is happening at each step.
- `Format Flexibility`: The program will support both my custom ISA and machine language formats for input instructions.

### How do I run it?

Download the code. Open your terminal and use the commands `ls` and `cd` to list the directories (folders) contents, and change directories until you are in the directory where the `main.py` file exists. Then, run the following command:

```python
python3 main.py
```

You'll be prompted with:

```plaintext
Enter the file name: 
```

`p1` and `p2` are pre-written programs which you can type in and choose, or you can add your own program file to the `programs` directory. You don't need to specify the extension, you can simply write the name of your file. Programs should however be written with the `.txt` extension.

If you don't have [python3](https://www.python.org/downloads/) installed, go to this link to install it.

### Contributing

Contributions are welcome! Please fork the repository and submit pull requests.

### License

This project is licensed under the MIT License.

