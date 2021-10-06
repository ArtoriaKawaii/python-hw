from random import shuffle as randshuffle
from card import *

class Deck(Card):
    """ A stack of cards """
    def __init__(self, faceup=True, shuffle=True, joker=False, \
                       pinochle=False, numDecks=1):
        """faceup decides if the cards show when printed.
            shuffle decides if the cards are ordered
            joker decides if the deck has jokers
            pinochle decides if cards 2-8 will be used
            numDecks decides if multiple decks are being used"""
        X=[Card(y,x,faceup=faceup) for x in "DCHS" for y in "2345678"*(not pinochle)+"9TJQKA"]
        if joker: X+=[Card("Joker","H",faceup=faceup), Card("Joker","S",faceup=faceup)]
        self._deck=X*numDecks
        if shuffle: randshuffle(self._deck)
        self._pos=0;

    @property
    def deal(self):x=self._deck[0]; del self._deck[0]; return x

    def __str__(self):
        ros=(len(self._deck)+23)//24
        s=""
        for i in range(ros):
            t=self._deck[i*24+ (y:=23 if i<ros-1 else(len(self._deck)-1)%24)]
            for j in range(i*24+y-1,i*24-1,-1):
                t=self._deck[j]+t
            s+=t+"\n"
        return s

if __name__ == "__main__":
    print("print(Deck(joker=True,shuffle=False,faceup=False)):")
    print(Deck(joker=True,shuffle=False,faceup=False))
    print("print(Deck(pinochle=True)):")
    print(Deck(pinochle=True))
    print("print(Deck(pinochle=True,faceup=False)):")
    print(Deck(pinochle=True,faceup=False),end="")
