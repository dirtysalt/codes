//===== ProgramFlow/BasicLoop/BasicLoop.vm =====
// L9: push constant 0
@SP
AM=M+1
A=A-1
M=0
// L10: pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// L11: label LOOP_START
(LOOP_START)
// L12: push argument 0
@ARG
A=M
D=M
@SP
AM=M+1
A=A-1
M=D
// L13: push local 0
@LCL
A=M
D=M
@SP
AM=M+1
A=A-1
M=D
// L14: add
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
// L15: pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// L16: push argument 0
@ARG
A=M
D=M
@SP
AM=M+1
A=A-1
M=D
// L17: push constant 1
@SP
AM=M+1
A=A-1
M=1
// L18: sub
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
// L19: pop argument 0
@SP
AM=M-1
D=M
@ARG
A=M
M=D
// L20: push argument 0
@ARG
A=M
D=M
@SP
AM=M+1
A=A-1
M=D
// L21: if-goto LOOP_START
@SP
AM=M-1
D=M
@LOOP_START
D;JNE
// L22: push local 0
@LCL
A=M
D=M
@SP
AM=M+1
A=A-1
M=D
