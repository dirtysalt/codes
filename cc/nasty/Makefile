all:nasty.l.cc nasty.l.hh nasty.y.cc nasty.y.hh
nasty.l.hh nasty.l.cc:nasty.lexer
	flex nasty.lexer
nasty.y.hh nasty.y.cc:nasty.parser
	bison nasty.parser
