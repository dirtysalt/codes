/* coding:utf-8
 * Copyright (C) dirlt
 */

#include <cassert>
#include <sstream>
#include "nasty/nasty.h"
using namespace nasty;
#include "nasty/nasty.y.hh"
#include "nasty/nasty.l.hh"

int yyparse(void* scanner, nasty::Parser* parser);

namespace nasty {

Parser::~Parser() {
    delete ex_;
    ex_ = 0;
}

Expr* Parser::run() {
    FILE* fin = fopen(f_.c_str(), "rb");
    if (!fin) {
        WARNING("open(%s) failed(%s)", f_.c_str(), SERRNO);
        return 0;
    }
    Expr* ex = run(fin);
    if (!ex) {
        fclose(fin);
    }
    return ex;
}

Expr* Parser::run(FILE* fin) {
    yyscan_t scanner;
    yylex_init(&scanner);
    yyset_in(fin, scanner);
    if(yyparse(scanner, this) != 0) {
        delete ex_;
        ex_ = 0;
    }
    return ex_;
}

Expr* Parser::run(std::string s) {
    // todo
    return 0;
}

void Expr::appendExpr(Expr* ex) {
    tree_.push_back(ex);
}

Expr::~Expr() {
    if (tree_.size()) {
        for(size_t i = 0; i < tree_.size(); i++) {
            delete tree_[i];
        }
    }
}

static inline void repeat(std::ostream& os, int indent, char c) {
    if (indent) {
        for(int i = 0; i < indent; i++) {
            os << c;
        }
    }
}

std::string Expr::toString() const {
    std::ostringstream os ;
    write(os);
    return os.str();
}

void Expr::write(std::ostream& os) const {
    if (tree_.size()) {
        assert(type_ == TREE);
        os << '(';
        for(size_t i = 0; i < tree_.size(); i++) {
            tree_[i]->write(os);
            if((i + 1) != tree_.size()) {
                os << ' ';
            }
        }
        os << ')';
    } else {
        os << text_;
    }
}

} // namespace nasty
