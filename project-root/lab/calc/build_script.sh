#!/bin/bash
# Assemble the ARM files
clang -c src/main/main.asm -o main.o
clang -c src/features/math/shared/add.asm -o add.o

# Link the object files, specifying the entry point as _start
clang -o demo main.o add.o -e _start
