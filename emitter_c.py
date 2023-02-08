import sys
import os

class Emitter():
    def __init__(self, file_path):
        self.file_path = os.path.join('tests', file_path)
        self.header = ''
        self.code = ''

    def abort(self, msg):
        sys.exit(f"Emitter error: {msg}")

    def emit(self, code):
        self.code += code

    def emit_line(self, code):
        self.code += code + '\n'

    def emit_header(self, code):
        self.header += code + '\n'

    def writeOutput(self):
        with open(self.file_path, 'w') as outputFile:
            outputFile.write(self.header + self.code)
