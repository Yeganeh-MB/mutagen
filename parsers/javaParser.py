__author__ = 'Velz'


class JavaParser:
    """
    Parser for Java code file.
    Remembers variables declared in the file.
    """

    def parse(self, file):
        _OPERANDS = ('+', '-', '*', '/', '%', '>', '<', '=', '&', '|', '!')
        _SKIP = ('(', ')', '{', '}', ' ', '\n', '\t')
        _DELIMITERS = (',', ';')
        words = []

        with open(file, 'r', encoding = 'utf-8') as src:
            char = src.read(1)

            while True:
                word = ''

                while char in _SKIP:
                    char = src.read(1)

                if char and char == ',':
                    word += char
                    char = src.read(1)
                elif char and char == '"':
                    char = src.read(1)

                    while char and char != '"':
                        char = src.read(1)

                    char = src.read(1)
                elif char and char in _OPERANDS:
                    while char and char in _OPERANDS:
                        word += char
                        char = src.read(1)
                elif char and char in _DELIMITERS:
                    word += char
                    char = src.read(1)
                elif char:
                    while char and char not in _OPERANDS and char not in _SKIP and char not in _DELIMITERS:
                        word += char
                        char = src.read(1)
                else: # end of file...
                    break

                if word:
                    print(word)
                    words.append(word)

        return words


if __name__ == '__main__':
    parser = JavaParser()

    parser.parse('test.txt');