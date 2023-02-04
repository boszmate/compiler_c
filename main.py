from lexer_c import *

def main():
    # fname = "input.ql"
    # with open(fname) as f:
    #     input = f.read()
    input = "+- = >>>= == != ! /*"
    input2 = "+- \'This is a string\' # This is a comment!\n */"
    input3 = "+-123 9.8654*/"
    input4 = "+- PRINT True* else +Else"

    lex = Lexer(input4)

    token = lex.get_token()
    while token.kind != TokenType.EOF:
        print(token.kind, token.text)
        token = lex.get_token()

if __name__ == "__main__":
    main()