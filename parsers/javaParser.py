__author__ = 'Velz'


class JavaParser:
    """
    parser for Java code file
    """

    def parse(self, file):
        tokens = self.tokenize(file)
        structure = self.analyze(tokens)
        return structure

    # TODO: add power operator...
    def tokenize(self, file):
        """
        reads a file and store each component together with its position
        """
        OPERANDS = ('+', '-', '*', '/', '%', '>', '<', '=', '&', '|', '!')
        SKIP = ('(', ')', '{', '}', ' ', '\n', '\t')
        DELIMITERS = (',', ';')
        tokens = []

        with open(file, 'r', encoding = 'utf-8') as src:
            char = src.read(1)

            while True:
                token = ''
                position = 0

                while char in SKIP:
                    char = src.read(1)

                if char and char == ',':
                    position = src.tell()
                    token += char
                    char = src.read(1)
                elif char and char == '"':
                    position = src.tell()
                    token += char
                    char = src.read(1)

                    while char and char != '"':
                        token += char
                        char = src.read(1)

                    token += char
                    char = src.read(1)
                elif char and char in OPERANDS:
                    position = src.tell()

                    while char and char in OPERANDS:
                        token += char
                        char = src.read(1)
                elif char and char in DELIMITERS:
                    position = src.tell()
                    token += char
                    char = src.read(1)
                elif char:
                    position = src.tell()

                    while char and char not in OPERANDS and char not in SKIP and char not in DELIMITERS:
                        token += char
                        char = src.read(1)
                else: # end of file...
                    break

                tokens.append([token, position])

        return tokens

    def analyze(self, tokens):
        """
        analyzes the parsed structure and separates variables with
        their names, variables occurrences, and target operators
        """
        OPERATORS = ('==', '!=', '>', '<', '>=', '<=', '+', '-', '*', '/', '%', '!', '&&', '||')
        RESERVED = ('abstract', 'assert', 'break', 'case', 'catch', 'char', 'class',
                    'const', 'continue', 'default', 'do', 'else', 'enum', 'extends',
                    'final', 'finally', 'for', 'goto', 'if', 'implements', 'instanceof',
                    'interface', 'native', 'new', 'package', 'private', 'protected',
                    'public', 'return', 'static', 'strictfp', 'super', 'switch', 'this',
                    'synchronized', 'throw', 'throws', 'transient', 'try', 'void', 'violate',
                    'while')
        types = {}
        operators = {}
        others = {}
        currentType = None
        expectDeclaration = False

        def isTypeName(name):
            """
            check whether the name is either of a primitive type or a class instance

            assumption: names of classes start with a capital letter
                        names of constants are capitalized
                        names of variables start with a small letter
                        names of methods start with a small letter
            """
            _PRIMITIVE_TYPES = ('int', 'float', 'double', 'boolean', 'byte', 'long', 'short')
            return name in _PRIMITIVE_TYPES

        def addTokenToDict(dict, token):
            key = token[0]
            val = token[1]

            if key not in dict.keys():
                dict[key] = []

            dict[key].append(val)

        for token in tokens:
            if token[0] in OPERATORS:
                addTokenToDict(operators, token)
            elif isTypeName(token[0]):
                currentType = token[0]
                expectDeclaration = True
            elif expectDeclaration and token[0] not in RESERVED:
                addTokenToDict(types, (currentType, token[0]))
                expectDeclaration = False
            elif currentType and token[0] == ',':
                expectDeclaration = True
            elif currentType and token[0] == ';':
                currentType = False
                expectDeclaration = False
            elif token[0] not in RESERVED:
                addTokenToDict(others, token)

        return {'types': types, 'operators': operators, 'tokens': others}

if __name__ == '__main__':
    parser = JavaParser()
    print( parser.parse('test.txt') )
    # print('types: {0}\noperators: {1}\nother: {2}'.format(a,b,c))