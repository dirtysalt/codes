//===== ./MemoryAccess/BasicTest/BasicTest.vm =====
// L7: push constant 10
@10
D=A
@SP
AM=M+1
A=A-1
M=D
// L8: pop local 0
@SP
AM=M-1
D=M
@LCL
A=M
M=D
// L9: push constant 21
@21
D=A
@SP
AM=M+1
A=A-1
M=D
// L10: push constant 22
@22
D=A
@SP
AM=M+1
A=A-1
M=D
// L11: pop argument 2
@ARG
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
// L12: pop argument 1
@SP
AM=M-1
D=M
@ARG
A=M+1
M=D
// L13: push constant 36
@36
D=A
@SP
AM=M+1
A=A-1
M=D
// L14: pop this 6
@THIS
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
// L15: push constant 42
@42
D=A
@SP
AM=M+1
A=A-1
M=D
// L16: push constant 45
@45
D=A
@SP
AM=M+1
A=A-1
M=D
// L17: pop that 5
@THAT
D=M
@5
D=D+A
@R13
M=D
@SP
AM=M-1
D=M
@R13
A=M
M=D
// L18: pop that 2
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
// L19: push constant 510
@510
D=A
@SP
AM=M+1
A=A-1
M=D
// L20: pop temp 6
@SP
AM=M-1
D=M
@R11
M=D
// L21: push local 0
@LCL
A=M
D=M
@SP
AM=M+1
A=A-1
M=D
// L22: push that 5
@THAT
D=M
@5
A=D+A
D=M
@SP
AM=M+1
A=A-1
M=D
// L23: add
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
// L24: push argument 1
@ARG
A=M+1
D=M
@SP
AM=M+1
A=A-1
M=D
// L25: sub
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
// L26: push this 6
@THIS
D=M
@6
A=D+A
D=M
@SP
AM=M+1
A=A-1
M=D
// L27: push this 6
@THIS
D=M
@6
A=D+A
D=M
@SP
AM=M+1
A=A-1
M=D
// L28: add
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
// L29: sub
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
// L30: push temp 6
@R11
D=M
@SP
AM=M+1
A=A-1
M=D
// L31: add
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
