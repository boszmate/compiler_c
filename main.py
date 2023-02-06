import sys
from lexer_c import *
from parser_c import *

def main():
    # input1 = "+- = >>>= == != ! /*"
    # input2 = "+- \'This is a string\' # This is a comment!\n */"
    # input3 = "+-123 9.8654*/"
    # input4 = "+- PRINT True* else +Else"

    if len(sys.argv) != 2:
        sys.exit("Error: Program needs input file with code source as argument!")
    with open(sys.argv[1], 'r') as f:
        input = f.read()

    lex = Lexer(input)
    # # Print tokens = debug only
    # token = lex.get_token()
    # while token.kind != TokenType.EOF:
    #     print(token.kind, token.text)
    #     token = lex.get_token()

    parser = Parser(lex)
    parser.program()

if __name__ == "__main__":
    main()
    