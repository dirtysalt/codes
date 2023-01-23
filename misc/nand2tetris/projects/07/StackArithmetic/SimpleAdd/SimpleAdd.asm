//===== ./StackArithmetic/SimpleAdd/SimpleAdd.vm =====
// L7: push constant 7
@7
D=A
@SP
AM=M+1
A=A-1
M=D
// L8: push constant 8
@8
D=A
@SP
AM=M+1
A=A-1
M=D
// L9: add
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
