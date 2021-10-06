isFilled = [False]
__doc__="""This module contains methods for handling a connect-4 board.
Connect-4 is a game where players drop tokens into one of 7 slots. These 7
slots go to the columns of a vertical playing board. Because the board is
vertical, the tokens will fill up the columns from the bottom. The playing
board is 6 rows high. The goal of connect-4 is to get a line of 4 tokens
(ie, to "connect four"), but we won't worry about winning the game, in this
programming assignment.

This module contains methods to reset the board, to insert a token into the
board, and to print the board. It also contains some top-level code that
creates an empty board when first loaded (ie, imported). 

This module also has 2 attributes:
 "B": This is a list of 6 elements. Each of those elements is itself a list
      of 7 elements (which are 1-character-long strings).
      In other words, B indicates what is at various board positions. Each
      of the positions may hold one of 3 things: a filled circle '●', a 
      hollow circle '○', or an empty space ' '. (Note: on some systems, the
      '●', and '○' symbols may print wider than the ' ' symbol prints, thus
      causing the printBoard() method to display in an unalligned way. If 
      you see this happening on your computer, then replace every ' ' in 
      your code with a '　' character, which is UNICODE value 12288.)
 "isFilled": This is a list containing a boolean. The boolean indicates the
      token piece that is currently making its move. If isFilled's boolean
      is true, then inserting a token into the board will insert a '●'.

There are many rules that you need to follow in your implementation:

 1. You cannot cheat and cannot look at another student's code.

 2. You must follow the instructions posted in the PA2.txt file, which is
    was posted to the cyberuniversity along with this connect4.py file.

 3. You must add your code into the spaces below, leaving all of the doc
    strings unchanged.

 4. You can only use commands that we have learned in the first 4 lectures.
    So you cannot use loops, if-structures or the global statement. And so:

       Conditional Execution: Must be achieved by using non-booleans within
                              logic expressions that calculate the desired
                              values (as described in Lecture 4).
       Modifying Global Vars: Python has rules (that we haven't learned) on 
                              writing to nonlocal variables. So we simply
                              won't *over-write* this module's attributes
                              from within any of the methods. 
                              But just because we won't *over-write* these
                              attributes, it doesn't mean we can't read or
                              update them. Both our attributes are lists,
                              which can be updated. This is particularly
                              notable for "isFilled", which is an immutable
                              boolean, wrapped into a mutable list.
       Repetition:            Can only be achieved through the * operator,
                              or by cut-and-pasting what you want repeated."""

def resetBoard():
    """This returns an empty board, which you are meant to then assign to
    this module's attribute named "B". The reason we return a new board
    (rather than just overwriting the old value of the "B" attribute)
    is because we cannot over-write our attributes.

    The implementation of resetBoard must contain only these 2 things:
    1. A line that creates a temporary variable that is a list containing 
       [' ',' ',' ',' ',' ',' ',' ']. 
       But, the line to create this temporary variable must not be longer
       than 12 characters (not counting the indentation).
    2. A line to return a list of 6 copies of the temporary variable. Note
       that these need to be copies."""
    tl = [' ']*7
    return [tl.copy(),tl.copy(),tl.copy(),tl.copy(),tl.copy(),tl.copy()]

def printBoard():
    """This prints the board. The upper left corner is position B[0][0] and
    the bottom right is position B[5][6]. The format is like this example:

    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

    [' ', ' ', ' ', '●', ' ', ' ', ' ', ' ']

    [' ', '○', ' ', '●', ' ', '○', ' ', ' ']

    ['●', '●', ' ', '●', ' ', '○', ' ', ' ']

    ['●', '○', '○', '●', ' ', '○', '○', '○']
    ========================================

    The implementation of printBoard must contain only these 2 things:
    1. A line to print the rows of "B". This line must be of the form
       'print("..."%(...))', and it cannot use the "[" symbol.
    2. A line to print 35 "=" characters. This line must be less than
       35 characters long, however."""
    print("\n%s\n\n%s\n\n%s\n\n%s\n\n%s\n\n%s"%(B.copy().pop(0), B.copy().pop(1), B.copy().pop(2), B.copy().pop(3), B.copy().pop(4), B.copy().pop(5)))
    print('='*35); print()

def _ok(r,c):
    """This function receives a row number, "r", and a column number, "c".
    The row number is in the range of 0 to 5, with 0 being the highest row
    in the board. The column number is in the range of 1 to 7, with 1 being
    the leftmost column (in other words, the passed-in column number needs
    to be reduced by 1 to get the range of 0 to 6 that we use to store 
    tokens into the columns of the attribute "B"). 

    The return value either the boolean value "False" or it is the value 
    of the passed-in variable "r". The determination of which value to 
    return is that it returns "False" if the corresponding position on the
    board already holds a token.

    The implementation of _ok must contain only a "return" statement that
    uses non-booleans in a logic expression to calculate the return value.

    This function is not meant to be called directly by the user. Instead
    it is meant to be called by the insert method."""
    return B[r][c-1] == ' ' and r
    
def insert(c):
    """This puts a token into the column indicated by the argument, "c". Take
    note that the numbering of "c" begins at 1, even though the numbering 
    of rows within the attribute "B" begins at 0. Note also that we are not
    concerned with the situation where the column is already full (in which 
    case any behavior is allowed, because it is a condition we won't test).

    The implementation of insert must contain only the following 3 things:
    1. A line to identify which row the token will fall into. That is to 
       say: the deepest row of "B" that has a " " in column "c".
       To calculate this row number, you'll call the "_ok" method multiple
       times. But you can't use loops or if-statements in this calculation.
    2. A line to put the correct token ('●' or '○') into the "B" attribute.
       The correct token is determined by checking the isFilled attribute.
       The correct position to place the token with the "B" attribute is
       determined by the passed-in column number, "c", and the row number
       that you just calculated on the previous line. Again, you cannot use
       an if-statement.
    3. A line that toggles the value held in the isFilled list (ie, if it
       was True then it becomes False, and vice versa)."""
    r = _ok(5,c) or _ok(4,c) or _ok(3,c) or _ok(2,c) or _ok(1,c) or _ok(0,c)
    B[r][c-1] = (isFilled[0] and '\u25cf') or '\u25cb'
    isFilled[0] = not isFilled[0]

def makeAmove():
    """This randomly chooses a column to put a token into. It prints a line
    of text indicating which column was chosen. It then calls the insert 
    method, to put a token into the chosen column.

    The implementation of makeAmove must have only the following 3 things:
    1. A line to pick a random number between 1 and 7. We will assume that
       the function it needs was already imported from the "random" module.
    2. A line in the form of "print(...)". This prints the choice you made
       on the previous line, in a format like: "○ chooses the 5th column."
       Note how the column prints as an ordinal number (ie: 1st, 2nd, 3rd,
       4th, 5th, 6th, 7th). You must use non-booleans in a logic expression
       to compute the ordinal suffix (ie: "st", "nd", "rd", or "th").
    3. A line that calls "insert", to put the token into the chosen column."""
    c = randint(1,7)
    print((isFilled[0] and '\u25cf' or '\u25cb') + " chooses the %d"%(c) + (c==1 and "st" or c==2 and "nd" or c==3 and "rd" or c>=4 and "th") + " column.\n")
    insert(c)


# The next line should create the "B" attribute, initialized to an empty board:
B=resetBoard()
#
# The remaining lines are for regression testing. This is the one place I will
# allow the use of an if-statement. The reason I allow it here is because this
# specific case was actually already covered, on slide #95 of Lecture 4. Follow
# that slide's syntax for the if-statement. But the body of your regression
# test will be different than on that slide. On that slide, the body was a call
# to doRegressTest(), but in the code below, the body will be three parts:
# First, a line to import the random number function that we saw makeAmove()
# using, above. Second, 16 calls to makeAmove(). Third, a call to printBoard().
# remember that every line of the body must be indented under the if-statement.
if __name__=='__main__':
    from random import randint
    makeAmove(); makeAmove(); makeAmove(); makeAmove(); makeAmove(); makeAmove(); makeAmove(); makeAmove(); makeAmove(); makeAmove(); makeAmove(); makeAmove(); makeAmove(); makeAmove(); makeAmove(); makeAmove()
    printBoard()
