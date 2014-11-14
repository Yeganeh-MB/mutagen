__author__ = 'Velz'


from parsers.javaParser import JavaParser

if __name__ == '__main__':
    parser = JavaParser()

    a = parser.parse('test.txt')
    print('Types: {0}\nOperators: {1}\nStrings: {2}\nNumbes: {3}\nTokens: {4}'.format(a['types'], a['operators'], a['strings'], a['numbers'], a['tokens']))