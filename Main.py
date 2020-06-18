from antlr4 import *
from generated.LangLexer import LangLexer
from generated.LangParser import LangParser
from LangVarListener import LangVarListener
import sys


def main():
    orig_stdout = sys.stdout
    # setting up a file where program will translate code to Python
    f = open('python_file.py', 'w')
    sys.stdout = f

    input_stream = FileStream("test1.txt")  # sys.argv[1])

    lexer = LangLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = LangParser(tokens)

    tree = parser.class_def()
    listener = LangVarListener()

    walker = ParseTreeWalker()
    walker.walk(listener, tree)

    # start
    init = "\nif __name__ == '__main__':\n\tmain()"
    print(init)

    sys.stdout = orig_stdout
    f.close()


if __name__ == '__main__':
    main()
