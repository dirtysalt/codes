/* coding:utf-8
 * Copyright (C) dirlt
 */

#include <cassert>
#include <cstdio>
#include "nasty/nasty.h"
using namespace nasty;

int main() {
    Parser p("test/test.in");
    Expr* e = p.run();
    const std::string s = e->toString();
    printf("%s\n", s.c_str());
    return 0;
}
