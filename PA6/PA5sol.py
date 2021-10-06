from functools import reduce, partial
from itertools import zip_longest
from operator import concat, eq, mul
from collections import ChainMap
from copy import copy
from random import randrange as rnd
from numpy import transpose
isFilled = True

B=tuple(map(copy,[["  "]*6]*7)) #This creates the exact same B as in PA4, but it creates it in a new way.
# PA4 had: B=(["  "]*6,["  "]*6,["  "]*6,["  "]*6,["  "]*6,["  "]*6,["  "]*6)
# As you can see, each of the seven items was created individually. We couldn't
# use *7, because then the items would have been the same item (what this means
# a you B must be defined such that the test "B[0] is B[1]" returns false).
#
# But wait. Now we learned about the copy function of the copy module. (We also
# learned about deepcopy, but the B object is not so deep as to need that much
# copying power.)
#
# So the rule of the new "B=..." is that your ... may only use one comma (it
# will separate the two arguments of a "map(.., ..)").



emptyNames=frozenset({'E','e','Empty','empty','EMPTY','H','h','Hollow','hollow','HOLLOW','O','o','Open','open','OPEN','⚪'})
fullNames=frozenset({'F','f','Full','full','FULL','Filled','filled','FILLED','Fill','fill','FILL','c','C','Closed','closed','CLOSED','⚫'})
# PA4 had: piece={'Filled':'⚫','filled':'⚫','F':'⚫','f':'⚫','⚫':'⚫','Empty':'⚪','empty':'⚪','E':'⚪','e':'⚪','Hollow':'⚪','hollow':'⚪','H':'⚪','h':'⚪','⚪':'⚪','Full':'⚫','full':'⚫'}
piece=ChainMap(dict(zip_longest(emptyNames,{},fillvalue='⚪')),dict(zip_longest(fullNames,{},fillvalue='⚫')))

def drop(*moves, player='Auto', toggle=True, **kws):
    global isFilled
    moves=list(moves)
    n=kws["numMoves"] if "numMoves" in kws else len(moves) if len(moves) else 1

    for l in range(n):
        token = '⚪⚫'[isFilled] if player=='Auto' else piece[player]
        if len(moves) == 0:
            try:
                moves=[int((y1:=reduce(concat,map(str,(filter(None,map(mul,map(eq,transpose(B)[0],['  ']*7),range(1,8)))))))[rnd(len(y1))])]
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
    printrow=partial(print,"",sep="|",end="|\n")
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

