import sys
from lexer_c import *

class Parser():
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = None
        self.peek_token = None
        self.skip_nl_after_tab_end = False

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
        # Print only for Debug purpose
        # print(self.peek_token.kind.name)

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
        #   elif comparision: nl
        #       {statement} nl
        #   else: nl
        #       {statement} nl
        #
        # while statement
        #   while comparison: nl
        #       {statement} nl
        # colon & nl = tab_indent_begin
        elif self.check_token(TokenType.IF) or \
             self.check_token(TokenType.ELIF) or \
             self.check_token(TokenType.ELSE) or \
             self.check_token(TokenType.WHILE):

            if not self.check_token(TokenType.ELSE):
                self.next_token()
                self.comparison()
            else:
                self.next_token()

            self.match_token(TokenType.COLON)
            self.match_token(TokenType.NEWLINE)
            self.match_token(TokenType.TAB_INDENT_BEGIN)
            while not self.check_token(TokenType.TAB_INDENT_END):
                self.statement()
            self.match_token(TokenType.TAB_INDENT_END)
            self.skip_nl_after_tab_end = True
        # identifier
        #   e.g. x = {expression}
        elif self.check_token(TokenType.IDENTIFIER):
            self.next_token()
            self.match_token(TokenType.IDENTIFIER)
            self.match_token(TokenType.EQUAL)
            self.expression()
        else:
            if not self.check_token(TokenType.NEWLINE):
                self.abort(f'Invalid statement: {self.current_token.text} : {self.current_token.kind.name}')

        # new line
        if self.skip_nl_after_tab_end:
            self.skip_nl_after_tab_end = False
        else:
            self.nl()

    # new line
    def nl(self):
        self.match_token(TokenType.NEWLINE)
        while self.check_token(TokenType.NEWLINE):
            self.next_token()

    """
    Expression needs to have some grammar rules. This is build based on tree.
    Operators with higher priority are lower in the tree (closest to the leaves).
    e.g. the unary operator (negation) has the higest priority (lowest in the tree),
    then are MUL and DIV, then ADD and SUB. It should ensure the order of operations.
    {term} (plus/minus {term}) <== brackets () ensure that we have more that 1 expression
    e.g. 3 + 4 - 5
    Inside the term is higer priority operators
    """
    def expression(self):
        self.term()
        while self.check_token(TokenType.PLUS) or self.check_token(TokenType.MINUS):
            self.next_token()
            self.term()

    """
    Term is a higer priority operators like * or /
    """
    def term(self):
        self.unary()
        while self.check_token(TokenType.ASTERISK) or self.check_token(TokenType.SLASH):
            self.next_token()
            self.unary()

    """
    Unary is a one-argument-operator like + or -
    That can change a number e.g. from positive to negative number
    """
    def unary(self):
        if self.check_token(TokenType.PLUS) or self.check_token(TokenType.MINUS):
            self.next_token()
        self.primary()

    """
    Primary is a number or identifier token (var name)
    """
    def primary(self):
        if self.check_token(TokenType.NUMBER):
            self.next_token()
        elif self.check_token(TokenType.IDENTIFIER):
            self.next_token()
        else:
            self.abort(f'Unrecognized token: {self.current_token.text}')

    """
    Comparison requires following comparison operators: ==, !=, >, >=, < and <=
    and are allowed i.e. for IF or WHILE statements.
    On the left and on the right sides of the comparison operators is an expression.
    TODO: if not {expression} {operator} {expression} <== NOTEQUAL in py
    """
    def comparison(self):
        self.expression()
        if not self.is_comparison_operator():
            self.abort(f'Expected comparison operator! Got: {self.current_token.text}')
        self.next_token()
        self.expression()

        while self.is_comparison_operator():
            self.next_token()
            self.expression()

    def is_comparison_operator(self):
        return self.check_token(TokenType.GRATERTHAN) or self.check_token(TokenType.GRATERTHAN_EQUAL) \
            or self.check_token(TokenType.LESSTHAN) or self.check_token(TokenType.LESSTHAN_EQUAL) \
            or self.check_token(TokenType.EQUAL)
