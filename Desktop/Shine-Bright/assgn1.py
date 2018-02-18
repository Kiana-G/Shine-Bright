from __future__ import print_function


# A recursive descent parser  Boolean expressions.


# QUESTION 7
# REGULAR Expressions for Tokens
# VAR = [$][A-za-z]*
# NOT = [not]   
# FALSE = [alse]
# TRUE = [true]
# END OF QUESTION 7

EOI = 0
NOT = 1
AND = 2
VAR = 3
TRUE = 4
FALSE = 5
OR = 6
EQ = 7
LP = 8
RP = 9
ERR = 10

#QUESTION 8
# Grammar
# expr ->  NOT expr| stmt 
# stmt -> stmt {AND OR} factor | factor
# factor -> {TRUE FALSE}| ( expr ) | var | assign  
# assign -> VAR = {TRUE FALSE} 
# 


import sys
debug = True

def show(indent,name,s,spp):
    if debug:
        print(indent+name+'("',end='');
        j = len(s)
        for i in range(spp,j):
            print(s[i],sep="",end="")
        print('")',end='\n')
        return
    else:
        return
#end show

def x(indent,name1,name2):
    if debug:
        print(indent+"returned to "+name1+" from "+name2)
    else:
        return
#end x



def EatWhiteSpace(s,spp):
    j = len(s)
    if spp >= j:
        return spp

    while s[spp] == ' ' or s[spp] == '\n':
        spp=spp+1
        if spp >= j:
            break
        
    return spp
#end EatWhiteSpace


# expr ->  NOT expr| stmt 
# function expr ------------------------------------------------------------
def expr(s,spp,indent):
    show(indent,'expr',s,spp)
    indent1 = indent+' '

    token = LookAhead(s,spp)
    if token == NOT:
        spp = ConsumeToken(s,spp)
        res,spp = expr(s,spp,indent1)
        x(indent1,"expr","expr")
        return res,spp
    elif token == stmt:
        spp = ConsumeToken(s,spp)
        res,spp = expr(s,spp,indent1)
        x(indent1,"expr","stmt")
        return res,spp
#end expr

# stmt -> stmt {AND OR} factor | factor
# function stmt --------------------------------------------------------
def stmt(s,spp,indent):
    show(indent,'stmt',s,spp)
    indent1 = indent+' '

    token = LookAhead(s,spp)
    if token == stmt:
        spp = ConsumeToken(s,spp)
        res,spp = expr(s,spp,indent1)
        x(indent1,"stmt","stmt")
        if token == AND or token == OR:
            res,spp = factor(s,spp,indent1)
            x(indent1,"stmt","factor")
            return res,spp
        else:
            return False,spp
    elif token == factor:
        return True,spp
    else:
        return False,spp
 
#end stmt 

# factor -> {TRUE FALSE}| ( expr ) | VAR | assign
# function factor --------------------------------------------- 
def factor(s,spp,indent):
    show(indent,'factor',s,spp)
    indent1 = indent+' '

    
    token = LookAhead(s,spp)
    if token == TRUE or token == FALSE:
        return True,spp
    elif token == LP:
        res,spp = expr(s,spp,indent1)
        x(indent1,"factor","expr")
        if not res:
            return False,spp
        token,spp = NextToken(s,spp);
        return (token == RP),spp
    if token == VAR or token == assign:
        return True,spp
    else:
        return False,spp

#end factor



# assign -> VAR = {TRUE FALSE}
# function assign --------------------------------------------- 
def assign(s,spp,indent):
    show(indent,'assign',s,spp)
    indent1 = indent+' '

    token = LookAhead(s,spp)
    if token == VAR:
        spp = ConsumeToken(s,spp)
        if token == EQ:
            res,spp = expr(s,spp,indent1)
            x(indent1,"assign","factor")
            return res,spp
        else:
            return False,spp
    
#end assign

# the scanner ####################################################

# function LookAhead ------------------------------------------- 
def LookAhead(s,spp):
    j = len(s);
    i = spp
    if i >= j:
        return EOI
    while s[i]==" " or s[i]=="\n":
        i = i+1
        if i >= j:
            return EOI

    if s[i] == "not":
        return NOT
    elif s[i] == "and":
        return AND
    elif x in list(s[i]) in list("$" + x) and x.isalpha():
        return VAR
    elif s[i] == "True":
        return TRUE
    elif s[i] == "FALSE":
        return FALSE
    elif s[i] == "or":
        return OR
    elif s[i] == "=":
        return EQ
    elif s[i] == "(":
        return LP
    elif s[i] == ")":
        return RP
    else:
        return ERR
#end LookAhead


# function NextToken --------------------------------------------- 
def NextToken(s,spp):
    spp1 = spp
    spp = EatWhiteSpace(s,spp)
    j = len(s)
    if spp >= j:
        return ERR,spp1

    if spp >= j:
        return EOI,spp
    elif s[spp] == 'not':
        return NOT,spp+1
    elif s[spp] == "and":
        return AND,spp+1
    elif s[spp] == "or":
        return OR,spp+1
    elif x in list(s[i]) in list("$" + x) and x.isalpha():
        return VAR,spp+1
    elif s[spp] == "True":
        return TRUE,spp+1
    elif s[spp] == "EQ":
        return EQ,spp+1
    elif s[spp] == "False":
        return FALSE,spp+1
    elif s[spp] == "(":
        return LP,spp+1
    elif s[spp] == ")":
        return RP,spp+1
    else:
        return ERR,spp1
#end NUM

def ConsumeToken(s,spp):
    token,spp = NextToken(s,spp)
    return spp
#end ConsumeToken


#main section
s = "not($a)"
res,spp = expr(s,0,"");

# is there a leftover ?
if spp < len(s)-1:
    print("parse Error")
else:
    if res:
        print("parsing OK")
    else:
        print("parse Error")
#end main section
                



