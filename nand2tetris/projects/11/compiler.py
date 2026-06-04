#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
from collections import defaultdict

from parser import Parser, TT_INT_CONST, Tokenizer, TreeClass, TreeClassFnDecl, TreeConstTerm, TreeDoStmt, TreeExpr, \
    TreeExprTerm, TreeFnBody, TreeFnCallTerm, TreeIfStmt, TreeLetStmt, TreeReturnStmt, TreeUnaryTerm, TreeVarTerm, \
    TreeWhileStmt


class Symbol:
    def __init__(self, name, kind, type, index):
        self.name = name
        self.kind = kind
        self.type = type
        self.index = index

    def __str__(self):
        return 'Symbol(name={}, kind={}, type={}, index={})'.format(
            self.name, self.kind, self.type, self.index
        )


KIND_CLASS = 'class'
KIND_FUNCTION = 'fn'
KIND_STATIC = 'static'
KIND_FIELD = 'field'
KIND_ARGUMENT = 'argument'
KIND_LOCAL = 'local'
TYPE_CLASS = 'class'
KW_THIS = 'this'
KW_METHOD = 'method'
KW_STATIC = 'static'
KW_FIELD = 'field'
KW_FUNCTION = 'function'
KW_CTOR = 'constructor'
KW_NEW = "new"


class SimpleSymbolTable:
    def __init__(self):
        self.table = dict()
        self.kind_counter = {
            KIND_CLASS: 0,
            KIND_FUNCTION: 0,
            KIND_STATIC: 0,
            KIND_FIELD: 0,
            KIND_ARGUMENT: 0,
            KIND_LOCAL: 0
        }

    def make(self, name, kind, type):
        index = self.kind_counter[kind]
        self.kind_counter[kind] += 1
        sym = Symbol(name, kind, type, index)
        self.table[name] = sym
        return sym

    def lookup(self, name):
        return self.table.get(name)

    def __str__(self):
        return str([str(x) for x in self.table.values()])

    def kind_count(self, kind):
        return self.kind_counter[kind]


class SymbolTable:
    def __init__(self):
        self.sst_list = []

    def enter(self):
        self.sst_list.append(SimpleSymbolTable())

    def exit(self):
        return self.sst_list.pop()

    def lookup(self, name):
        for sst in reversed(self.sst_list):
            v = sst.lookup(name)
            if v:
                return v
        return None

    def current_sst(self):
        return self.sst_list[-1]


class ClassInfo:
    def __init__(self, input_file):
        self.input_file = input_file
        self.field_number = 0
        self.sst = None


class FunctionInfo:
    def __init__(self):
        self.local_number = 0


class Resolver:
    def __init__(self,
                 report_type_not_found=True,
                 report_dup_def=True,
                 report_current_sst=True,
                 report_lookup_entry=True,
                 has_builtin_class_symtable=False):
        self.symtable = SymbolTable()
        self.report_type_not_found = report_type_not_found
        self.report_dup_def = report_dup_def
        self.report_current_sst = report_current_sst
        self.report_lookup_entry = report_lookup_entry
        self.has_builtin_class_symtable = has_builtin_class_symtable
        self.builtin_classes = ('Math', 'String', 'Array', 'Output', 'Screen', 'Keyboard', 'Memory', 'Sys')

    def resolve_class_list(self, cls_list):
        self.symtable.enter()
        sst: SimpleSymbolTable = self.symtable.current_sst()
        for cls in self.builtin_classes:
            sst.make(cls, KIND_CLASS, TYPE_CLASS)

        # 把所有的class全部添加到符号表
        for cls in cls_list:
            name = cls.name.val
            if sst.lookup(name):
                if self.report_dup_def:
                    print('dup-def of class {}'.format(name))
            else:
                sst.make(name, KIND_CLASS, cls)
        if self.report_current_sst:
            print('class_list: current sst = {}'.format(sst))

        # 把所有的class下面function全部添加到符号表中
        for cls in cls_list:
            self.symtable.enter()
            sst: SimpleSymbolTable = self.symtable.current_sst()
            fn_decl_list = cls.fn_decl_list
            for fn_decl in fn_decl_list:
                name = fn_decl.name.val
                if sst.lookup(name):
                    if self.report_dup_def:
                        print('dup-def of function {} in class {}'.format(name, cls.name.val))
                else:
                    sst.make(name, KIND_FUNCTION, fn_decl)
            self.symtable.exit()
            cls.info.sst = sst

        # 然后编译每个class
        for cls in cls_list:
            self.symtable.enter()
            self.resolve_class(cls)
            self.symtable.exit()

        self.symtable.exit()

    def resolve_class(self, cls: TreeClass):
        sst: SimpleSymbolTable = self.symtable.current_sst()
        var_decl_list = cls.var_decl_list
        fn_decl_list = cls.fn_decl_list

        # 把所有的variable和function加入符号表
        for var_decl in var_decl_list:
            cls_pt = var_decl.cls_pt.val
            assert cls_pt in (KW_STATIC, KW_FIELD)
            ty = var_decl.ty.val
            var_names = var_decl.names
            self.resolve_type(ty)
            for var_name in var_names:
                name = var_name.val
                if sst.lookup(name):
                    if self.report_dup_def:
                        print('dup-def of variable {} in class {}'.format(name, cls.name.val))
                else:
                    sst.make(name, cls_pt, ty)

        cls.info.field_number = sst.kind_count(KIND_FIELD)
        for fn_decl in fn_decl_list:
            name = fn_decl.name.val
            if sst.lookup(name):
                if self.report_dup_def:
                    print('dup-def of function {} in class {}'.format(name, cls.name.val))
            else:
                sst.make(name, KIND_FUNCTION, fn_decl)

        if self.report_current_sst:
            print('class {}: current sst = {}'.format(cls.name.val, sst))

        # 然后编译每个function
        for fn_decl in fn_decl_list:
            self.symtable.enter()
            self.resolve_function(fn_decl, cls)
            self.symtable.exit()

    def resolve_function(self, fn_decl: TreeClassFnDecl, cls: TreeClass):
        sst: SimpleSymbolTable = self.symtable.current_sst()
        self.resolve_type(fn_decl.ty.val)
        cls_pt = fn_decl.cls_pt.val
        # 如果是method的话，那么有个额外参数this
        if cls_pt == KW_METHOD:
            sst.make(KW_THIS, KIND_ARGUMENT, cls)

        param_list = fn_decl.param_list
        for param in param_list:
            name = param.name.val
            ty = param.ty.val
            self.resolve_type(ty)
            if sst.lookup(name):
                if self.report_dup_def:
                    print('dup-def of param {} in function {}'.format(name, fn_decl.name.val))
            else:
                sst.make(name, KIND_ARGUMENT, ty)

        body: TreeFnBody = fn_decl.body
        var_decl_list = body.var_decl_list
        for var_decl in var_decl_list:
            ty = var_decl.ty.val
            var_names = var_decl.names
            self.resolve_type(ty)
            for var_name in var_names:
                name = var_name.val
                if sst.lookup(name):
                    if self.report_dup_def:
                        print('dup-def of var {} in function {}'.format(name, fn_decl.name.val))
                else:
                    sst.make(name, KIND_LOCAL, ty)
        info = FunctionInfo()
        info.local_number = sst.kind_count(KIND_LOCAL)
        fn_decl.info = info

        if self.report_current_sst:
            print('function {}: current sst = {}'.format(fn_decl.name.val, sst))
        # 遍历语句去解析里面引用的变量，将每个变量添加上具体的引用符号
        self.resolve_statements(body.statements)

    def resolve_statements(self, stmts):
        for stmt in stmts:
            self.resolve_stmt(stmt)

    def resolve_type(self, ty):
        if ty in ('boolean', 'char', 'int', 'void'):
            return True
        v = self.symtable.lookup(ty)
        if v and v.kind == KIND_CLASS:
            return True
        if self.report_type_not_found:
            print('type not found: {}'.format(ty))
        return False

    def resolve_stmt(self, stmt):
        if isinstance(stmt, TreeIfStmt):
            self.resolve_expr(stmt.cond_expr)
            self.resolve_statements(stmt.true_stmts)
            self.resolve_statements(stmt.else_stmts)
        elif isinstance(stmt, TreeLetStmt):
            self.resolve_name(stmt.name)
            self.resolve_expr(stmt.ref_expr)
            self.resolve_expr(stmt.val_expr)
        elif isinstance(stmt, TreeWhileStmt):
            self.resolve_expr(stmt.cond_expr)
            self.resolve_statements(stmt.stmts)
        elif isinstance(stmt, TreeDoStmt):
            self.resolve_expr(stmt.call_expr)
        elif isinstance(stmt, TreeReturnStmt):
            self.resolve_expr(stmt.ret_expr)
            pass
        else:
            raise RuntimeError('unknown stmt = {}'.format(stmt))

    def resolve_expr(self, expr):
        if isinstance(expr, TreeExpr):
            self.resolve_expr(expr.term)
            for op, term in expr.rest:
                self.resolve_expr(term)
        elif isinstance(expr, TreeConstTerm):
            pass
        elif isinstance(expr, TreeVarTerm):
            self.resolve_name(expr.name)
            self.resolve_expr(expr.ref_expr)
        elif isinstance(expr, TreeFnCallTerm):
            # 如果有限定对象，那么认为是对象上的方法，这里不就去解析这些对象上的方法了
            fn_entry = None
            if expr.cls_obj_name:
                class_entry = self.resolve_name(expr.cls_obj_name)
                is_function = False
                # 如果是class的话，那么要确保expr.fn_name出现在cls的symtable里面
                # 如果是对象的话，那么要确保expr.fn_name出现在对象的cls的symtable里面
                if class_entry.kind == KIND_CLASS:
                    is_function = True
                    pass
                else:
                    class_entry = self.symtable.lookup(class_entry.type)
                    assert class_entry and class_entry.kind == KIND_CLASS

                if (class_entry.name not in self.builtin_classes) or self.has_builtin_class_symtable:
                    sst = class_entry.type.info.sst
                    fn_entry = sst.lookup(expr.fn_name.val)
                    assert fn_entry.kind == KIND_FUNCTION

                    # 检查函数属性是否正确
                    fn_decl = fn_entry.type
                    cls_pt = fn_decl.cls_pt.val
                    if is_function:
                        if expr.fn_name.val == KW_NEW:
                            assert cls_pt == KW_CTOR
                        else:
                            assert cls_pt == KW_FUNCTION
                    else:
                        assert cls_pt == KW_METHOD


            # 否则认为是自己Class里面的方法，这个因为在符号表里面了，可以查找到
            # 理论上生成代码是不需要查找这个方法名称的
            else:
                fn_entry = self.resolve_name(expr.fn_name)
                assert fn_entry.type.cls_pt.val == KW_METHOD

            # 如果找到了函数定义, 检查数量是否匹配
            if fn_entry:
                fn_decl = fn_entry.type
                assert isinstance(fn_decl, TreeClassFnDecl)
                assert len(fn_decl.param_list) == len(expr.expr_list)

            for ex in expr.expr_list:
                self.resolve_expr(ex)

        elif isinstance(expr, TreeExprTerm):
            self.resolve_expr(expr.expr)
        elif isinstance(expr, TreeUnaryTerm):
            self.resolve_expr(expr.term)

    def resolve_name(self, name):
        entry = self.symtable.lookup(name.val)
        assert entry
        name.info = entry
        if self.report_lookup_entry:
            print('lookup {} -> {}'.format(name.val, entry))
        return entry


def text_to_codes(text):
    ss = text.split('\n')
    ss = list(filter(lambda x: x and not x.startswith('//'),
                     map(lambda x: x.strip(), ss)))
    return ss


op_to_code = {
    '*': 'call Math.multiply 2',
    '/': 'call Math.divide 2',
    '+': 'add',
    '-': 'sub',
    '&': 'and',
    '|': 'or',
    '<': 'lt',
    '>': 'gt',
    '=': 'eq',
    '~': 'not',
}


class CodeGen:
    def __init__(self):
        self.texts = []
        self.label_counter = defaultdict(int)
        self.class_name = None

    def add_text(self, text):
        self.texts.append(text)

    def gen_label(self, scope):
        v = self.label_counter[scope]
        self.label_counter[scope] += 1
        return v

    def reset_label(self):
        self.label_counter.clear()

    def output(self, output_file):
        with open(output_file, 'w') as fh:
            for text in self.texts:
                codes = text_to_codes(text)
                for code in codes:
                    fh.write(code)
                    fh.write('\n')

    def gen_class(self, cls: TreeClass):
        fn_decl_list = cls.fn_decl_list
        self.class_name = cls.name.val
        for fn_decl in fn_decl_list:
            self.reset_label()
            info = fn_decl.info
            text = """
            function {class_name}.{func_name} {local_number}
            """.format(
                class_name=cls.name.val,
                func_name=fn_decl.name.val,
                local_number=info.local_number
            )
            self.add_text(text)

            cls_pt = fn_decl.cls_pt.val
            if cls_pt == 'function':
                self.gen_function(fn_decl)
            elif cls_pt == 'method':
                self.gen_method(fn_decl)
            elif cls_pt == 'constructor':
                self.gen_ctor(fn_decl, cls)
            else:
                raise RuntimeError('unknown function cls_pt: {}'.format(cls_pt))

    def gen_method(self, fn_decl: TreeClassFnDecl):
        text = """
        // set to THIS
        push argument 0
        pop pointer 0
        """
        self.add_text(text)
        self.gen_function(fn_decl)

    def gen_ctor(self, fn_decl: TreeClassFnDecl, cls: TreeClass):
        info = cls.info
        field_number = info.field_number
        text = """
        push constant {field_number}
        call Memory.alloc 1
        pop pointer 0
        """.format(field_number=field_number)
        self.add_text(text)
        self.gen_function(fn_decl)

    def gen_function(self, fn_decl: TreeClassFnDecl):
        self.gen_statements(fn_decl.body.statements)

    def gen_statements(self, stmts):
        for stmt in stmts:
            if isinstance(stmt, TreeIfStmt):
                self.gen_if_stmt(stmt)
            elif isinstance(stmt, TreeLetStmt):
                self.gen_let_stmt(stmt)
            elif isinstance(stmt, TreeWhileStmt):
                self.gen_while_stmt(stmt)
            elif isinstance(stmt, TreeDoStmt):
                self.gen_do_stmt(stmt)
            elif isinstance(stmt, TreeReturnStmt):
                self.gen_return_stmt(stmt)
            else:
                raise RuntimeError('unknown stmt = {}'.format(stmt))

    def gen_if_stmt(self, stmt: TreeIfStmt):
        self.gen_expr(stmt.cond_expr)
        lbl = self.gen_label('if')
        true_label = 'IF_TRUE{}'.format(lbl)
        false_label = 'IF_FALSE{}'.format(lbl)
        end_label = 'IF_END{}'.format(lbl)

        # 两种不同的生成方式，其实完全可以使用第一种
        # 不过为了和JackCompiler.sh输出一致，使用了这种方法
        if not stmt.else_stmts:
            text = f"""
            if-goto {true_label}
            """
            self.add_text(text)
            self.gen_statements(stmt.else_stmts)

            text = f"""
            goto {false_label}
            label {true_label}
            """
            self.add_text(text)
            self.gen_statements(stmt.true_stmts)
            self.add_text(f'label {false_label}')

        else:
            text = f"""
            if-goto {true_label}
            goto {false_label}
            label {true_label}
            """
            self.add_text(text)
            self.gen_statements(stmt.true_stmts)
            text = f"""
            goto {end_label}
            label {false_label}
            """
            self.add_text(text)
            self.gen_statements(stmt.else_stmts)
            self.add_text(f'label {end_label}')

    def gen_let_stmt(self, stmt: TreeLetStmt):
        if stmt.ref_expr is None:
            self.gen_expr(stmt.val_expr)
            self.gen_pop_var(stmt.name)
        else:
            self.gen_expr(stmt.ref_expr)
            self.gen_push_var(stmt.name)
            self.add_text('add')
            self.gen_expr(stmt.val_expr)
            self.add_text("""
            pop temp 0
            pop pointer 1
            push temp 0
            pop that 0
            """)

    def gen_while_stmt(self, stmt: TreeWhileStmt):
        lbl = self.gen_label('while')
        begin_label = 'WHILE_EXP{}'.format(lbl)
        end_label = 'WHILE_END{}'.format(lbl)
        self.add_text(f'label {begin_label}')
        self.gen_expr(stmt.cond_expr)
        self.add_text(f"""
        not
        if-goto {end_label}
        """)
        self.gen_statements(stmt.stmts)
        self.add_text(f"""
        goto {begin_label}
        label {end_label}
        """)

    def gen_do_stmt(self, stmt: TreeDoStmt):
        self.gen_expr(stmt.call_expr)
        self.add_text('pop temp 0')

    def gen_return_stmt(self, stmt: TreeReturnStmt):
        if stmt.ret_expr:
            self.gen_expr(stmt.ret_expr)
        else:
            self.add_text("push constant 0")
        self.add_text('return')

    def gen_push_var(self, var):
        sym = var.info
        kind = sym.kind
        index = sym.index
        if kind == KW_FIELD:
            kind = KW_THIS
        self.add_text(f"""
        push {kind} {index}
        """)

    def gen_pop_var(self, var):
        sym = var.info
        kind = sym.kind
        index = sym.index
        if kind == KW_FIELD:
            kind = KW_THIS
        self.add_text(f"""
        pop {kind} {index}
        """)

    def gen_binop_expr(self, first, rest):
        self.gen_expr(first)
        if rest:
            (op, second) = rest.pop(0)
            self.gen_binop_expr(second, rest)
            self.gen_op(op)

    def gen_op(self, op, unary=False):
        op = op.val
        if op == '-' and unary:
            self.add_text('neg')
        else:
            self.add_text(op_to_code[op])

    def gen_expr(self, expr):
        if isinstance(expr, TreeExpr):
            self.gen_binop_expr(expr.term, expr.rest)
        elif isinstance(expr, TreeConstTerm):
            tk = expr.tk
            val = expr.tk.val
            if tk.ty == TT_INT_CONST:
                self.add_text("push constant {}".format(expr.tk.val))
            elif val == "true":
                # self.add_text('push constant {}'.format(2 << 16 - 1))
                self.add_text("""
                push constant 0
                not
                """)
            elif val in ("false", 'null'):
                self.add_text('push constant 0')
            elif val == 'this':
                self.add_text("push pointer 0")
            else:
                self.add_text("""
                push constant {size}
                call String.new 1
                """.format(size=len(val)))
                for c in val:
                    self.add_text("""
                    push constant {ch}
                    call String.appendChar 2
                    """.format(ch=ord(c)))

        elif isinstance(expr, TreeExprTerm):
            self.gen_expr(expr.expr)
        elif isinstance(expr, TreeUnaryTerm):
            self.gen_expr(expr.term)
            self.gen_op(expr.op, unary=True)
        elif isinstance(expr, TreeVarTerm):
            if expr.ref_expr:
                self.gen_expr(expr.ref_expr)
                self.gen_push_var(expr.name)
                self.add_text("""
                add
                pop pointer 1
                push that 0
                """)
            else:
                self.gen_push_var(expr.name)
        elif isinstance(expr, TreeFnCallTerm):
            self.gen_fn_call_expr(expr)
        else:
            raise RuntimeError('unknown expr = {}'.format(expr))

    def gen_fn_call_expr(self, expr):
        class_name = self.class_name
        func_name = expr.fn_name.val
        param_size = len(expr.expr_list)
        if expr.cls_obj_name:
            info = expr.cls_obj_name.info
            if info.kind == KIND_CLASS:  # 如果这个符号是class的话，说明function调用
                assert info.type == TYPE_CLASS or isinstance(info.type, TreeClass)
                class_name = expr.cls_obj_name.val
            else:  # 否则说明这个符号是object, method调用
                class_name = info.type
                self.gen_push_var(expr.cls_obj_name)
                param_size += 1
        else:
            # 默认就是method调用
            param_size += 1
            self.add_text("""
            push pointer 0
            """)

        for ex in expr.expr_list:
            self.gen_expr(ex)
        self.add_text(f"""
        call {class_name}.{func_name} {param_size}
        """)


class Compiler:
    def __init__(self, file_ext='.vm'):
        self.file_ext = file_ext

    def parse_files(self, input_files):
        cls_list = []
        for input_file in input_files:
            with open(input_file) as fh:
                tokenizer = Tokenizer(fh.read())
            tokenizer.reset()
            parser = Parser(tokenizer)
            cls = parser.parse_class()
            cls_info = ClassInfo(input_file)
            cls.info = cls_info
            cls_list.append(cls)
        return cls_list

    def resolve_symbols(self, cls_list):
        resolver = Resolver(report_lookup_entry=False, report_current_sst=False)
        resolver.resolve_class_list(cls_list)

    def gen_codes(self, cls_list):
        for cls in cls_list:
            cg = CodeGen()
            cg.gen_class(cls)
            output_file = cls.info.input_file.replace('.jack', self.file_ext)
            cg.output(output_file)

    def run(self, input_files):
        cls_list = self.parse_files(input_files)
        self.resolve_symbols(cls_list)
        self.gen_codes(cls_list)


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--file-ext', action='store', default='.vm')
    args, input_files = parser.parse_known_args()
    compiler = Compiler(args.file_ext)
    compiler.run(input_files)


if __name__ == '__main__':
    main()
