# Hack Assembler

This is a Python implementation for the Hack Assembler, an assembler for the Hack Machine Language built for the [nand2tetris)](https://www.nand2tetris.org/) course.

### Usage Guide
Run the Assembler with a valid `.asm` file by using the following command:

```
  python src/Main.py --source path/to/file
```

The assembler will output a `.hack` file inside your directory. You can upload this machine code file inside your Hack Computer implementation or in the CPU Emulator provided in the nand2tetris website.

The `/tests` folder contains valid `.asm` test files from **nand2tetris** that you can use to test the assembler.
