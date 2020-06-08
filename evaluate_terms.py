def eval_depth0(string,mode):
    if mode==0:
        add=string.split('+')
        multiply=[add[i].split('*')for i in range(len(add))]
        for i in range(len(multiply)):
            for j in range(len(multiply[i])):
                multiply[i][j]=int(multiply[i][j])
        for i in range(len(multiply)):
            start=1
            for j in multiply[i]:
                start *= j
            multiply[i]=start
        start=0
        for i in multiply:
            start += i
        return start
    if mode==1:
        add=string.split('+')
        multiply=[add[i].split('*')for i in range(len(add))]
        for i in range(len(multiply)):
            for j in range(len(multiply[i])):
                multiply[i][j]=int(multiply[i][j])
        for i in range(len(multiply)):
            start=0
            for j in multiply[i]:
                start += j
            multiply[i]=start
        return max(multiply)
    if mode==-1:
        add=string.split('+')
        multiply=[add[i].split('*')for i in range(len(add))]
        for i in range(len(multiply)):
            for j in range(len(multiply[i])):
                multiply[i][j]=int(multiply[i][j])
        for i in range(len(multiply)):
            start=0
            for j in multiply[i]:
                start += j
            multiply[i]=start
        return min(multiply)

def syntaxcheck(exp):
    numbers=['0','1','2','3','4','5','6','7','8','9']
    open_bracket=['(','{','[']
    closed_bracket=[')','}',']']
    operator=['+','*']
    allowed=numbers+open_bracket+closed_bracket+operator
    x=len(exp)
    stack=[]
    for i in exp:
        if i not in allowed:
            return False
    for i in range(len(open_bracket)):
        if exp.count(open_bracket[i])!=exp.count(closed_bracket[i]):
            return False
    if exp[0] in closed_bracket or exp[0] in operator:
        return False
    for i in range(x-1):
        if exp[i] in open_bracket:
            if exp[i+1] in closed_bracket or exp[i+1] in operator:
                return False
        if exp[i] in closed_bracket:
            if exp[i+1] in open_bracket or exp[i+1] in numbers:
                return False
        if exp[i] in operator:
            if exp[i+1] in operator or exp[i+1] in closed_bracket:
                return False
        if exp[i] in numbers:
            if exp[i+1] in open_bracket:
                return False
    if exp[x-1] in open_bracket or exp[x-1] in operator:
        return False
    if exp[x-1] in closed_bracket:
        if exp[x-2] in open_bracket:
            return False
    for i in exp:
        if i in open_bracket:
            stack.append(i)
        elif i in closed_bracket:
            a=stack.pop()
            if i != closed_bracket[open_bracket.index(a)]:
                return False
    return True

def wert(exp,mode):
    listexp=list(exp)
    for i in range(len(listexp)):
        if listexp[i]=='[' or listexp[i]=='{':
            listexp[i]='('
        if listexp[i]==']' or listexp[i]=='}':
            listexp[i]=')'
    exp=''.join(listexp)
    if '(' in exp or ')' in exp:
        a=exp.index(')')
        for i in range(a,-1,-1):
            if exp[i]=='(':
                x=str(eval_depth0(exp[i+1:a],mode))
                exp=exp[0:i]+x+exp[a+1:]
                return wert(exp,mode)
    else:
        return eval_depth0(exp,mode)

def tiefe(exp):
    open_bracket,closed_bracket=['(','{','['],[')','}',']']
    a,L=0,[]
    for i in range(len(exp)):
        if exp[i] in open_bracket:
            a+=1
            L.append(a)
        if exp[i] in closed_bracket:
            a-=1
            L.append(a)
    if len(L)==0:
        return 0
    else:
        return max(L)
        
def evaluate(string,mode):
    if syntaxcheck(string)==False:
        raise Exception("syntaktisch inkorrekt")
    else:
        return (wert(string,mode),tiefe(string))
