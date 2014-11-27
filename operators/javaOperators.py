__author__ = 'Yeganeh'


"""
Mutation Operators for Java code

implemented:
  LCR - logical connector replacement
  ABS - absolute value insertion
  UOI - unary operator insertion
  AOR - arithmetic operator replacement
  ROR - relatinal operator replacement
"""

def  LCR(filename, operators):
    """
    Logical Connector Replacement mutation operator 
    Changes || to && and vice versa
    """

    mutantsCount = 0

    if '||' in operators.keys() or '&&' in operators.keys():
        with open(filename + '.java', 'r') as infile:
            content = infile.read()

    if '||' in operators.keys():
        for position in operators['||']:
            with open('LCR_mutant_{0}_{1}.java'.format(mutantsCount+1, filename), 'w') as outfile:
                outfile.write( content[:position - 1] + '&&' + content[position + 1:] )
            mutantsCount += 1

    if '&&' in operators.keys():
        for position in operators['&&']:
            with open('LCR_mutant_{0}_{1}.java'.format(mutantsCount+1, filename), 'w') as outfile:
                outfile.write( content[:position - 1] + '||' + content[position + 1:] )
            mutantsCount += 1

    print('LCR mutation finished. Mutants generated: {0}'.format(mutantsCount))
    
    
def  AOR(filename, operators):
    """
    Orarithmetic Replacement mutation operator 
    Changes + to - and vice versa
    And changes * to / and vice versa
    """

    mutantsCount = 0

    if '+' in operators.keys() or '-' in operators.keys() or '/' in operators.keys() or '*' in operators.keys():
        with open(filename + '.java', 'r') as infile:
            content = infile.read()
            
    

    if '-' in operators.keys():
        for position in operators['-']:
            with open('AOR_mutant_{0}_{1}.java'.format(mutantsCount+1, filename), 'w') as outfile:
                outfile.write( content[:position - 1] + '+' + content[position + 1:] )
            mutantsCount += 1

    if '+' in operators.keys():
        for position in operators['+']:
            with open('AOR_mutant_{0}_{1}.java'.format(mutantsCount+1, filename), 'w') as outfile:
                outfile.write( content[:position - 1] + '-' + content[position:] )
            mutantsCount += 1
            
    if '*' in operators.keys():
        for position in operators['*']:
            with open('AOR_mutant_{0}_{1}.java'.format(mutantsCount+1, filename), 'w') as outfile:
                outfile.write( content[:position - 1] + '/' + content[position:] )
            mutantsCount += 1

    if '/' in operators.keys():
        for position in operators['/']:
            with open('AOR_mutant_{0}_{1}.java'.format(mutantsCount+1, filename), 'w') as outfile:
                outfile.write( content[:position - 1] + '*' + content[position:] )
            mutantsCount += 1        

    

    print('AOR mutation finished. Mutants generated: {0}'.format(mutantsCount))
    
    
def  ROR(filename, operators):   
    """
    Relatinal Replacement mutation operator 
    Changes < to > and vice versa
    And changes =< to >= and vice versa
    """

    mutantsCount = 0

    if '<' in operators.keys() or '>' in operators.keys() or '>=' in operators.keys() or '=<' in operators.keys():
        with open(filename + '.java', 'r') as infile:
            content = infile.read()

    if '>' in operators.keys():
        for position in operators['>']:
            with open('ROR_mutant_{0}_{1}.java'.format(mutantsCount+1, filename), 'w') as outfile:
                outfile.write( content[:position - 1] + '<' + content[position :] )
            mutantsCount += 1

    if '<' in operators.keys():
        for position in operators['<']:
            with open('ROR_mutant_{0}_{1}.java'.format(mutantsCount+1, filename), 'w') as outfile:
                outfile.write( content[:position - 1] + '>' + content[position :] )
            mutantsCount += 1

    if '=<' in operators.keys():
        for position in operators['=<']:
            with open('ROR_mutant_{0}_{1}.java'.format(mutantsCount+1, filename), 'w') as outfile:
                outfile.write( content[:position - 1] + '>=' + content[position + 1:] )
            mutantsCount += 1

    if '>=' in operators.keys():
        for position in operators['>=']:
            with open('ROR_mutant_{0}_{1}.java'.format(mutantsCount+1, filename), 'w') as outfile:
                outfile.write( content[:position - 1] + '=<' + content[position + 1:] )
            mutantsCount += 1

    print('ROR mutation finished. Mutants generated: {0}'.format(mutantsCount))


