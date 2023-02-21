import unittest
import os

from lexer_c import *
from parser_c import *
from emitter_c import *

class PrintLexTest(unittest.TestCase):
    def setUp(self):
        self.input = 'print(\'Hello Compiler!\')'
        self.result = []
        self.expected = [TokenType.PRINT,
                         TokenType.ROUND_BRACKET_OPEN,
                         TokenType.STRING,
                         TokenType.ROUND_BRACKET_CLOSE,
                         TokenType.NEWLINE]

        
        lex = Lexer(self.input)
        token = lex.get_token()
        while token.kind != TokenType.EOF:
            self.result.append(token.kind)
            token = lex.get_token()

    def testPrintLexCountEqual(self):
        self.assertCountEqual(self.result, self.expected)

    def testPrintLexListEqual(self):
        self.assertListEqual(self.result, self.expected)

class PrintEmitTest(unittest.TestCase):
    def setUp(self):
        self.test_file = 'unittests/test_print.c'
        self.input = 'print(\'Hello Compiler!\')'
        self.result = []
        self.expected = [CLangNomen.PRINTF,
                         CLangNomen.ROUND_BRACKET_BEGIN,
                         CLangNomen.DOUBLE_QUOTE,
                         'Hello Compiler!',
                         CLangNomen.NEW_LINE_PRINT,
                         CLangNomen.DOUBLE_QUOTE,
                         CLangNomen.ROUND_BRACKET_END,
                         CLangNomen.SEMICOLON,
                         CLangNomen.NEW_LINE]

        lex = Lexer(self.input)
        emit = Emitter(self.test_file)
        parser = Parser(lex, emit)
        parser.program()
        self.result = emit.getTestOutput()

    def testPrintEmitCountEqual(self):
        self.assertCountEqual(self.result, self.expected)

    def testPrintEmitListEqual(self):
        self.assertListEqual(self.result, self.expected)

if __name__ == '__main__':
    unittest.main()
