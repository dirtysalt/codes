// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed.
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.

(KB_START)

// last kb code
@last_kb
M=1

// fill_v = 0 or -1
@fill_v
M=0

// n = 8192
@8192
D=A
@n
M=D

(KB_LOOP)

// compare with last kb
@KBD
D=M
@last_kb
D=D-M
@KB_LOOP
D;JEQ

// save last kb
@KBD
D=M
@last_kb
M=D

@SET_WHITE
D;JEQ
// set black
@fill_v
M=-1
@FS_START
0;JMP
(SET_WHITE)
@fill_v
M=0
@FS_START
0;JMP


(FS_START)

// i = 0
@i
M=0

(FS_LOOP)
// i >= n, goto FS_STOP
@i
D=M
@n
D=D-M
@FS_STOP
D;JGE

// set screen[i] = v
@i
D=M
@SCREEN
D=D+A // screen[i]
@addr
M=D
@fill_v
D=M
@addr
A=M
M=D

// i+=1
@i
M=M+1
@FS_LOOP
0;JMP

(FS_STOP)
@KB_LOOP
0;JMP
