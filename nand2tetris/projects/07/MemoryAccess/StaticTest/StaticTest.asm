//===== ./MemoryAccess/StaticTest/StaticTest.vm =====
// L7: push constant 111
@111
D=A
@SP
AM=M+1
A=A-1
M=D
// L8: push constant 333
@333
D=A
@SP
AM=M+1
A=A-1
M=D
// L9: push constant 888
@888
D=A
@SP
AM=M+1
A=A-1
M=D
// L10: pop static 8
@SP
AM=M-1
D=M
@StaticTest.8
M=D
// L11: pop static 3
@SP
AM=M-1
D=M
@StaticTest.3
M=D
// L12: pop static 1
@SP
AM=M-1
D=M
@StaticTest.1
M=D
// L13: push static 3
@StaticTest.3
D=M
@SP
AM=M+1
A=A-1
M=D
// L14: push static 1
@StaticTest.1
D=M
@SP
AM=M+1
A=A-1
M=D
// L15: sub
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
// L16: push static 8
@StaticTest.8
D=M
@SP
AM=M+1
A=A-1
M=D
// L17: add
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
