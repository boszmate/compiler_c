import sys
from lexer_c import *

class Parser():
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = None
        self.peek_token = None

        # init current and next token
        self.next_token()
        self.next_token()

    def check_token(self, kind):
        return kind == self.current_token.kind

    def check_peek_token(self, kind):
        return kind == self.peek_token.kind

    def next_token(self):
        self.current_token = self.peek_token
        self.peek_token = self.lexer.get_token()

    def match_token(self, kind):
        if not self.check_token(kind):
            self.abort(f"Expected {kind.name}, got {self.current_token.kind.name}")
        self.next_token()

    def abort(self, msg):
        sys.exit(f"Parser error: {msg}")

    # rules of py language
    def program(self):
        print("Program starts to parse...")
        while not self.check_token(TokenType.EOF):
            self.statement()
        print("Parsing completed.")

    def statement(self):
        # print statement
        #   print(string | expression) nl
        if self.check_token(TokenType.PRINT):
            self.next_token()
            if not self.check_token(TokenType.ROUND_BRACKET_OPEN):
                self.abort(f"Incorrect token for {self.current_token.kind} statement: {self.peek_token.kind}")

            self.next_token()
            while not self.check_token(TokenType.ROUND_BRACKET_CLOSE):
                if self.check_token(TokenType.STRING):
                    self.next_token()
                else:
                    self.expression()

            if self.check_token(TokenType.ROUND_BRACKET_CLOSE):
                self.next_token()
        # if-elif-else statement
        #   if comparision: nl
        #       {statement} nl
        # colon & nl = tab_indent_begin
        elif self.check_token(TokenType.IF):
            self.next_token()
            self.comparision()
            self.match_token(TokenType.TAB_INDENT_BEGIN)

            while not self.check_token(TokenType.TAB_INDENT_END):
                self.statement()
            self.match_token(TokenType.TAB_INDENT_END)

        # new line
        self.nl()

    # new line
    def nl(self):
        self.match_token(TokenType.NEWLINE)
        while self.check_token(TokenType.NEWLINE):
            self.next_token()

    def expression(self):
        pass

    def comparision(self):
        self.next_token()
        self.next_token()
        self.next_token()
