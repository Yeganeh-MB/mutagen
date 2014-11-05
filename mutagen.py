__author__ = 'Velz'

from parsers.javaParser import JavaParser

if __name__ == '__main__':
    parser = JavaParser()

    a = parser.parse('test.txt');
    print('Types: {0}\nOperators: {1}\nTokens: {2}'.format(a['types'], a['operators'], a['tokens']))