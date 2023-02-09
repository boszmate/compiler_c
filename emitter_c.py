import sys
import os
import enum

class Emitter():
    def __init__(self, file_path):
        self.file_path = os.path.join('tests', file_path)
        self.code = ''

    def abort(self, msg):
        sys.exit(f"Emitter error: {msg}")

    def writeOutput(self):
        with open(self.file_path, 'w') as outputFile:
            outputFile.write(self.code)

    def emitLine(self, *args):
        for arg in args:
            if type(arg) == str:
                self.code += arg
            else:
                self.code += arg.value

    def emitPreDefinedHeader(self, header):
        self.emitLine(CLangNomen.HASH,
                      CLangNomen.INCLUDE,
                      CLangNomen.SPACE,
                      CLangNomen.ANGLE_BRACKET_BEGIN,
                      header,
                      CLangNomen.ANGLE_BRACKET_END,
                      CLangNomen.NEW_LINE)

    def emitUserHeader(self, header):
        self.emitLine(CLangNomen.HASH,
                      CLangNomen.INCLUDE,
                      CLangNomen.SPACE,
                      CLangNomen.DOUBLE_QUOTE,
                      header,
                      CLangNomen.DOUBLE_QUOTE,
                      CLangNomen.NEW_LINE)

    def emitMainBegin(self):
        self.emitLine(CLangNomen.NEW_LINE,
                      CLangNomen.INTEGER,
                      CLangNomen.SPACE,
                      CLangNomen.MAIN,
                      CLangNomen.ROUND_BRACKET_BEGIN,
                      CLangNomen.VOID,
                      CLangNomen.ROUND_BRACKET_END,
                      CLangNomen.SPACE,
                      CLangNomen.CURLY_BRACKET_BEGIN,
                      CLangNomen.NEW_LINE)

    def emitMainEnd(self):
        self.emitLine(CLangNomen.RETURN,
                      CLangNomen.SPACE,
                      str(0),
                      CLangNomen.SEMICOLON,
                      CLangNomen.NEW_LINE,
                      CLangNomen.CURLY_BRACKET_END,
                      CLangNomen.NEW_LINE)

    # printf("Hello Compiler!\n");
    def emitPrintfString(self, text):
        self.emitLine(CLangNomen.PRINTF,
                      CLangNomen.ROUND_BRACKET_BEGIN,
                      CLangNomen.DOUBLE_QUOTE,
                      text,
                      CLangNomen.NEW_LINE_PRINT,
                      CLangNomen.DOUBLE_QUOTE,
                      CLangNomen.ROUND_BRACKET_END,
                      CLangNomen.SEMICOLON,
                      CLangNomen.NEW_LINE)


    # ('printf(\"%d\\n\", (int)(')
    def emitPrintfExpressionBegin(self):
        self.emitLine(CLangNomen.PRINTF,
                      CLangNomen.ROUND_BRACKET_BEGIN,
                      CLangNomen.DOUBLE_QUOTE,
                      CLangNomen.PERCENT,
                      'd',
                      CLangNomen.NEW_LINE_PRINT,
                      CLangNomen.DOUBLE_QUOTE,
                      CLangNomen.COMMA,
                      CLangNomen.SPACE)

    # ');'
    def emitPrintfExpressionEnd(self):
        self.emitLine(CLangNomen.ROUND_BRACKET_END,
                      CLangNomen.SEMICOLON,
                      CLangNomen.NEW_LINE)

    # 'if ('
    def emitIfStatement(self):
        self.emitLine(CLangNomen.IF,
                      CLangNomen.SPACE,
                      CLangNomen.ROUND_BRACKET_BEGIN)
    # ') {'
    def emitStatementEnd(self):
        self.emitLine(CLangNomen.ROUND_BRACKET_END,
                      CLangNomen.SPACE,
                      CLangNomen.CURLY_BRACKET_BEGIN,
                      CLangNomen.NEW_LINE)

    # '}'
    def emitCloseCurlyBracket(self):
        self.emitLine(CLangNomen.CURLY_BRACKET_END,
                      CLangNomen.NEW_LINE)

    def emitTabSpace(self):
        self.emitLine(CLangNomen.TAB_SPACE)

# C language nomenclature
class CLangNomen(enum.Enum):
    # special char
    NEW_LINE = '\n'
    CURLY_BRACKET_BEGIN = '{'
    CURLY_BRACKET_END = '}'
    ANGLE_BRACKET_BEGIN = '<'
    ANGLE_BRACKET_END = '>'
    ROUND_BRACKET_BEGIN = '('
    ROUND_BRACKET_END = ')'
    TAB_SPACE = '   '
    SPACE = ' '
    HASH = '#'
    DOUBLE_QUOTE = '\"'
    SEMICOLON = ';'
    COMMA = ','
    PERCENT = '%'

    # keywords
    INCLUDE = 'include'
    INTEGER = 'int'
    VOID = 'void'
    MAIN = 'main'
    RETURN = 'return'
    PRINTF = 'printf'
    NEW_LINE_PRINT = '\\n'
    IF = 'if'
