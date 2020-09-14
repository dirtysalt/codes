//===== FunctionCalls/SimpleFunction/SimpleFunction.vm =====
// L7: function SimpleFunction.test 2
(SimpleFunction.test)
@SP
A=M
M=0
A=A+1
M=0
A=A+1
D=A
@SP
M=D
// L8: push local 0
@LCL
A=M
D=M
@SP
AM=M+1
A=A-1
M=D
// L9: push local 1
@LCL
A=M+1
D=M
@SP
AM=M+1
A=A-1
M=D
// L10: add
@SimpleFunction.test$lbl0
D=A
@R14
M=D
@ARITH_OP_ADD
0;JMP
(SimpleFunction.test$lbl0)
// L11: not
@SimpleFunction.test$lbl1
D=A
@R14
M=D
@ARITH_OP_NOT
0;JMP
(SimpleFunction.test$lbl1)
// L12: push argument 0
@ARG
A=M
D=M
@SP
AM=M+1
A=A-1
M=D
// L13: add
@SimpleFunction.test$lbl2
D=A
@R14
M=D
@ARITH_OP_ADD
0;JMP
(SimpleFunction.test$lbl2)
// L14: push argument 1
@ARG
A=M+1
D=M
@SP
AM=M+1
A=A-1
M=D
// L15: sub
@SimpleFunction.test$lbl3
D=A
@R14
M=D
@ARITH_OP_SUB
0;JMP
(SimpleFunction.test$lbl3)
// L16: return
@RETURN_POP_CODE
0;JMP
(CALL_PUSH_CODE)
@SP
AM=M+1
A=A-1
M=D
@LCL
D=M
@SP
AM=M+1
A=A-1
M=D
@ARG
D=M
@SP
AM=M+1
A=A-1
M=D
@THIS
D=M
@SP
AM=M+1
A=A-1
M=D
@THAT
D=M
@SP
AM=M+1
A=A-1
M=D
@SP
D=M
@LCL
M=D
@SP
D=M
@R13
D=D-M
@ARG
M=D
@R14
A=M
0;JMP
@R15
A=M
0;JMP
(RETURN_POP_CODE)
@LCL
D=M
@5
A=D-A
D=M
@R14
M=D
@SP
AM=M-1
D=M
@ARG
A=M
M=D
@ARG
D=M+1
@SP
M=D
@LCL
D=M
@R13
AM=D-1
D=M
@THAT
M=D
@R13
AM=M-1
D=M
@THIS
M=D
@R13
AM=M-1
D=M
@ARG
M=D
@R13
AM=M-1
D=M
@LCL
M=D
@R14
A=M
0;JMP
(ARITH_OP_ADD)
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
@R14
A=M
0;JMP
(ARITH_OP_NOT)
@SP
AM=M-1
D=M
D=!D
@SP
AM=M+1
A=A-1
M=D
@R14
A=M
0;JMP
(ARITH_OP_NEG)
@SP
AM=M-1
D=M
D=-D
@SP
AM=M+1
A=A-1
M=D
@R14
A=M
0;JMP
(ARITH_OP_SUB)
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
@R14
A=M
0;JMP
(ARITH_OP_GT)
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
@GLOBAL$lbl0.true
D;JGT
D=0
@GLOBAL$lbl0.ok
0;JMP
(GLOBAL$lbl0.true)
D=-1
(GLOBAL$lbl0.ok)
@SP
AM=M+1
A=A-1
M=D
@R14
A=M
0;JMP
(ARITH_OP_OR)
@SP
AM=M-1
D=M
@R13
M=D
@SP
AM=M-1
D=M
@R13
D=D|M
@SP
AM=M+1
A=A-1
M=D
@R14
A=M
0;JMP
(ARITH_OP_LT)
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
@GLOBAL$lbl1.true
D;JLT
D=0
@GLOBAL$lbl1.ok
0;JMP
(GLOBAL$lbl1.true)
D=-1
(GLOBAL$lbl1.ok)
@SP
AM=M+1
A=A-1
M=D
@R14
A=M
0;JMP
(ARITH_OP_AND)
@SP
AM=M-1
D=M
@R13
M=D
@SP
AM=M-1
D=M
@R13
D=D&M
@SP
AM=M+1
A=A-1
M=D
@R14
A=M
0;JMP
(ARITH_OP_EQ)
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
@GLOBAL$lbl2.true
D;JEQ
D=0
@GLOBAL$lbl2.ok
0;JMP
(GLOBAL$lbl2.true)
D=-1
(GLOBAL$lbl2.ok)
@SP
AM=M+1
A=A-1
M=D
@R14
A=M
0;JMP
