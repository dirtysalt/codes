#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

import string
from lxml import etree
from lxml.etree import Element

KEYWORDS = {
    'class', 'constructor', 'function',
    'method', 'field', 'static', 'var',
    'int', 'char', 'boolean', 'void', 'true', 'false', 'null',
    'this', 'let', 'do', 'if', 'else', 'while', 'return'
}

SYMBOLS = set("{}[]().,;+-*/&|<>=~")
TT_KEYWORD = "keyword"
TT_SYMBOL = "symbol"
TT_IDENTIFIER = "identifier"
TT_INT_CONST = "integerConstant"
TT_STR_CONST = "stringConstant"
IDENTIFIER_CHARS = set(string.ascii_letters + string.digits)


class Token:
    def __init__(self, ty, val):
        self.ty = ty
        self.val = val

        if (self.ty == TT_KEYWORD and self.val not in KEYWORDS) or \
                (self.ty == TT_SYMBOL and self.val not in SYMBOLS):
            raise RuntimeError('wrong arguments to new Token. ty = {}, val = {}'.format(
                self.ty, self.val))

    def __str__(self):
        return 'Token({}, {})'.format(self.ty, self.val)

    def __eq__(self, other):
        return self.ty == other.ty and self.val == other.val

    def to_xml(self):
        root = Element(self.ty)
        root.text = ' {} '.format(self.val)
        return root

    def __hash__(self):
        return hash((self.ty, self.val))


class Tokenizer:
    def __init__(self, buf):
        self.buf = buf
        self.off = 0
        self.last_off = 0
        self.end = len(self.buf)
        self.buf_token = None  # 缓存token, 用于peek.

    def reset(self):
        self.off = self.last_off = 0
        self.buf_token = None

    def has_more(self):
        if self.buf_token:
            return True

        while self.off < self.end:
            c = self.buf[self.off]
            if c in string.whitespace:
                self.off += 1
                continue
            # //  comment
            elif self.buf[self.off: self.off + 2] == '//':
                self.off += 2
                while self.off < self.end and self.buf[self.off] not in ('\n', '\r'):
                    self.off += 1
            # /* */ comment.
            elif self.buf[self.off: self.off + 2] == '/*':
                self.off += 2
                while self.off < self.end:
                    if self.buf[self.off: self.off + 2] == '*/':
                        self.off += 2
                        break
                    else:
                        self.off += 1
            else:
                break

        return self.off < self.end

    def pull(self):
        if self.buf_token:
            tt = self.buf_token
            self.buf_token = None
            return tt

        if not self.has_more():
            return None

        self.last_off = self.off
        c = self.buf[self.off]
        if c in SYMBOLS:
            self.off += 1
            return Token(TT_SYMBOL, c)
        elif c == '"':
            p = self.off + 1
            while p < self.end and self.buf[p] != '"':
                p += 1
            tt = Token(TT_STR_CONST, self.buf[self.off + 1:p])
            self.off = p + 1
            return tt
        elif c in string.digits:
            p = self.off + 1
            while p < self.end and self.buf[p] in string.digits:
                p += 1
            tt = Token(TT_INT_CONST, int(self.buf[self.off: p]))
            self.off = p
            return tt
        elif c in IDENTIFIER_CHARS:
            p = self.off + 1
            while p < self.end and (self.buf[p] in IDENTIFIER_CHARS or self.buf[p] == '_'):
                p += 1
            s = self.buf[self.off: p]
            self.off = p
            if s in KEYWORDS:
                return Token(TT_KEYWORD, s)
            else:
                return Token(TT_IDENTIFIER, s)
        else:
            raise RuntimeError('unknown character = {}'.format(c))

    def peek(self):
        if not self.buf_token:
            self.buf_token = self.pull()
        return self.buf_token


class TreeClass:
    def __init__(self, name, var_decl_list, fn_decl_list):
        self.name = name
        self.var_decl_list = var_decl_list
        self.fn_decl_list = fn_decl_list

    def to_xml(self):
        root = Element('class')
        root.append(Token(TT_KEYWORD, 'class').to_xml())
        root.append(self.name.to_xml())
        root.append(Token(TT_SYMBOL, '{').to_xml())
        for var_decl in self.var_decl_list:
            root.append(var_decl.to_xml())
        for fn_decl in self.fn_decl_list:
            root.append(fn_decl.to_xml())
        root.append(Token(TT_SYMBOL, '}').to_xml())
        return root


class TreeClassVarDecl:
    def __init__(self, cls_pt, ty, names):
        self.cls_pt = cls_pt
        self.ty = ty
        self.names = names

    def to_xml(self):
        root = Element('classVarDec')
        root.append(self.cls_pt.to_xml())
        root.append(self.ty.to_xml())
        first = True
        for name in self.names:
            if not first:
                root.append(Token(TT_SYMBOL, ',').to_xml())
            first = False
            root.append(name.to_xml())
        root.append(Token(TT_SYMBOL, ';').to_xml())
        return root


class TreeClassFnDecl:
    def __init__(self, cls_pt, ty, name, param_list, body):
        self.cls_pt = cls_pt
        self.ty = ty
        self.name = name
        self.param_list = param_list
        self.body = body

    def to_xml(self):
        root = Element('subroutineDec')
        root.append(self.cls_pt.to_xml())
        root.append(self.ty.to_xml())
        root.append(self.name.to_xml())
        root.append(Token(TT_SYMBOL, '(').to_xml())
        ps = Element('parameterList')
        first = True
        for param in self.param_list:
            if not first:
                ps.append(Token(TT_SYMBOL, ',').to_xml())
            first = False
            ps.append(param.ty.to_xml())
            ps.append(param.name.to_xml())
        root.append(ps)
        root.append(Token(TT_SYMBOL, ')').to_xml())
        root.append(self.body.to_xml())
        return root


class TreeFnParam:
    def __init__(self, ty, name):
        self.ty = ty
        self.name = name

    def to_xml(self):
        pass


class TreeFnBody:
    def __init__(self, var_decl_list, statements):
        self.var_decl_list = var_decl_list
        self.statements = statements

    def to_xml(self):
        root = Element('subroutineBody')
        root.append(Token(TT_SYMBOL, '{').to_xml())
        for var_decl in self.var_decl_list:
            root.append(var_decl.to_xml())
        stmts = Element('statements')
        for stmt in self.statements:
            stmts.append(stmt.to_xml())
        root.append(stmts)
        root.append(Token(TT_SYMBOL, '}').to_xml())
        return root


class TreeVarDecl:
    def __init__(self, ty, names):
        self.ty = ty
        self.names = names

    def to_xml(self):
        root = Element('varDec')
        root.append(Token(TT_KEYWORD, 'var').to_xml())
        root.append(self.ty.to_xml())
        first = True
        for name in self.names:
            if not first:
                root.append(Token(TT_SYMBOL, ',').to_xml())
            first = False
            root.append(name.to_xml())
        root.append(Token(TT_SYMBOL, ';').to_xml())
        return root


class TreeIfStmt:
    def __init__(self, cond_expr, true_stmts, else_stmts):
        self.cond_expr = cond_expr
        self.true_stmts = true_stmts
        self.else_stmts = else_stmts

    def to_xml(self):
        root = Element('ifStatement')
        root.append(Token(TT_KEYWORD, 'if').to_xml())
        root.append(Token(TT_SYMBOL, '(').to_xml())
        root.append(self.cond_expr.to_xml())
        root.append(Token(TT_SYMBOL, ')').to_xml())
        root.append(Token(TT_SYMBOL, '{').to_xml())
        stmts = Element('statements')
        for stmt in self.true_stmts:
            stmts.append(stmt.to_xml())
        root.append(stmts)
        root.append(Token(TT_SYMBOL, '}').to_xml())

        if self.else_stmts:
            root.append(Token(TT_KEYWORD, 'else').to_xml())
            root.append(Token(TT_SYMBOL, '{').to_xml())
            stmts = Element('statements')
            for stmt in self.else_stmts:
                stmts.append(stmt.to_xml())
            root.append(stmts)
            root.append(Token(TT_SYMBOL, '}').to_xml())
        return root


class TreeLetStmt:
    def __init__(self, name, ref_expr, val_expr):
        self.name = name
        self.ref_expr = ref_expr
        self.val_expr = val_expr

    def to_xml(self):
        root = Element('letStatement')
        root.append(Token(TT_KEYWORD, 'let').to_xml())
        root.append(self.name.to_xml())
        if self.ref_expr:
            root.append(Token(TT_SYMBOL, '[').to_xml())
            root.append(self.ref_expr.to_xml())
            root.append(Token(TT_SYMBOL, ']').to_xml())
        root.append(Token(TT_SYMBOL, '=').to_xml())
        root.append(self.val_expr.to_xml())
        root.append(Token(TT_SYMBOL, ';').to_xml())
        return root


class TreeWhileStmt:
    def __init__(self, cond_expr, stmts):
        self.cond_expr = cond_expr
        self.stmts = stmts

    def to_xml(self):
        root = Element('whileStatement')
        root.append(Token(TT_KEYWORD, 'while').to_xml())
        root.append(Token(TT_SYMBOL, '(').to_xml())
        root.append(self.cond_expr.to_xml())
        root.append(Token(TT_SYMBOL, ')').to_xml())
        root.append(Token(TT_SYMBOL, '{').to_xml())
        stmts = Element('statements')
        for stmt in self.stmts:
            stmts.append(stmt.to_xml())
        root.append(stmts)
        root.append(Token(TT_SYMBOL, '}').to_xml())
        return root


class TreeDoStmt:
    def __init__(self, call_expr):
        self.call_expr = call_expr

    def to_xml(self):
        root = Element('doStatement')
        root.append(Token(TT_KEYWORD, 'do').to_xml())
        t = self.call_expr.to_xml()
        for sub in t:
            root.append(sub)
        root.append(Token(TT_SYMBOL, ';').to_xml())
        return root


class TreeReturnStmt:
    def __init__(self, ret_expr):
        self.ret_expr = ret_expr

    def to_xml(self):
        root = Element('returnStatement')
        root.append(Token(TT_KEYWORD, 'return').to_xml())
        if self.ret_expr:
            root.append(self.ret_expr.to_xml())
        root.append(Token(TT_SYMBOL, ';').to_xml())
        return root


class TreeExpr:
    def __init__(self, term, rest):
        self.term = term
        self.rest = rest

    def to_xml(self):
        root = Element('expression')
        root.append(self.term.to_xml())
        for (op, term) in self.rest:
            root.append(op.to_xml())
            root.append(term.to_xml())
        return root


class TreeConstTerm:
    def __init__(self, tk):
        self.tk = tk

    def to_xml(self):
        root = Element('term')
        root.append(self.tk.to_xml())
        return root


class TreeVarTerm:
    def __init__(self, name, ref_expr):
        self.name = name
        self.ref_expr = ref_expr

    def to_xml(self):
        root = Element('term')
        root.append(self.name.to_xml())
        if self.ref_expr:
            root.append(Token(TT_SYMBOL, '[').to_xml())
            root.append(self.ref_expr.to_xml())
            root.append(Token(TT_SYMBOL, ']').to_xml())
        return root


class TreeFnCallTerm:
    def __init__(self, fn_name, cls_obj_name, expr_list):
        self.fn_name = fn_name
        self.cls_obj_name = cls_obj_name
        self.expr_list = expr_list

    def to_xml(self):
        root = Element('term')
        if self.cls_obj_name:
            root.append(self.cls_obj_name.to_xml())
            root.append(Token(TT_SYMBOL, '.').to_xml())
        root.append(self.fn_name.to_xml())
        root.append(Token(TT_SYMBOL, '(').to_xml())
        xs = Element('expressionList')
        first = True
        for expr in self.expr_list:
            if not first:
                xs.append(Token(TT_SYMBOL, ',').to_xml())
            first = False
            xs.append(expr.to_xml())
        root.append(xs)
        root.append(Token(TT_SYMBOL, ')').to_xml())
        return root


class TreeExprTerm:
    def __init__(self, expr):
        self.expr = expr

    def to_xml(self):
        root = Element('term')
        root.append(Token(TT_SYMBOL, '(').to_xml())
        root.append(self.expr.to_xml())
        root.append(Token(TT_SYMBOL, ')').to_xml())
        return root


class TreeUnaryTerm:
    def __init__(self, op: Token, term):
        self.op = op
        self.term = term

    def to_xml(self):
        root = Element('term')
        root.append(self.op.to_xml())
        root.append(self.term.to_xml())
        return root


class Parser:
    def __init__(self, tk: Tokenizer):
        self.tk = tk

    def match_token(self, exp):
        tt = self.tk.pull()
        if tt != exp:
            raise RuntimeError('expect {} but get {}'.format(exp, tt))
        return tt

    def match_type(self, ty):
        tt = self.tk.pull()
        if tt.ty != ty:
            raise RuntimeError('expect type {} but get {}'.format(ty, tt))
        return tt

    def match_val_type(self, has_void=False):
        tt = self.tk.pull()
        if (tt.ty == TT_KEYWORD and tt.val in ('char', 'boolean', 'int')) or tt.ty == TT_IDENTIFIER:
            return tt
        if has_void and tt.ty == TT_KEYWORD and tt.val in ('void',):
            return tt
        raise RuntimeError('expect var type but get {}'.format(tt))

    def is_peek_equal(self, exp):
        tt = self.tk.peek()
        return tt == exp

    def is_binary_op(self, tt):
        if tt.ty == TT_SYMBOL and tt.val in "+-*/&|<>=":
            return True
        return False

    def is_unary_op(self, tt):
        if tt.ty == TT_SYMBOL and tt.val in "-~":
            return True
        return False

    def is_constant_value(self, tt):
        if tt.ty in (TT_STR_CONST, TT_INT_CONST):
            return True
        if tt.ty == TT_KEYWORD and tt.val in ('true', 'false', 'this', 'null'):
            return True
        return False

    def parse_class(self):
        self.match_token(Token(TT_KEYWORD, 'class'))
        name = self.match_type(TT_IDENTIFIER)
        self.match_token(Token(TT_SYMBOL, '{'))
        var_decl_list = self.parse_class_var_decl_list()
        fn_decl_list = self.parse_class_fn_decl_list()
        self.match_token(Token(TT_SYMBOL, '}'))
        return TreeClass(name, var_decl_list, fn_decl_list)

    def parse_class_var_decl(self):
        cls_pt = self.tk.pull()
        ty = self.match_val_type()
        names = []
        first = True
        while not self.is_peek_equal(Token(TT_SYMBOL, ';')):
            if not first:
                self.match_token(Token(TT_SYMBOL, ','))
            first = False
            name = self.match_type(TT_IDENTIFIER)
            names.append(name)
        self.match_token(Token(TT_SYMBOL, ';'))
        return TreeClassVarDecl(cls_pt, ty, names)

    def parse_class_var_decl_list(self):
        res = []
        while self.is_peek_equal(Token(TT_KEYWORD, 'static')) or \
                self.is_peek_equal(Token(TT_KEYWORD, 'field')):
            var_decl = self.parse_class_var_decl()
            res.append(var_decl)
        return res

    def parse_class_fn_decl(self):
        cls_pt = self.tk.pull()
        ty = self.match_val_type(has_void=True)
        name = self.match_type(TT_IDENTIFIER)
        self.match_token(Token(TT_SYMBOL, '('))
        param_list = self.parse_fn_param_list()
        self.match_token(Token(TT_SYMBOL, ')'))
        body = self.parse_fn_body()
        return TreeClassFnDecl(cls_pt, ty, name, param_list, body)

    def parse_fn_param_list(self):
        res = []
        first = True
        while not self.is_peek_equal(Token(TT_SYMBOL, ')')):
            if not first:
                self.match_token(Token(TT_SYMBOL, ','))
            ty = self.match_val_type()
            name = self.match_type(TT_IDENTIFIER)
            first = False
            res.append(TreeFnParam(ty, name))
        return res

    def parse_fn_body(self):
        self.match_token(Token(TT_SYMBOL, '{'))
        var_decl_list = []
        while self.is_peek_equal(Token(TT_KEYWORD, 'var')):
            var_decl_list.append(self.parse_var_decl())
        statements = self.parse_statements()
        self.match_token(Token(TT_SYMBOL, '}'))
        return TreeFnBody(var_decl_list, statements)

    def parse_class_fn_decl_list(self):
        res = []
        while self.is_peek_equal(Token(TT_KEYWORD, 'constructor')) or \
                self.is_peek_equal(Token(TT_KEYWORD, 'function')) or \
                self.is_peek_equal(Token(TT_KEYWORD, 'method')):
            fn_decl = self.parse_class_fn_decl()
            res.append(fn_decl)
        return res

    def parse_var_decl(self):
        res = []
        self.match_token(Token(TT_KEYWORD, 'var'))
        ty = self.match_val_type()
        first = True
        names = []
        while not self.is_peek_equal(Token(TT_SYMBOL, ';')):
            if not first:
                self.match_token(Token(TT_SYMBOL, ','))
            first = False
            name = self.match_type(TT_IDENTIFIER)
            names.append(name)
        self.match_token(Token(TT_SYMBOL, ';'))
        return TreeVarDecl(ty, names)

    def parse_statements(self):
        res = []
        while not self.is_peek_equal(Token(TT_SYMBOL, '}')):
            stmt = self.parse_stmt()
            res.append(stmt)
        return res

    def parse_stmt(self):
        if self.is_peek_equal(Token(TT_KEYWORD, 'let')):
            return self.parse_let_stmt()
        elif self.is_peek_equal(Token(TT_KEYWORD, 'if')):
            return self.parse_if_stmt()
        elif self.is_peek_equal(Token(TT_KEYWORD, 'while')):
            return self.parse_while_stmt()
        elif self.is_peek_equal(Token(TT_KEYWORD, 'do')):
            return self.parse_do_stmt()
        elif self.is_peek_equal(Token(TT_KEYWORD, 'return')):
            return self.parse_return_stmt()
        else:
            raise RuntimeError('bad stmt. tt = {}'.format(self.tk.peek()))

    def parse_if_stmt(self):
        self.match_token(Token(TT_KEYWORD, 'if'))
        self.match_token(Token(TT_SYMBOL, '('))
        cond_expr = self.parse_expr()
        self.match_token(Token(TT_SYMBOL, ')'))
        self.match_token(Token(TT_SYMBOL, '{'))
        true_stmts = self.parse_statements()
        self.match_token(Token(TT_SYMBOL, '}'))
        false_stmts = []
        if self.is_peek_equal(Token(TT_KEYWORD, 'else')):
            self.match_token(Token(TT_KEYWORD, 'else'))
            self.match_token(Token(TT_SYMBOL, '{'))
            false_stmts = self.parse_statements()
            self.match_token(Token(TT_SYMBOL, '}'))
        return TreeIfStmt(cond_expr, true_stmts, false_stmts)

    def parse_let_stmt(self):
        self.match_token(Token(TT_KEYWORD, 'let'))
        name = self.match_type(TT_IDENTIFIER)
        ref_expr = None
        if self.is_peek_equal(Token(TT_SYMBOL, '[')):
            self.match_token(Token(TT_SYMBOL, '['))
            ref_expr = self.parse_expr()
            self.match_token(Token(TT_SYMBOL, ']'))
        self.match_token(Token(TT_SYMBOL, '='))
        val_expr = self.parse_expr()
        self.match_token(Token(TT_SYMBOL, ';'))
        return TreeLetStmt(name, ref_expr, val_expr)

    def parse_while_stmt(self):
        self.match_token(Token(TT_KEYWORD, 'while'))
        self.match_token(Token(TT_SYMBOL, '('))
        cond_expr = self.parse_expr()
        self.match_token(Token(TT_SYMBOL, ')'))
        self.match_token(Token(TT_SYMBOL, '{'))
        stmts = self.parse_statements()
        self.match_token(Token(TT_SYMBOL, '}'))
        return TreeWhileStmt(cond_expr, stmts)

    def parse_do_stmt(self):
        self.match_token(Token(TT_KEYWORD, 'do'))
        tt = self.match_type(TT_IDENTIFIER)
        call_expr = self.parse_fn_call(tt)
        self.match_token(Token(TT_SYMBOL, ';'))
        return TreeDoStmt(call_expr)

    def parse_return_stmt(self):
        self.match_token(Token(TT_KEYWORD, 'return'))
        ret_expr = None
        if not self.is_peek_equal(Token(TT_SYMBOL, ';')):
            ret_expr = self.parse_expr()
        self.match_token(Token(TT_SYMBOL, ';'))
        return TreeReturnStmt(ret_expr)

    def parse_expr(self):
        first_term = self.parse_term()
        rest = []
        while True:
            tt = self.tk.peek()
            if self.is_binary_op(tt):
                self.tk.pull()
                term = self.parse_term()
                rest.append((tt, term))
            else:
                break
        return TreeExpr(first_term, rest)

    def parse_term(self):
        tt = self.tk.peek()
        if self.is_constant_value(tt):
            self.tk.pull()
            return TreeConstTerm(tt)
        elif tt.ty == TT_IDENTIFIER:
            self.tk.pull()
            t2 = self.tk.peek()
            ref_expr = None
            if t2 == Token(TT_SYMBOL, '['):
                self.tk.pull()
                ref_expr = self.parse_expr()
                self.match_token(Token(TT_SYMBOL, ']'))
                return TreeVarTerm(tt, ref_expr)
            elif t2 == Token(TT_SYMBOL, '.') or t2 == Token(TT_SYMBOL, '('):
                return self.parse_fn_call(tt)
            else:
                return TreeVarTerm(tt, ref_expr)
        elif tt == Token(TT_SYMBOL, '('):
            self.tk.pull()
            expr = self.parse_expr()
            self.match_token(Token(TT_SYMBOL, ')'))
            return TreeExprTerm(expr)
        elif self.is_unary_op(tt):
            self.tk.pull()
            term = self.parse_term()
            return TreeUnaryTerm(tt, term)
        else:
            raise RuntimeError('bad term. tt = {}'.format(tt))

    def parse_fn_call(self, tt):
        cls_obj_name = None
        if self.is_peek_equal(Token(TT_SYMBOL, '.')):
            cls_obj_name = tt
            self.match_token(Token(TT_SYMBOL, '.'))
            tt = self.match_type(TT_IDENTIFIER)
        self.match_token(Token(TT_SYMBOL, '('))
        expr_list = self.parse_expr_list()
        self.match_token(Token(TT_SYMBOL, ')'))
        return TreeFnCallTerm(tt, cls_obj_name, expr_list)

    def parse_expr_list(self):
        res = []
        first = True
        while not self.is_peek_equal(Token(TT_SYMBOL, ')')):
            if not first:
                self.match_token(Token(TT_SYMBOL, ','))
            expr = self.parse_expr()
            first = False
            res.append(expr)
        return res


def write_xml(xml_tree, output_file):
    # 不合规的XML格式，对于没有内容的tag, 应该使用self closing tag格式
    s = etree.tostring(xml_tree, pretty_print=True).decode('utf8')
    ss = s.split('\n')
    fields = ('expressionList', 'parameterList')
    ss2 = []
    for x in ss:
        found = False
        for f in fields:
            p = x.find('<' + f + '/>')
            if p != -1:
                found = True
                ss2.append(x[:p] + '<' + f + '>')
                ss2.append(x[:p] + '</' + f + '>')
                break
        if not found:
            ss2.append(x)
    s = '\n'.join(ss2)

    with open(output_file, 'w', newline='\r\n') as fh:
        fh.write(s)


def run(input_file, output_file):
    print('{} -> {}'.format(input_file, output_file))
    with open(input_file) as fh:
        tokenizer = Tokenizer(fh.read())
    tokenizer.reset()
    parser = Parser(tokenizer)
    cls = parser.parse_class()
    xml_tree = cls.to_xml()
    write_xml(xml_tree, output_file)


def main():
    import argparse
    parser = argparse.ArgumentParser()
    args, input_files = parser.parse_known_args()

    for input_file in input_files:
        output_file = input_file.replace('.jack', '.txt')
        run(input_file, output_file)


if __name__ == '__main__':
    main()
