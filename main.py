import sys
from lexer_c import *
from parser_c import *
from emitter_c import *

def debug_print(lex):
    token = lex.get_token()
    while token.kind != TokenType.EOF:
        print(token.kind, token.text)
        token = lex.get_token()

def main():
    if len(sys.argv) != 2:
        sys.exit("Error: Program needs input file with code source as argument!")
    with open(sys.argv[1], 'r') as f:
        input = f.read()

    lex = Lexer(input)
    # # Print tokens = debug only
    # debug_print(lex)
    emit = Emitter('out.c')
    parser = Parser(lex, emit)

    parser.program()
    emit.writeOutput()

if __name__ == "__main__":
    main()
    