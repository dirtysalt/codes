#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

def compile_rules(rules):
    names = []
    code = ''
    for r in rules:
        print(r)
        name, data = r.split('{')
        data = data[:-1].split(',')
        code += f"def f_{name}(x,m,a,s):\n"
        for s in data[:-1]:
            expr, dest = s.split(':')
            code += f"    if {expr}: return '{dest}'\n"
        code += f"    return '{data[-1]}'\n"
        names.append(name)

    code += "\nfmap = {" + ','.join([f'"{x}": f_{x}' for x in names]) + "}"
    code += f"""
def f_entry(x,m,a,s):
    st = 'in'
    global fmap
    while st not in 'AR':
        f = fmap[st]
        st = f(x,m,a,s)
    return st
"""
    print(code)
    exec(code)
    return locals()['f_entry']


def main():
    # test = True
    test = False
    input_file = 'tmp.in' if test else 'input.txt'
    rules = []
    ans = 0
    with open(input_file) as fh:
        for s in fh:
            s = s.strip()
            if not s: break
            rules.append(s)

        f_entry = compile_rules(rules)

        for s in fh:
            s = s.strip()
            s = 'dict(' + s[1:-1] + ')'
            d = eval(s)
            x, m, a, s = d['x'], d['m'], d['a'], d['s']
            st = f_entry(x, m, a, s)
            if st == 'A':
                ans += x + m + a + s
    print(ans)


if __name__ == '__main__':
    main()
