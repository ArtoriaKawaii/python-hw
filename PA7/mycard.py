#Section 1:
# Functions to import from modules: dataclass, sub, split, randrange & partial
# Functions to define (but without using the "def" keyword:
#   1. A simplified form of randrange that assumes a 0 left-end point
#   2. An function that can invoke object's setattr method (see Lecture 16).
from dataclasses import dataclass
from random import randrange
from functools import partial

#Section 2:
# A dataclass decorator with flags set that will allow order comparisons and
# will make objects of this class immutable.
@dataclass(init=False, repr=True, eq=True, order=True, unsafe_hash=False, frozen=True)

#Section 3:
class Card:  #This line must come immediately after the dataclass decorator.
    """ A playing card. """

#Section 4: Declare two class attributes. One is a string of all possible card
# values ("23456789TJQKA🃏"), and the other is of all possible suits ("♣♦♥♠").
# You will notice that the Joker is a unicode character. On my computer, this
# unicode character is double-wide, but the widths of the suit characters is
# ordinary. This is how we will assume things display in this homework (so if
# it looks different on your computer, just pretend that it looks as it does
    val_str='23456789TJQKA🃏'
    suit_str='♣♦♥♠'

#Section 5: Declare two annotated attributes. The first holds an integer for
# that will indicate this card's value: it is an index to the above class
# attribute of card values. The second holds an integer for this card's suit.
# Note: the order of declaring these two attributes is important for allowing
# the dataclass to reason correctly about the comparison order between cards.
    val_index: int
    suit_index: int

#Section 6: This is the constructor method. It can be called 2 different ways:
#           1. With two positional parameters. Both of these are strings. The
#              first string is value, Any of the following are fine:
#              "Ace","aCe","A","a","2","3","4","5","6","7","8","9","10","T",
#              Queen","Q","q","Quiditch","King", "KING", "k", "Jack", "j",
#              "J is for Jack, not Joker", "Joker","JOKER","joker", "🃏", etc.
#              Notice that: 1) Only the 1st letter of the string matters. (In
#                              the case of "10", it is a 2-character string,
#                              but the first character, "1" is still unique.)
#                           2) Both the Jack and the Joker being with "J".
#                              Therefore, the user must actually say "joker"
#                              to get a joker (or they can pass in a "🃏").
#              The second positional parameter is for the suit. Any of the
#              following are fine: "Heart","Hearts","H","h","Spades","S","s"
#              "cLuB","C","c","diamond","D","d","Don't need extra chars",etc.
#              Note that a joker does not have a suit, but does have a color.
#              Therefore, we still store a suit for the joker cards.
#           2. With no positional parameters. In this case, the card is chosen
#              randomly among all possible cards (either 52 or 54 if jokers).
#              Each card must have an equal probability.
#
# In addition, __init__ also takes two named parameters with default values.
# One is named "joker", and its default value is False. This parameter is used
# if choosing a random card (ie, when no positional parameters are given): it
# decides whether there are 52 or 54 possibilities. This parameter is not used
# for anything else, hence this is be legal "Card('joker','H',joker=False)".
# The other named parameter is "faceup", which has a default value of False.
# This value gets stored in an instance variable "faceup". It will be used
# later, when the card is printed, by __str__, below.
#
# If a class is made with incorrect arguments, raise an error.
#
#
# Four notes are worth discussing:
#  1. The @dataclass line has defined cards as frozen. This is correct, in the
#     sense that they won't change once created. (And by being frozen, they
#     are hash-able and can store in sets -- which is a good feature because
#     the cards in a player's hand is best-modeled as being an unordered set.)
#     But it's not exactly true that they won't change. For one thing, there
#     will be a flip() method defined below. Of more immediate concern, the
#     instance attributes do get set within the constructor. But you cannot
#     write code like "self.faceup=faceup", because cards are frozen. See
#     lecture 16 for details, but the basic idea is that you will use the
#     function you defined in Section #1, above.
#  2. The value will be stored as an integer which indicates the index for
#     the corresponding position of the class attribute string of values (ie,
#     it will be a number between 0 and 12). Similarly, the suit will be a
#     number between 0 and 4, indicating the index in the class attribute of
#     suits. This was already discussed in section 5.
#  3. Recall that the string class has methods named lower() and upper()
#  4. Recall that strings are immutable, so you cannot change just the first
#     character, but you can create a new string with the same name. And you
#     can do this even if it is the name of one of the function's parameters.
    def __init__(self, joker=False, faceup=False):
        pass
    def __init__(self, value, suit, joker=False, faceup=False):
        self.faceup=faceup

#Section 7: This is a method named "flip", which toggles the value of the
# "faceup" attribute. (By the way, this means that the object is technically
# not immutable -- but since it does not change the hash value, it is still
# safe to hash it (ie to use these cards as elements of sets).
    def flip(self):
        self.faceup^=1
#Section 8: This is the __str__ method. It uses color codes that work on my
# computer, and which I hope will work on yours (If they don't just pretend
# that they do, because it will work when I test your code on my computer).
# Because I have not taught you about color codes, I'll give that part to you:
    def __str__(self):
        if not self.faceup:
            S=' \033[32m\033[44m'  #Color is now green on blue
        elif self.suit in [1,2]: 
            S=' \033[31m\033[107m' #Color is now red on white
        else:
            S=' \033[30m\033[107m' #Color is now black on white
            
        #Section 8.1: This part decides how the card should appear. Here are
        # all of the possibilities:"2♣","3♣","4♣","5♣","6♣","7♣","8♣","9♣",
        # "T♣","J♣","Q♣","K♣","A♣","2♦","3♦","4♦","5♦","6♦","7♦","8♦","9♦",
        # "T♦","J♦","Q♦","K♦","A♦","2♥","3♥","4♥","5♥","6♥","7♥","8♥","9♥",
        # "T♥","J♥","Q♥","K♥","A♥","2♠","3♠","4♠","5♠","6♠","7♠","8♠","9♠",
        # "T♠","J♠","Q♠","K♠","A♠","🃏", and "⠿⠿".
        # Among the above, notice the final two ("🃏" and "⠿⠿"). The joker
        # is (at least for me) a double-wide character, and it doesn't display
        # a suit (although it does have a suit for setting the color). As for
        # the "⠿⠿" string, this is what you print if the card is NOT face-up. 

        #Section 8.2:
        S+='\033[37m\033[40m\n' # Restore normal colors

        #Section 8.3: as the image file provided with this template shows, the
        # cards each display on two lines. And that means that we need to do
        # all of that color stuff again - but actually, we don't want to that.
        # Instead, we'll just use the "sub" function from the re module to
        # convert all of the strings listed in Section 8.1 into "  ".

        #Section 8.4:
        return S
    
#Section 9: This is the __add__ method. Its behavior is a little strange. It
# does not make sense to add two cards. Instead we'll define it differently:
# as the adding of their two display strings (ie, the strings returned by
# __str__). Now why would we want to do this? It is because we want to be
# able to display several cards next to each other -- but each card displays
# on two lines. So we need to merge each card's top lines together, then merge
# their bottom lines together.
# There must be three lines of code:
# 1. The object that adds to self may be either another card (in which case
#    you need to run its __str__), or it be a string (ie, its __str__ was run
#    already). This line runs __str__ on the parameter (if hasn't run already)
#
# 2. This line has to use these components:
#    -The split function from the re module must be used to separate based on
#     the "\n" character.
#    -The zip function must then be used to merge the splits of the two cards
#     (ie, to put the top rows together and the bottom rows together).
#    -A list comprehension must then be used to create top and bottom strings.
#     Note, the for-loop of the comprehension will assign to two variables at
#     once (ie, it uses a comma).
#
# 3. The third line returns the combined string, by concatenating the top and
#    bottom strings (along with adding some extra "\n" characters).


if __name__ == "__main__":
    print()
    c1=Card("Queen", "Hearts"); print(c1)
    c1.flip(); print(c1+Card("joker", "hearts",faceup=True),end="\n\n")
    print(Card(joker=True,faceup=True)+Card(joker=True,faceup=True))
    print(c1<Card("A","S"),c1<Card("2","S"),c1>Card("A","S"),c1<Card("2","S"))

#Look at the provided deck.py for another test of this card module...
