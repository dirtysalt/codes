//===== ./MemoryAccess/PointerTest/PointerTest.vm =====
// L8: push constant 3030
@3030
D=A
@SP
AM=M+1
A=A-1
M=D
// L9: pop pointer 0
@SP
AM=M-1
D=M
@THIS
M=D
// L10: push constant 3040
@3040
D=A
@SP
AM=M+1
A=A-1
M=D
// L11: pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
// L12: push constant 32
@32
D=A
@SP
AM=M+1
A=A-1
M=D
// L13: pop this 2
@THIS
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
// L14: push constant 46
@46
D=A
@SP
AM=M+1
A=A-1
M=D
// L15: pop that 6
@THAT
D=M
@6
D=D+A
@R13
M=D
@SP
AM=M-1
D=M
@R13
A=M
M=D
// L16: push pointer 0
@THIS
D=M
@SP
AM=M+1
A=A-1
M=D
// L17: push pointer 1
@THAT
D=M
@SP
AM=M+1
A=A-1
M=D
// L18: add
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
// L19: push this 2
@THIS
D=M
@2
A=D+A
D=M
@SP
AM=M+1
A=A-1
M=D
// L20: sub
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
// L21: push that 6
@THAT
D=M
@6
A=D+A
D=M
@SP
AM=M+1
A=A-1
M=D
// L22: add
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
