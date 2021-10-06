#This programming assignment is due May 18th, at 11:59pm. Save you answer as
#PA5.py, and submit to the cyber university.
#
#This file is a template, containing four ... regions that you need to fill in.
#Your solution must use all of the following imported functions:
from functools import reduce, partial
from itertools import zip_longest
from operator import concat, eq, mul
from collections import ChainMap
from copy import copy
from random import randrange as rnd
from numpy import transpose
isFilled = True

B=tuple(map(copy,[['  ']*6]*7))
#This creates the exact same B as in PA4, but it creates it in a new way.
# PA4 had: B=(["  "]*6,["  "]*6,["  "]*6,["  "]*6,["  "]*6,["  "]*6,["  "]*6)
# As you can see, each of the seven items was created individually. We couldn't
# use *7, because then the items would have been the same item (what this means
# is that your B must be defined in such a way that the test "B[0] is B[1]"
# returns False).
#
# But wait. Now we learned about the copy function of the copy module. (We also
# learned about deepcopy, but the B object is not so deep as to need that much
# copying power.) This could overcome the problem with *7.
#
# So the rule of the new "B=..." is that your ... may only use one comma (it
# will separate the two arguments of a "map(.., ..)").

emptyNames=frozenset({'E','e','Empty','empty','EMPTY','H','h','Hollow','hollow','HOLLOW','O','o','Open','open','OPEN','⚪'})
fullNames=frozenset({'F','f','Full','full','FULL','Filled','filled','FILLED','Fill','fill','FILL','c','C','Closed','closed','CLOSED','⚫'})

piece=dict(ChainMap(dict(zip_longest(emptyNames, '', fillvalue='⚪')), dict(zip_longest(fullNames, '', fillvalue='⚫'))))
#This makes a more-complete version of piece from PA4, using a new way
# (It is "more complete" because emptyNames & fullNames have new name choices.)
# Recall that PA4 only had: piece={'Filled':'⚫','filled':'⚫','F':'⚫','f':'⚫','⚫':'⚫','Empty':'⚪','empty':'⚪','E':'⚪','e':'⚪','Hollow':'⚪','hollow':'⚪','H':'⚪','h':'⚪','⚪':'⚪','Full':'⚫','full':'⚫'}
#
# In this new homework, the "piece=..." cannot use the ":" symbol, and it must
# use the emptyNames & fullNames variables. Your solution must use zip_longest
# and ChainMap.

def drop(*moves, player='Auto', toggle=True, **kws):
    global isFilled
    moves=list(moves)
    n=kws["numMoves"] if "numMoves" in kws else len(moves) if len(moves) else 1

    for l in range(n):
        token = '⚪⚫'[isFilled] if player=='Auto' else piece[player]
        if len(moves) == 0:
            try:
                moves=[int((y:=reduce(concat, map(str, filter(None, map(mul, map(eq, list(transpose(B)[0]), ['  ']*7), range(1,8))))))[rnd(len(y))])]
                #Makes the same random move as PA4 did.
#The first thing we notice above is that it uses an assignment expression, (as
#we learned about in Lecture 11). Using this assignment expression makes sense
#because PA4's solution had recomputed the expression: "reduce(lambda x,y:x+y,
#map(str,(filter(None,map(lambda i:(B[i][0]=='  ')*(i+1),range(7))))))".
#Now, with expression assignments, we can compute it once. But, when compared
#to PA4, we see an extra "(" between the int and reduce, in the above answer
#stub. This extra parenthesis is needed because of the quirky syntax rules
#restricting where and how you can place assignment expressions. (It's the same
#reason why Lecture 9, slide 17 required parentheses in the "if (y:=rnd(9)<5)".
#
#One feature of PA4's solution was its use of lambda functions. For example, it
#used (lambda x,y:x+y,...) because no built-in function would do the job. The
#built-in function "sum" might seem a promising candidate, but (as slide #39 of
#Lecture 11 highlights) it cannot work with strings.
#
#But in lecture 11 we learned how the "operator" module defines functional
#versions of Python's operators. (Eg, Python has "+", "*", "in", "is" and "or" 
#operators, so the operator module has the functions "add", "mul", "contains", 
#"is_", and "or_".)
#
#So, in our new homework, you CANNOT use lambda functions. Instead, you'll use
#the "concat", "eq", and "mul" functions, as imported from the operator module.
#
#PA4's other lambda function ("lambda i:(B[i][0]=='  ')*(i+1)...") has a more
#complicated behavior. But again, the functions provided by the operator module
#can perform the needed computations. With "eq" we can see if B[element]=='  '.
#With "mul" we can perform the (B[element]=='  ')*(i+1). (We don't need to use
#the "add" operator to create (i+1), because we can get the i+1 values by using
#the range() function.
#
#Another requirement of our new homework is to use the transpose function from 
#numpy. This step is necessary in order to be able to reference the top line of
#the connect-4 board as a single row. (What I mean is: B[0] grabs the leftmost
#column of the board, not the topmost row. But if it was transposed, then a [0]
#would get the desired board positions.)
            except:
                if "announce" in kws:
                    print("The board's full, so",token,"can't randomly place.")
                return False
        c=moves.pop(0)
        if '  ' not in B[c-1]:
            if "announce" in kws:
                print(token,"was unable to place into column",str(c)+".")
            return False
        if "announce" in kws:
            print(token,"places into column",str(c)+".")
        B[c-1][5-[*reversed(B[c-1])].index('  ')]=token
        if toggle: isFilled ^=1

def display():
    printrow=partial(print,'', sep='|',end='|\n')#In the code below, the call to print() has been
    #replaced with a call to printrow(), and this new call has fewer arguments.
    r=tuple(zip(*B))
    print("┌──┬──┬──┬──┬──┬──┬──┐")
    for i in range(6):
        printrow(*r[i])
        if i==5: break
        print("├──┼──┼──┼──┼──┼──┼──┤")
    print("└──┴──┴──┴──┴──┴──┴──┘")
    
drop(1,toggle=False,announce=True)
drop(1,toggle=False,announce=True)
drop(1,announce=True)
drop(1,toggle=False,announce=False)
drop(7,player='⚫',toggle=False,announce=False)
drop(7,toggle=False,announce=False)
drop(7,toggle=False,announce=False)
drop(7,player='⚫',announce=False)
drop(7,player='⚫',announce=False)
drop(7,player='⚫',announce=False)
display()
drop(2,3,4,5,6,announce=True)
drop(2,3,4,5,6,toggle=False,announce=True)
drop(2,3,4,5,6,player="empty",announce=True)
drop(2,3,4,5,6,player="Filled",announce=True)
display()
drop(announce=True)
drop(announce=True)
drop(announce=True)
drop(announce=True)
drop(announce=True)
drop(announce=True)
drop(announce=True)
drop(announce=True)
drop(announce=True)
drop(announce=True)
drop(announce=True)
drop(announce=True)
drop(announce=True)
drop(announce=True)
display()

