###############################################################################
# There are 6 places below labeled "Add something here". Fill in those 6 places
# to complete the assignment. When you are done, rename this file to "PA6.py"
# and submit to the cyberunversity by Friday, May 28th, at 11:59pm.
###############################################################################
from functools import reduce, partial
from itertools import zip_longest
from operator import concat, eq, mul
from collections import ChainMap
from copy import copy
from random import randrange as rnd
from numpy import transpose

class Connect4():
    p=ChainMap(dict(zip_longest({'⚪','e','E','h','H','o','O','empty','hollow',
                                 'open','Empty','Hollow','Open','EMPTY','OPEN',
                                 'HOLLOW'},{},fillvalue='⚪')),
               dict(zip_longest({'⚫','c','C','f','F','closed','filled','full',
                                 'fill','Closed','Filled','Full','Fill','FULL',
                                 'FILL','CLOSED','FILLED'},{},fillvalue='⚫')))

# Add something here #1 #######################################################
# A class function "token(piece)" that identifies the token type ('⚪' or '⚫')
# of the string piece. That is: it looks for piece in Connect4's dictionary p.
# return the type, if found. If not, raise TypeError with a meaningful message.
# Q: Why not just access p directly? A:Because we'll later be making p private.
#
# Note: class functions don't get the "self" parameter.
###############################################################################
    def token(piece):
        try:
            return Connect4.p[piece]
        except:
            raise TypeError("There's not a type called" + piece)

# Add something here #2 #######################################################
# The __init__ constructor method that creates the board instance attribute and
# the isFilled instance attribute which keeps track of whose move it is.
#
# As for the board, create it exactly like in the last homework (using tuple,
# map, and copy)
#
# As for the isFilled attribute, it is still a boolean, but now it is set based
# on an argument that the user can optionally pass into the constructor. This
# argument must then be passed token() class function to determine the piece.
# If no argument is passed to the constructor, then the default token type is
# filled.
#
# Note, when calling a class function, such as token(), you do need to call it
# as a class function, and not as an instance method.
###############################################################################
    def __init__(self, piece='filled'):
        self.B=tuple(map(copy,[["  "]*6]*7))
        self.isFilled = (Connect4.token(piece) == '⚫')

# Add something here #3 #######################################################
# The __str__ method for printing the board. It must RETURN the print string,
# not print anything itself. The returned string must look the same as in the
# previous homework -- but, since we can't use print, this string will need to
# be created in a new way. That new way is to: 1) create a tuple of the rows,
# 2) use repr to turn each of those rows into a string, 3) use the str.replace
# method multiple times to make the string look like how it should print, 4)
# also add in the horizontal grid lines that go between the rows.
#
# Note: When a tuple converts to a string, the elements are separated by a
# ", ". Your calls to replace should not confuse these separating spaces with
# with the spaces used to indicate empty board positions (ie, the "  "s). It
# is easy to not confuse them if you use ", " as the replacement string.
###############################################################################
    def __str__(self):
        t=tuple(zip(*self.B))
        s = "┌──┬──┬──┬──┬──┬──┬──┐\n"
        for i in range(len(t)):
            r=repr(t[i]).replace('(','|')
            r=r.replace(')','|')
            r=r.replace('\'','')
            r=r.replace(', ','|')
            if i < 5:
                s += r + "\n├──┼──┼──┼──┼──┼──┼──┤\n"
            else:
                s += r + '\n'
        s += "└──┴──┴──┴──┴──┴──┴──┘"
        return s    

# Add something here #4 #######################################################
# The __contains__ method receives a column numbered between 1-7. It returns
# True if the coresponding column has room in it for a token.
#
# Note: This means that "g=Connect4();print(2 in g)" will print "True".
###############################################################################
    def __contains__(self, c):
        return self.B[c-1][0] == '  '

# Add something here #5 #######################################################
# The __setitem__ method receives a column numbered between 1-7 and a token to
# insert into that column. If the column is full, raise an error. Otherwise add
# the token to the column using the same technique as in the last homework.
###############################################################################
    def __setitem__(self, c, token):
        try:
            self.B[c-1][5-[*reversed(self.B[c-1])].index('  ')]=token
        except:
            raise Exception("Error")
    def drop(self, *mvs, player='Auto', toggle=True, **kws):
        mvs=list(mvs)
        n=kws["numMoves"] if "numMoves" in kws else len(mvs) if len(mvs) else 1

        for l in range(n):
            token = '⚪⚫'[self.isFilled]\
                    if player=='Auto' else Connect4.token(player)
            if len(mvs) == 0:
                try:
                    mvs=[int((y1:=reduce(concat,map(str,(filter(None,map(mul,
                                         map(eq,transpose(self.B)[0],['  ']*7),
                                             range(1,8)))))))[rnd(len(y1))])]
                except:
                    if "announce" in kws:
                        print("Board's full, so",token,"can't randomly place.")
                        return False
            c=mvs.pop(0)
            try:
# Add something here #6 #######################################################
#               Add a line here that indirectly uses __setitem__ to assign the
#               token to column c.  Note: you cannot use the word "setitem".
##############################################################################
                self[c]=token
            except:
                if "announce" in kws:
                    print(token,"was unable to place into column",str(c)+".")
                    return False
            if "announce" in kws:
                print(token,"places into column",str(c)+".")
            if toggle: self.isFilled ^=1
    
b=Connect4()
b.drop(1,toggle=False,announce=True)
b.drop(1,toggle=False,announce=True)
b.drop(1,announce=True)
b.drop(1,toggle=False,announce=False)
b.drop(7,player='⚫',toggle=False,announce=False)
b.drop(7,toggle=False,announce=False)
b.drop(7,toggle=False,announce=False)
b.drop(7,player='⚫',announce=False)
b.drop(7,player='⚫',announce=False)
print(b)
print ("7 in b: ", 7 in b)
b.drop(7,player='⚫',announce=False)
print(b)
print ("7 in b: ", 7 in b)
b.drop(2,3,4,5,6,announce=True)
b.drop(2,3,4,5,6,toggle=False,announce=True)
b.drop(2,3,4,5,6,player="empty",announce=True)
b.drop(2,3,4,5,6,player="Filled",announce=True)
print(b)
b.drop(announce=True)
b.drop(announce=True)
b.drop(announce=True)
b.drop(announce=True)
b.drop(announce=True)
b.drop(announce=True)
b.drop(announce=True)
b.drop(announce=True)
b.drop(announce=True)
b.drop(announce=True)
b.drop(announce=True)
b.drop(announce=True)
b.drop(announce=True)
b.drop(announce=True)
print(b)

