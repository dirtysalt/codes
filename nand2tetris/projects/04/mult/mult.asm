// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

// Put your code here.

// @5
// D=A
// @R0
// M=D
// @4
// D=A
// @R1
// M=D

@R2
M=0

@i
M=0

(LOOP)
@i
D=M
@R1
D=D-M
@STOP
D;JEQ // i == R1, break

// R2 += R0
@R0
D=M
@R2
M=D+M

// i += 1
@i
M=M+1
@LOOP
0;JMP

(STOP)
@STOP
0;JMP
