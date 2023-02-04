import enum
import sys

class Lexer():
    def __init__(self, input):
        self.source = input + '\n'
        self.current_char = ''
        self.current_position = -1
        self.next_char()

    def next_char(self):
        self.current_position += 1
        if self.current_position >= len(self.source):
            self.current_char = '\0'
        else:
            self.current_char = self.source[self.current_position]

    def peek_next_char(self):
        if self.current_position + 1 >= len(self.source):
            return '\0'
        return self.source[self.current_position+1]

    def abort(self, msg):
        sys.exit("Lexer error: " + msg)

    def skip_whitespace(self):
        while self.current_char == ' ' or self.current_char == '\t' or self.current_char == '\r':
            self.next_char()

    def skip_comment(self):
        if self.current_char == '#':
            while self.current_char != '\n':
                self.next_char()

    def get_token(self):
        self.skip_whitespace()
        self.skip_comment()

        token = None

        # simple arthmetic operators
        if self.current_char == '+':
            token = Token(self.current_char, TokenType.PLUS)
        elif self.current_char == '-':
            token = Token(self.current_char, TokenType.MINUS)
        elif self.current_char == '*':
            token = Token(self.current_char, TokenType.ASTERISK)
        elif self.current_char == '/':
            token = Token(self.current_char, TokenType.SLASH)
        
        # double operators
        elif self.current_char == '=':
            first_char = self.current_char
            if self.peek_next_char() == '=':
                self.next_char()
                token = Token(first_char + self.current_char, TokenType.DUALEQUAL)
            else:
                token = Token(self.current_char, TokenType.EQUAL)
        elif self.current_char == '>':
            first_char = self.current_char
            if self.peek_next_char() == '=':
                self.next_char()
                token = Token(first_char + self.current_char, TokenType.GRATERTHAN_EQUAL)
            elif self.peek_next_char() == '>':
                self.next_char()
                token = Token(first_char + self.current_char, TokenType.SHIFTRIGHT)
            else:
                token = Token(self.current_char, TokenType.GRATERTHAN)
        elif self.current_char == '<':
            first_char = self.current_char
            if self.peek_next_char() == '=':
                self.next_char()
                token = Token(first_char + self.current_char, TokenType.LESSTHAN_EQUAL)
            elif self.peek_next_char() == '<':
                self.next_char()
                token = Token(first_char + self.current_char, TokenType.SHIFTLEFT)
            else:
                token = Token(self.current_char, TokenType.LESSTHAN)
        elif self.current_char == '!':
            first_char = self.current_char
            if self.peek_next_char() == '=':
                self.next_char()
                token = Token(first_char + self.current_char, TokenType.NOTEQUAL)
            else:
                token = Token(self.current_char, TokenType.NEGATION)

        # strings
        elif self.current_char == '\"' or self.current_char == '\'':
            self.next_char()
            start_position = self.current_position
            while not (self.current_char == '\"' or self.current_char == '\''):
                self.next_char()
            current_string = self.source[start_position : self.current_position]
            token = Token(current_string, TokenType.STRING)

        # numbers
        elif self.current_char.isdigit():
            start_position = self.current_position
            while self.peek_next_char().isdigit():
                self.next_char()
            if self.peek_next_char() == '.':
                self.next_char()
                if not self.peek_next_char().isdigit():
                    self.abort("Illegal character for number! Char: " + self.peek_next_char())
                while self.peek_next_char().isdigit():
                    self.next_char()
            number = self.source[start_position : self.current_position + 1]
            token = Token(number, TokenType.NUMBER)

        # identifiers and keywords
        elif self.current_char.isalpha():
            start_position = self.current_position
            while self.peek_next_char().isalnum():
                self.next_char()
            
            substring = self.source[start_position : self.current_position + 1]
            keyword = Token.check_keyword(substring)
            if not keyword:
                token = Token(substring, TokenType.IDENTIFIER)
            else:
                token = Token(substring, keyword)

        # special characters
        elif self.current_char == '\n':
            token = Token(self.current_char, TokenType.NEWLINE)
        elif self.current_char == '\0':
            token = Token(self.current_char, TokenType.EOF)
        else:
            self.abort("Unknown token found! Token: " + self.current_char)

        self.next_char()
        return token

class Token():
    def __init__(self, text, kind):
        self.text = text
        self.kind = kind

    def check_keyword(keyword):
        for kind in TokenType:
            if (kind.name.capitalize() == keyword and kind.value > 100 and kind.value < 104) or (kind.name.lower() == keyword and kind.value > 103 and kind.value < 200):
                return kind
        return None

class TokenType(enum.Enum):
    EOF = -1
    NEWLINE = 0
    NUMBER = 1
    STRING = 2
    IDENTIFIER = 4

    # py keywords
    NONE = 101
    TRUE = 102
    FALSE = 103
    AND = 104
    AS = 105
    ASSERT = 106
    ASYNC = 107
    AWAIT = 108
    BREAK = 109
    CLASS = 110
    CONTINUE = 111
    DEF = 112
    DEL = 113
    ELIF = 114
    ELSE = 115
    EXCEPT = 116
    FINALLY = 117
    FOR = 118
    FROM = 119
    GLOBAL = 120
    IF = 121
    IMPORT = 122
    IN = 123
    IS = 124
    LAMBDA = 125
    NONLOCAL = 126
    NOT = 127
    OR = 128
    PASS = 129
    RAISE = 130
    RETURN = 131
    TRY = 132
    WHILE = 133
    WITH = 134
    YIELD = 135

    # operators
    EQUAL = 201
    PLUS = 202
    MINUS = 203
    ASTERISK = 204
    SLASH = 205
    DUALEQUAL = 206
    NOTEQUAL = 207
    LESSTHAN = 208
    LESSTHAN_EQUAL = 209
    GRATERTHAN = 210
    GRATERTHAN_EQUAL = 211
    SHIFTLEFT = 212
    SHIFTRIGHT = 213
    NEGATION = 214
    