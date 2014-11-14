__author__ = 'Yeganeh'

class LogicalMutation
"""
change the operations && to || and vice versa
"""
def ChangeOrtoAnd(file,Row,Column,OutputFile):
"""
Read the file, saving in the tuple, put the tuple in list,
change the character in given positions (in list), change the tuple,
write the new version in the file
"""
    
    f.open(file,'r')
    lines=tuple(f)
    f.close()
    new=list(lines[Row])
    new[Column]='|'
    new[Column+1]='|'
    lines[i].replace(lines[i],''.joint(new))

    f2=open(OutputFile,'w')
    for t in lines:
        line=''.join(str(x) for x in t)
        f2.write(line)


    f2.close();

def ChangeAndtoOr(file,Row,Column,OutputFile):
    
"""
Read the file, saving in the tuple, put the tuple in list,
change the character in given positions (in list), change the tuple,
write the new version in the file
"""
    
    f.open(file,'r')
    lines=tuple(f)
    f.close()
    new=list(lines[Row])
    new[Column]='&'
    new[Column+1]='&'
    lines[i].replace(lines[i],''.joint(new))

    f2=open(OutputFile,'w')
    for t in lines:
        line=''.join(str(x) for x in t)
        f2.write(line)


    f2.close();

    
    
