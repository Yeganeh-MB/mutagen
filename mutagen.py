__author__ = 'Velz'


from parsers.javaParser import JavaParser
from operators.javaOperators import LCR

if __name__ == '__main__':
    parser = JavaParser()

    filename = 'test'
    parsedFile = parser.parse(filename + '.java')
    LCR(filename, parsedFile['operators'])
    