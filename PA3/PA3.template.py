from random import randrange as rnd
#The following variable is no longer wrapped inside of a mutable list:
isFilled = True

#The following data structure now has dimensions of 7x6 (as compared to the previous
#homework, which was 6x7). The connect-4 game has no changed it s shape, but we are
#storing the board in transposed form (to make it easier to let a token drop into a
#column). The right-most element of each list-of-6 is the BOTTOM cell of the board's
#corresponding column. Also note that each cell is initialized to TWO spaces:
B=(["  "]*6,["  "]*6,["  "]*6,["  "]*6,["  "]*6,["  "]*6,["  "]*6)

#The following offers the player a choice of words to choose the right token type:
piece={'Filled':'⚫','filled':'⚫','F':'⚫','f':'⚫','⚫':'⚫','Empty':'⚪','empty':'⚪','E':'⚪','e':'⚪','Hollow':'⚪','hollow':'⚪','H':'⚪','h':'⚪','⚪':'⚪','Full':'⚫','full':'⚫'}

def drop(*moves, player='Auto', toggle=True, **kws):
    """This drops one or more tokens into the board. There are many ways to run it:
     
       drop(): By not supplying a move, you are indicating that a random move is to
               be made. If any column is full of tokens, then that column will not 
               be an option for the random column choice. If every column is full,
               then the function returns false.
               When placing the token into the radomly chose column,the token type
               is determined by isFilled. 
               After the token is placed, the isFilled variable will be toggled.

       drop(toggle=True, player='Auto'): This works just the same as drop(), because
               these to arguments are being passed with values that also happen to
               be their default values.

       drop(toggle=false): This works just the same as drop(), except that the 
               isFilled variable will NOT be toggled.

       drop(player='full', toggle=false): This works the same as drop(toggle=False),
               except that the token used is ⚫.

       drop(player='Full'): This works the same as drop(player="full",toggle=False),
               except that, in the end, isFilled==False (The filled token just moved
               and you didn't turn off toggling). 

       drop(announce=True): This works the same as drop(), except that the chosen
               move is announced (ie, printed). Similarly, if no move was possible,
               it will state that fact before it returns False.

       drop(announce=False): This works the same as drop(announce=True). But why? It
               is because I wanted to introduce variable keyword arguments into this
               homework. Therefore, the mere existence of the "announce" keyword is
               what indicates that printing is requested -- not its given value.)

       drop(reset=1, player="E"): This empties the board, sets isFilled to False, 
               and returns true.

       drop(reset=1, player="⚫"): This empties the board, sets isFilled to True, 
               and returns true.

       drop(reset=1): This empties the board and returns true.

       drop(reset=False): This works the same as drop(reset=1), because reset is
               like announce: an extra keyword whose mere existence indicates the
               need to take the action, regardless of the value passed into it.

       drop(7,player='⚪'): This place a ⚪ token into column #7. If this column 
               is full, then it instead returns false. Also, isFilled becomes True, 
               because toggling is on, and the current move was ⚪.

       drop(7,player='⚪',announce=0): This is the same as drop(7,player='⚪'), but
               it also prints the move.

       drop(7,player='⚪',announce=0,reset=False): This is the same as drop(reset=1)
               because reset takes precedence.

       drop(1,2,3,4,5,6,7,player='h',announce=0): This places a ⚪ into each column.
               It announces each move. If any column is already full, it announces
               that and then immediatley exits with a False, without finishing the
               rest of the moves (even if some of those future moves would have been
               able to fit).
               When this process finishes, it set isFilled to True (because toggle
               wasn't turned off).

       drop(1,2,3,4,5,6,7,toggle=0,announce=1): This is the same as drop(1,2,3,4,5,
              6,7,player='h',announce=0), except that the token will toggle between
              moves. So, for example, if isFilled began as True, then it will put
              a ⚫ into columns 1,3,5&7 (and it will put a ⚪ into the others). The
              final value of isFilled will be False, since an odd number of moves
              were made."""

    #The 1st line of the function defines the number n, which is the number of moves
    #requested: drop(4,5,6)=> n=3, drop(2)=> n=1, drop()=> n=1, drop(reset=1)=> n=X.
    #the "X" in the last case is because I don't care about the answer in tha case.
    #the "1" in the 2nd-to-last case is because "drop()" indicates one random move.
    #In the following line, you must replace the ... with an expression:
    #print("moves =",moves, "Type of moves =", type(moves), "len = ", len(moves))
    n=len(moves) if len(moves)>0 else 1
    #As for most of the rest of the function, its implementation is up to you.
    #Insert it here:
    global isFilled, B
    
    def boardIsFull():
        for i in range(7):
            for j in range(6):
                if B[i][j] == "  ":
                    return False
        return True

    if len(kws) == 2:
        announce = True
        reset = True
    elif len(kws) == 1:
        if [*kws][0] == 'announce':
            announce = True
            reset = False
        else:
            announce = False
            reset = True
    else:
        announce = False
        reset = False

    if reset:
        B=(["  "]*6,["  "]*6,["  "]*6,["  "]*6,["  "]*6,["  "]*6,["  "]*6)
        if piece[player] == '⚫':
            isFilled = True
        elif piece[player] == '⚪':
            isFilled = False
        return True

    if player == 'Auto':
        token = '⚫' if isFilled else '⚪'
    else:
        token = piece[player]
    
    if n == 1:
        if len(moves) == 0:
            if boardIsFull():
                if announce:
                    print("The board is full, so", token, "cannot randomly place.")
                return False
            while True:
                c = rnd(1, 8)
                insert = -1
                for i in range(0, 6):
                    if B[c-1][i] == "  ":
                        insert = i
                if insert != -1:
                    break
        else:
            c = moves[0]
            if boardIsFull():
                if announce:
                    print("The board is full, so ", token, " cannot place into column", c, ".", sep = '')
                return False
            insert = -1
            for i in range(0, 6):
                if B[c-1][i] == "  ":
                    insert = i
            if insert == -1:
                if announce:
                    print("Column", c, "is full, so", token, "cannot place into it.")
                return False
    else:
        if toggle and player == 'Auto':
            toggle = True
        elif toggle and player != 'Auto':
            toggle = False
        elif not toggle and player == 'Auto':
            toggle = False
        else:
            toggle = False
        for i in moves:
            if not drop(i, player=player, toggle=toggle, **kws):
                return False
        return True
          
    if announce:
        print(token, " places into column ", c, ".", sep='')
                

    #The last three lines of the function must obey some rules, however.
    #At this end part, the variable "c" should hold the column number (0<c<8), and
    #the variable "token" should hold the token type (either: ⚪ or ⚫).
    #
    #The 3rd-to-last line must accomplish the inserting of the identified token,
    #by filling in the ... below (of course you can also add tabs at the front):
    B[c-1][insert]=token
      #Hint:B[c-1] is a list representing a column, with the right-most entry being
      #the bottom of that column. In the connect-4 game, gavity will drop the token
      #into bottom-most *empty* spot (empty means "contains a '  '"). If we wanted 
      #to find the first empty spot it would be esier, because index does that. But
      #is there is a way to flip it around and let .index() work nonetheless?
    #
    #The 2nd-to-last must accomplish the toggling of IsFilled, by replacing the ...
    #with an expression: 
    if toggle: isFilled = not isFilled
    #
    #The last line:
    return True
    

def wrapper_drop(*moves, player='Auto', toggle=True, **kws):
    """This function only does two things. It prints "Wrapper:", and it calls drop,
    passing on its arguments as-is."""
    print("Wrapper: ",end="")
    drop(*moves, player=player, toggle=toggle, **kws)

def display():
    """This function displays the board in a pretty format (on my computer). I'm
    sorry if it isn't as pretty on your computer, but you can still do the program,
    even if it looks a little ugly on your screen."""
    #Line 1: This uses zip to create a transposed version of B.
    transB = tuple(zip(B[0],B[1],B[2],B[3],B[4],B[5],B[6]))
    #Line 2:
    print("┌──┬──┬──┬──┬──┬──┬──┐")
    #Line 3:
    for i in range(6):
        #Line 4. Fill in the ... to print out a row of tokens, in a format like
        #        this:  "|⚪|  |⚪|⚪|  |  |⚫|"
        print("",*transB[i],"", sep='|')
        #Line 5:
        if i==5: break
        #Line 6:
        print("├──┼──┼──┼──┼──┼──┼──┤")
    #Line 7:
    print("└──┴──┴──┴──┴──┴──┴──┘")

if (__name__ == "__main__"):
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
