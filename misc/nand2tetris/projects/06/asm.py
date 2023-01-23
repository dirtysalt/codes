#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Inst:
    def __init__(self):
        pass

    def emit(self, fixsym=False):
        pass


class AInst(Inst):
    def __init__(self, addr, tags):
        super()
        self.addr = addr
        self.value = addr
        self.tags = tags

    def must_be_fn(self):
        if not self.tags:
            return False
        return ':fn' in self.tags

    def emit(self, fixsym=False):
        if fixsym:
            return '@{}'.format(self.value)
        else:
            return '0{:015b}'.format(self.value)

    def __str__(self):
        return '@{}'.format(self.addr)


dest_in_seq = [None, 'M', 'D', 'MD', 'A', 'AM', 'AD', 'AMD']
jump_in_seq = [None, 'JGT', 'JEQ', 'JGE', 'JLT', 'JNE', 'JLE', 'JMP']
dest_map = {v: '{:03b}'.format(i) for i, v in enumerate(dest_in_seq)}
jump_map = {v: '{:03b}'.format(i) for i, v in enumerate(jump_in_seq)}
comp_map = {
    '0': '0101010',
    '1': '0111111',
    '-1': '0111010',
    'D': '0001100',
    'A': '0110000',
    '!D': '00011101',
    '!A': '0110001',
    '-D': '0001111',
    '-A': '0110011',
    'D+1': '0011111',
    'A+1': '0110111',
    'D-1': '0001110',
    'A-1': '0110010',
    'D+A': '0000010',
    'D-A': '0010011',
    'A-D': '0000111',
    'D&A': '0000000',
    'D|A': '0010101',
    'M': '1110000',
    '!M': '1110001',
    '-M': '1110011',
    'M+1': '1110111',
    'M-1': '1110010',
    'D+M': '1000010',
    'D-M': '1010011',
    'M-D': '1000111',
    'D&M': '1000000',
    'D|M': '1010101',
}


class CInst(Inst):
    def __init__(self, dest, comp, jump):
        super()
        self.dest = dest.replace(' ', '') if dest else None
        self.comp = comp.replace(' ', '') if comp else None
        self.jump = jump.replace(' ', '') if jump else None

    def emit(self, fixsym=False):
        if fixsym:
            return str(self)
        else:
            return '111' + comp_map[self.comp] + dest_map[self.dest] + jump_map[self.jump]

    def __str__(self):
        res = self.comp
        if self.dest:
            res = self.dest + '=' + res
        if self.jump:
            res = res + ';' + self.jump
        return res


class Label(Inst):
    def __init__(self, name):
        super()
        self.name = name

    def emit(self, fixsym=False):
        return None


class Parser:
    def __init__(self, debug=False):
        self.debug = debug
        self.tags = None

    def parse_line(self, x):
        x = x.strip()

        # special comment for tags
        if x.startswith('//#'):
            x = x[3:].strip()
            tags = [c.strip() for c in x.split()]
            tags = [c for c in tags]
            self.tags = tags
            return

        # remove comment
        p = x.find('//')
        if p != -1:
            x = x[:p].strip()

        if not x:
            return None

        tags = self.tags
        self.tags = None
        if x[0] == '(' and x[-1] == ')':
            name = x[1:-1]
            return Label(name)
        elif x[0] == '@':
            addr = x[1:]
            if addr.isdigit():
                addr = int(addr)
            return AInst(addr, tags)

        if '=' not in x:
            dest = None
        else:
            dest, x = x.split('=')

        if ';' not in x:
            jump = None
        else:
            x, jump = x.split(';')
        comp = x
        return CInst(dest, comp, jump)

    def parse_lines(self, lines):
        insts = []
        for x in lines:
            inst = self.parse_line(x)
            if not inst:
                continue
            insts.append(inst)
        return insts


class Assembler:
    def __init__(self, insts, debug=False):
        self.insts = insts
        self.symtable = {}
        self.debug = debug

    def build_builtin_symtable(self):
        symtable = self.symtable
        for i in range(0, 16):
            symtable['R{}'.format(i)] = i
        for k, v in (('SP', 0), ('LCL', 1), ('ARG', 2),
                     ('THIS', 3), ('THAT', 4), ('SCREEN', 16384),
                     ('KBD', 24576)):
            symtable[k] = v

    def build_label_symtable(self):
        offset = 0
        labels = []

        def add_labels(labels, offset):
            for lbl in labels:
                if self.debug:
                    print('label {} -> {}'.format(lbl, offset))
                self.symtable[lbl] = offset
            labels.clear()

        for inst in self.insts:
            if isinstance(inst, Label):
                labels.append(inst.name)
            else:
                add_labels(labels, offset)
                offset += 1
        add_labels(labels, offset)

    def build_var_symtable(self):
        offset = 16
        for (i, inst) in enumerate(self.insts):
            if isinstance(inst, AInst):
                # absolute address or label.
                if isinstance(inst.addr, int) or \
                        inst.addr in self.symtable:
                    pass
                else:
                    if inst.must_be_fn():
                        print('[WARNING] require address label {}'.format(inst))

                    # 如果下面一条是跳转指令的话，那么说明链接错误
                    if (i + 1) < len(self.insts):
                        inst2 = self.insts[i + 1]
                        if isinstance(inst2, CInst) and inst2.jump is not None:
                            print('[WARNING] jump inst follows non-address label. {} -> {}'.format(
                                inst, inst2))

                    if self.debug:
                        print('var {} -> {}'.format(inst.addr, offset))
                    self.symtable[inst.addr] = offset
                    offset += 1

    def emit(self, fixsym=False):
        codes = []
        for inst in self.insts:
            if isinstance(inst, AInst) and \
                    not isinstance(inst.addr, int):
                inst.value = self.symtable[inst.addr]
            code = inst.emit(fixsym=fixsym)
            if code:
                codes.append(code)
        return codes


def run(args, input_file, output_file):
    with open(input_file) as fh:
        lines = fh.readlines()
    parser = Parser(debug=args.debug)
    insts = parser.parse_lines(lines)
    asm = Assembler(insts, debug=args.debug)
    asm.build_builtin_symtable()
    # 3 passes. we can combine last two passes to a single one.
    asm.build_label_symtable()
    asm.build_var_symtable()
    codes = asm.emit(fixsym=args.fixsym)
    with open(output_file, 'w') as fh:
        for c in codes:
            fh.write(c)
            fh.write('\n')


def main():
    import argparse
    import sys
    parser = argparse.ArgumentParser()
    parser.add_argument('--debug', action='store_true')
    parser.add_argument('--fixsym', action='store_true')
    parser.add_argument('--ext', action='store')
    args, input_files = parser.parse_known_args()
    ext = args.ext or '.hack'

    for input_file in input_files:
        output_file = input_file.replace('.asm', ext)
        print('{}: {} -> {}'.format(sys.argv[0], input_file, output_file))
        run(args, input_file, output_file)


if __name__ == '__main__':
    main()
