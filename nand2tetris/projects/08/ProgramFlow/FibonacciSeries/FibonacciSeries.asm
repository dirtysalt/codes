//===== ProgramFlow/FibonacciSeries/FibonacciSeries.vm =====
// L11: push argument 1
@ARG
A=M+1
D=M
@SP
AM=M+1
A=A-1
M=D
// L12: pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// L14: push constant 0
@SP
AM=M+1
A=A-1
M=0
// L15: pop that 0
@SP
AM=M-1
D=M
@THAT
A=M
M=D
// L16: push constant 1
@SP
AM=M+1
A=A-1
M=1
// L17: pop that 1
@SP
AM=M-1
D=M
@THAT
A=M+1
M=D
// L19: push argument 0
@ARG
A=M
D=M
@SP
AM=M+1
A=A-1
M=D
// L20: push constant 2
@2
D=A
@SP
AM=M+1
A=A-1
M=D
// L21: sub
@SP
AM=M-1
D=M
@R13
M=D
@SP
AM=M-1
D=M
@R13
D=D-M
@SP
AM=M+1
A=A-1
M=D
// L22: pop argument 0
@SP
AM=M-1
D=M
@ARG
A=M
M=D
// L24: label MAIN_LOOP_START
(MAIN_LOOP_START)
// L26: push argument 0
@ARG
A=M
D=M
@SP
AM=M+1
A=A-1
M=D
// L27: if-goto COMPUTE_ELEMENT
@SP
AM=M-1
D=M
@COMPUTE_ELEMENT
D;JNE
// L28: goto END_PROGRAM
@END_PROGRAM
0;JMP
// L30: label COMPUTE_ELEMENT
(COMPUTE_ELEMENT)
// L32: push that 0
@THAT
A=M
D=M
@SP
AM=M+1
A=A-1
M=D
// L33: push that 1
@THAT
A=M+1
D=M
@SP
AM=M+1
A=A-1
M=D
// L34: add
@SP
AM=M-1
D=M
@R13
M=D
@SP
AM=M-1
D=M
@R13
D=D+M
@SP
AM=M+1
A=A-1
M=D
// L35: pop that 2
@THAT
D=M
@2
D=D+A
@R13
M=D
@SP
AM=M-1
D=M
@R13
A=M
M=D
// L37: push pointer 1
@THAT
D=M
@SP
AM=M+1
A=A-1
M=D
// L38: push constant 1
@SP
AM=M+1
A=A-1
M=1
// L39: add
@SP
AM=M-1
D=M
@R13
M=D
@SP
AM=M-1
D=M
@R13
D=D+M
@SP
AM=M+1
A=A-1
M=D
// L40: pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// L42: push argument 0
@ARG
A=M
D=M
@SP
AM=M+1
A=A-1
M=D
// L43: push constant 1
@SP
AM=M+1
A=A-1
M=1
// L44: sub
@SP
AM=M-1
D=M
@R13
M=D
@SP
AM=M-1
D=M
@R13
D=D-M
@SP
AM=M+1
A=A-1
M=D
// L45: pop argument 0
@SP
AM=M-1
D=M
@ARG
A=M
M=D
// L47: goto MAIN_LOOP_START
@MAIN_LOOP_START
0;JMP
// L49: label END_PROGRAM
(END_PROGRAM)
