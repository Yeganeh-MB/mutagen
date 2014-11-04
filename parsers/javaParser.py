__author__ = 'Velz'


class JavaParser:
    """
    Parser for Java code file.
    Remembers variables declared in the file.
    Each parsed line
    """

    # # constants for comparison during parsing
    # _JAVA_KEYWORDS = ('for', 'while')
    # _JAVA_TYPES = ('boolean', 'int', 'double', 'float')
    # _JAVA_OPERATORS =  ('+', '-', '/', '*', '%',
    #                     '>', '<', '<=', '>=', '==', '!=',
    #                     '&&', '||')

    def __init__(self, file):
        self.file = file
        self.fileHandler = None
        # self.variables = {}

    #TODO: implement via decorator
    def __enter__(self):
        try:
            self.fileHandler = open(self.file, 'r', encoding = 'utf-8')
        except FileNotFoundError:
            print('File {0} does not exist. Please, check the path.'.format(self.file))
        return self

    #TODO: implement via decorator
    def __exit__(self, type, value, traceback):
        if self.fileHandler:
            self.fileHandler.close()

    def parseLines(self):
        if self.fileHandler:
            for line in self.fileHandler:
                yield self._parse(line)


    def _parse(self, line):
        line = line.strip()
        return (line, len(line))