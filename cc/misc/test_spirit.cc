/* coding:utf-8
 * Copyright (C) dirlt
 */

// http://www.ibm.com/developerworks/cn/aix/library/au-boost_parser/

#include <iostream>
#include <string>
#include <boost/spirit.hpp>
using namespace boost::spirit;

struct ParserState {
    std::string name;
}; // class ParserState


struct set_name {
    set_name(ParserState& state): state(state) {}
    void operator()(char const* s, char const* e) const {
        state.name.assign(s, e);
    }
    ParserState& state;
};

struct Parser : public grammar< Parser > {
    Parser(ParserState& state): state(state) {}
    template< typename ScannerT >
    struct definition {
        definition(Parser const& self) {
            keywords = ""; // define keywords.
            typedef strlit<> Token; // case sensitive
            // typedef inhibit_case< strlit<> > Token // case insensitive
            Token MY = "my";
            Token NAME = "name";
            Token IS = "is";
            chlit<> DOUBLEQUOTE('"');

            // grammers.
            identifier = lexeme_d[(alpha_p >> *(alnum_p | '_')) - (keywords)];
            string_literal = lexeme_d[DOUBLEQUOTE >> +(anychar_p - chlit<>('"')) >> DOUBLEQUOTE];
            statement = MY >> NAME >> IS >> string_literal[set_name(self.state)];
        }
        // entry.
        rule< ScannerT> const& start() const {
            return statement;
        }
        symbols<> keywords;
        rule< ScannerT> statement,
              identifier,
              string_literal;
    }; // class definition
    ParserState& state;
}; // class Parser

int main () {
    std::string input = "my name is \"lilei\"";
    ParserState state;
    Parser parser(state);
    parse_info<> info = parse(input.c_str(), parser, space_p);
    if(info.full) {
        printf("%s\n", state.name.c_str());
    }
    return 0;
}
