# Von Neumann Architecture Memory Emulation

## Project Overview

This project involves emulating the changing memory space (RAM) in a Von Neumann architected computer. Essentially, programs are written in one of many formats defined by a custom Instruction Set Architecture. There are pre-written programs, but once the main program is run, you can specify your program by its filename, and then watch as the program steps through each instruction in your program. Inspired by the book *CODE: The Hidden Language of Hardware and Software*.

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

*not ready to be run yet... but soon!*

### Contributing

Contributions are welcome! Please fork the repository and submit pull requests.

### License

This project is licensed under the MIT License.

