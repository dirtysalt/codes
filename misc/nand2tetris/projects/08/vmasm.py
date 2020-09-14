#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
import os


class Parser:
    def __init__(self):
        pass

    def parse_line(self, x, loc):
        x = x.strip()
        p = x.find('//')
        if p != -1:
            x = x[:p].strip()
        if not x:
            return None
        ss = x.split(' ')
        type = ss[0]
        arg1 = ss[1] if len(ss) >= 2 else None
        arg2 = ss[2] if len(ss) >= 3 else None
        inst = Inst(x, loc, type, arg1, arg2)
        return inst

    def parse_lines(self, lines):
        insts = []
        loc = 0
        for x in lines:
            loc += 1
            inst = self.parse_line(x, loc)
            if not inst:
                continue
            insts.append(inst)
        return insts


C_ARITH = "arith"
C_PUSH = "push"
C_POP = "pop"
C_LABEL = "label"
C_GOTO = "goto"
C_IF_GOTO = "if-goto"
C_FUNC = "function"
C_RET = "return"
C_CALL = "call"

SEG_TO_BASE_REG = {
    'argument': 'ARG',
    'local': 'LCL',
    'this': 'THIS',
    'that': 'THAT'
}


def is_comment(x):
    # special comment.
    if x.startswith('//#'):
        return False
    if x.startswith('//'):
        return True
    return False


def text_to_codes(text):
    ss = text.split('\n')
    ss = list(filter(lambda x: x and not is_comment(x),
                     map(lambda x: x.strip(), ss)))
    return ss


class CodeGenContext:
    def __init__(self, init_code, remove_unused_fn, compact_size):
        self.init_code = init_code
        self.global_label = 0
        self.file_path = None
        self.file_ns = 0
        self.func_name = None
        self.func_label = 0
        self.remove_unused_fn = remove_unused_fn
        self.used_fn = set()
        self.output_enabled = True
        self.compact_size = compact_size

    def add_used_fn(self, name):
        self.used_fn.add(name)

    def set_file_path(self, file_path):
        self.file_path = file_path
        self.file_ns = os.path.splitext(os.path.basename(file_path))[0]

    def gen_label(self, name=None):
        if self.func_name:
            if name:
                s = '{}${}'.format(self.func_name, name)
            else:
                s = '{}$lbl{}'.format(self.func_name, self.func_label)
                self.func_label += 1
        else:
            if name:
                s = name
            else:
                s = 'GLOBAL$lbl{}'.format(self.global_label)
                self.global_label += 1
        return s

    def enter_func(self, func_name):
        self.func_name = func_name
        self.func_label = 0
        if self.remove_unused_fn and func_name not in self.used_fn:
            self.output_enabled = False
        else:
            self.output_enabled = True

    def exit_func(self):
        self.func_name = None
        self.func_label = 0


CALL_PUSH_TEXT = """
    // return address in D
    @SP
    AM=M+1
    A=A-1
    M=D
    // push local.
    @LCL
    D=M
    @SP
    AM=M+1
    A=A-1
    M=D
    // push argument.
    @ARG
    D=M
    @SP
    AM=M+1
    A=A-1
    M=D
    // push this
    @THIS
    D=M
    @SP
    AM=M+1
    A=A-1
    M=D
    // push that
    @THAT
    D=M
    @SP
    AM=M+1
    A=A-1
    M=D
    // lcl = sp
    @SP
    D=M
    @LCL
    M=D
    // arg = sp - stack_size
    @SP
    D=M
    // stack size in R13
    @R13
    D=D-M
    @ARG
    M=D
    // jump address in R14
    @R14
    A=M
    0;JMP
"""

RETURN_POP_TEXT = """
   // return address in R14
   @LCL
   D=M
   @5
   A=D-A
   D=M
   @R14
   M=D
   // pop to *arg
   @SP
   AM=M-1
   D=M
   @ARG
   A=M
   M=D
   // sp = arg + 1
   @ARG
   D=M+1
   @SP
   M=D
   @LCL
   D=M
   // restore that
   @R13
   AM=D-1
   D=M
   @THAT
   M=D
   // restore this
   @R13
   AM=M-1
   D=M
   @THIS
   M=D
   // restore arg
   @R13
   AM=M-1
   D=M
   @ARG
   M=D
   // restore lcl
   @R13
   AM=M-1
   D=M
   @LCL
   M=D
   // goto return
   @R14
   A=M
   0;JMP
   """

ARITH_OPS = {'add', 'sub', 'neg', 'eq', 'gt', 'lt', 'and', 'or', 'not'}


class CodeGen:
    def __init__(self):
        self.codes = []

    def gen_codes(self, insts, ctx: CodeGenContext):
        codes = self.codes
        codes.append("//===== {} =====\n\n".format(ctx.file_path))
        for inst in insts:
            codes.extend(inst.emit_with_comment(ctx))

    def gen_init(self, ctx: CodeGenContext):
        ctx.add_used_fn('Main.main')
        if ctx.init_code:
            # 这里其实也可以直接跳转到Sys.init，但是SP就要设置成为261.
            text = """
            @256
            D=A
            @SP
            M=D
            """
            self.codes.extend(text_to_codes(text))
            self.codes.extend(emit_call('Sys.init', 0, ctx))
            ctx.add_used_fn('Sys.init')

    def gen_fini(self, ctx: CodeGenContext):
        ctx.exit_func()
        if ctx.compact_size:
            text = """
            // call subroutine
            (CALL_PUSH_CODE)
            {call_push_text}
            // r15 as address.
            @R15
            A=M
            0;JMP
            // return subroutine
            (RETURN_POP_CODE)
            {return_pop_text}
            """.format(return_pop_text=RETURN_POP_TEXT, call_push_text=CALL_PUSH_TEXT)
            self.codes.extend(text_to_codes(text))

            # disable compact code size temporarily
            ctx.compact_size = False
            for op in ARITH_OPS:
                op_upper = op.upper()
                text = f"""
                (ARITH_OP_{op_upper})
                """
                self.codes.extend(text_to_codes(text))
                self.codes.extend(emit_arith(op, ctx))
                text = """
                @R14
                A=M
                0;JMP
                """
                self.codes.extend(text_to_codes(text))
            ctx.compact_size = True


def emit_push(seg, index, ctx: CodeGenContext):
    src = 'D'
    # load to D register first.
    if seg in SEG_TO_BASE_REG:
        br = SEG_TO_BASE_REG[seg]
        # NOTE: optimization. index = 0 or 1
        if index == 0:
            text = """
            @{br}
            A=M
            D=M
            """.format(br=br)
        elif index == 1:
            text = """
            @{br}
            A=M+1
            D=M
            """.format(br=br)
        else:
            text = """
            @{br}
            D=M
            @{index}
            A=D+A
            D=M
            """.format(br=br, index=index)
    elif seg == 'constant':
        if index in (0, 1):
            src = index
            text = ""
        else:
            text = """
            @{index}
            D=A
            """.format(index=index)
    elif seg == 'static':
        text = """
        @{namespace}.{index}
        D=M
        """.format(namespace=ctx.file_ns, index=index)
    elif seg == 'pointer':
        br = 'THIS' if index == 0 else 'THAT'
        text = """
        @{br}
        D=M
        """.format(br=br)
    elif seg == 'temp':
        index = index + 5
        text = """
        @R{index}
        D=M
        """.format(index=index)
    else:
        raise RuntimeError('unknown seg = {}'.format(seg))

    # save D register to *SP and SP++
    text += f"""
    // *sp=d, sp++
    @SP
    AM=M+1
    A=A-1
    M={src}
    """
    codes = text_to_codes(text)
    return codes


def emit_pop(seg, index, ctx: CodeGenContext):
    # SP-- and load *SP to D
    load_text = """
    // sp--, d=*sp
    @SP
    AM=M-1
    D=M
    """

    if seg in SEG_TO_BASE_REG:
        br = SEG_TO_BASE_REG[seg]
        # NOTE: optimization. index = 0 or 1
        # 这里因为跨度比较大，所以不太好写成局部规则

        if index == 0:
            text = load_text + """
            @{br}
            A=M
            M=D
            """.format(br=br)
        elif index == 1:
            text = load_text + """
            @{br}
            A=M+1
            M=D
            """.format(br=br)
        else:
            text = """
            @{br}
            D=M
            @{index}
            D=D+A
            @R13
            M=D
            """ + load_text + """
            @R13
            A=M
            M=D
            """
            text = text.format(br=br, index=index)
        return text_to_codes(text)

    elif seg == 'static':
        text = """
        @{namespace}.{index}
        M=D
        """.format(namespace=ctx.file_ns, index=index)

    elif seg == 'pointer':
        br = 'THIS' if index == 0 else 'THAT'
        text = """
        @{br}
        M=D
        """.format(br=br)

    elif seg == 'temp':
        index = index + 5
        text = """
        @R{index}
        M=D
        """.format(index=index)

    else:
        raise RuntimeError('unknown seg = {}'.format(seg))

    text = load_text + text
    codes = text_to_codes(text)
    return codes


def emit_arith(op, ctx: CodeGenContext):
    if ctx.compact_size:
        return_label = ctx.gen_label()
        jump_label = 'ARITH_OP_{}'.format(op.upper())
        text = f"""
        @{return_label}
        D=A
        @R14
        M=D
        @{jump_label}
        0;JMP
        ({return_label})
        """
        return text_to_codes(text)

    def pop_d():
        s = """
        @SP
        AM=M-1
        D=M
        """
        return s

    def push_d():
        s = """
        @SP
        AM=M+1
        A=A-1
        M=D
        """
        return s

    if op == 'add':
        text = pop_d() + """
        @R13
        M=D
        """ + pop_d() + """
        @R13
        D=D+M
        """ + push_d()

    elif op == 'sub':
        text = pop_d() + """
        @R13
        M=D
        """ + pop_d() + """
        @R13
        D=D-M
        """ + push_d()

    elif op in ('eq', 'gt', 'lt'):
        lbl = ctx.gen_label()
        lbl_ok = lbl + '.ok'
        lbl_true = lbl + '.true'

        if op == 'eq':
            jmp = 'JEQ'
        elif op == 'gt':
            jmp = 'JGT'
        elif op == 'lt':
            jmp = 'JLT'

        text = pop_d() + """
        @R13
        M=D        
        """ + pop_d() + """
        @R13
        D=D-M
        @{lbl_true}
        D;{jmp}
        D=0
        @{lbl_ok}
        0;JMP
        ({lbl_true})
        D=-1
        ({lbl_ok})
        """.format(lbl_ok=lbl_ok, lbl_true=lbl_true, jmp=jmp) + push_d()

    elif op == 'neg':
        text = pop_d() + """
        D=-D
        """ + push_d()

    elif op == 'not':
        text = pop_d() + """
        D=!D
        """ + push_d()

    elif op == 'and':
        text = pop_d() + """
        @R13
        M=D
        """ + pop_d() + """
        @R13
        D=D&M
        """ + push_d()

    elif op == 'or':
        text = pop_d() + """
        @R13
        M=D
        """ + pop_d() + """
        @R13
        D=D|M
        """ + push_d()

    else:
        raise RuntimeError('unknown op = {}'.format(op))

    return text_to_codes(text)


def emit_label(name, ctx: CodeGenContext):
    label = ctx.gen_label(name)
    text = """
    ({label})
    """.format(label=label)
    return text_to_codes(text)


def emit_goto(name, ctx: CodeGenContext):
    label = ctx.gen_label(name)
    text = """
    @{label}
    0;JMP
    """.format(label=label)
    return text_to_codes(text)


def emit_if_goto(name, ctx: CodeGenContext):
    label = ctx.gen_label(name)
    text = """
    @SP
    AM=M-1
    D=M
    @{label}
    D;JNE
    """.format(label=label)
    return text_to_codes(text)


def emit_function(name, local_size, ctx: CodeGenContext):
    ctx.enter_func(name)
    label = """
    ({func_name})
    """.format(func_name=ctx.func_name)

    # NOTE(yan): local_size = 1 optimization.
    if local_size == 0:
        text = ""
    elif local_size == 1:
        text = """
        @SP
        AM=M+1
        A=A-1
        M=0
        """
    else:
        text = """
        @SP
        A=M        
        """ + """
        // *sp=0, sp++
        M=0
        A=A+1
        """ * local_size + """
        D=A
        @SP
        M=D
        """
    text = label + text
    return text_to_codes(text)


def emit_return(ctx: CodeGenContext):
    # 这里必须先拿到return address, 是因为如果我们调用一个无参数function的时候
    # return address和argument 0的地址是相同的。如果不先拿到return address的话，
    # 那么返回值会把return address覆盖了。
    if ctx.compact_size:
        return_pop_text = """
        @RETURN_POP_CODE
        0;JMP
        """
    else:
        return_pop_text = RETURN_POP_TEXT
    return text_to_codes(return_pop_text)


def emit_call(name, param_size, ctx: CodeGenContext):
    lbl = ctx.gen_label()
    return_label = lbl + '.ret'

    # 两种方式来调用，一个是放在CALL_PUSH_CODE里面压栈
    # 一个是把CALL_PUSH_CODE代码完全展开
    # 前面一种节省空间

    stack_size = param_size + 5
    if ctx.compact_size:
        call_push_text = f"""
        @CALL_PUSH_CODE
        0;JMP
        """
    else:
        call_push_text = CALL_PUSH_TEXT

    text = f"""
    // push stack size to R13
    @{stack_size}
    D=A
    @R13
    M=D
    // push jump label to R14
    //# :fn
    @{name}
    D=A
    @R14
    M=D
    // push return label to D
    @{return_label}
    D=A
    {call_push_text}
    ({return_label})
    """
    return text_to_codes(text)


class Inst:
    def __init__(self, vm, loc, op, arg1, arg2):
        self.vm = vm
        self.loc = loc
        self.op = op
        self.arg1 = arg1
        self.arg2 = arg2

    def emit(self, ctx: CodeGenContext):
        if self.op == C_FUNC:
            ctx.enter_func(self.arg1)
        if not ctx.output_enabled:
            return []

        if self.op in ARITH_OPS:
            return emit_arith(op=self.op, ctx=ctx)
        elif self.op == C_POP:
            return emit_pop(seg=self.arg1, index=int(self.arg2), ctx=ctx)
        elif self.op == C_PUSH:
            return emit_push(seg=self.arg1, index=int(self.arg2), ctx=ctx)
        elif self.op == C_LABEL:
            return emit_label(name=self.arg1, ctx=ctx)
        elif self.op == C_GOTO:
            return emit_goto(name=self.arg1, ctx=ctx)
        elif self.op == C_IF_GOTO:
            return emit_if_goto(name=self.arg1, ctx=ctx)
        elif self.op == C_FUNC:
            return emit_function(name=self.arg1, local_size=int(self.arg2), ctx=ctx)
        elif self.op == C_RET:
            return emit_return(ctx=ctx)
        elif self.op == C_CALL:
            return emit_call(name=self.arg1, param_size=int(self.arg2), ctx=ctx)
        else:
            raise RuntimeError('unknown op: {}'.format(self.op))

    def emit_with_comment(self, ctx: CodeGenContext):
        codes = ['// L{}: {}'.format(self.loc, self.vm)]
        codes.extend(self.emit(ctx=ctx))
        return codes


def collect_used_functions(input_files, ctx: CodeGenContext):
    for f in input_files:
        with open(f) as fh:
            lines = fh.readlines()
        parser = Parser()
        insts = parser.parse_lines(lines)
        for inst in insts:
            if inst.op == C_CALL:
                name = inst.arg1
                ctx.add_used_fn(name)


def run(input_files, output_file, ctx: CodeGenContext):
    print('{} -> {}'.format(input_files, output_file))
    cg = CodeGen()
    cg.gen_init(ctx)
    collect_used_functions(input_files, ctx)

    for f in input_files:
        with open(f) as fh:
            lines = fh.readlines()
        parser = Parser()
        insts = parser.parse_lines(lines)
        ctx.set_file_path(f)
        cg.gen_codes(insts, ctx)

    cg.gen_fini(ctx)
    codes = cg.codes

    with open(output_file, 'w') as fh:
        for c in codes:
            fh.write(c)
            fh.write('\n')


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--init-code', action='store_true')
    parser.add_argument('--output', action='store')
    parser.add_argument('--remove-unused-fn', action='store_true')
    parser.add_argument('--compact-size', action='store_true')
    args, input_files = parser.parse_known_args()

    ctx = CodeGenContext(args.init_code, args.remove_unused_fn, args.compact_size)
    if args.output:
        # 将这些文件编译成为一个文件
        output_file = args.output
        if len(input_files) > 1:
            ctx.init_code = True
        run(input_files, output_file, ctx)
    else:
        for input_file in input_files:
            output_file = input_file.replace('.vm', '.asm')
            run([input_file], output_file, ctx)


if __name__ == '__main__':
    main()
