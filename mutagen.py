__author__ = 'Velz'

from parsers.javaParser import JavaParser

if __name__ == '__main__':
    fileParser = JavaParser('test.txt')

    with fileParser as srcFile:
        for text,length in srcFile.parseLines():
            print('{0} | {1}'.format(text, length))