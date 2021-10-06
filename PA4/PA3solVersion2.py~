from random import randrange as rnd
isFilled = True
B=(["  "]*6,["  "]*6,["  "]*6,["  "]*6,["  "]*6,["  "]*6,["  "]*6)
piece={'Filled':'⚫','filled':'⚫','F':'⚫','f':'⚫','⚫':'⚫','Empty':'⚪','empty':'⚪','E':'⚪','e':'⚪','Hollow':'⚪','hollow':'⚪','H':'⚪','h':'⚪','⚪':'⚪','Full':'⚫','full':'⚫'}

def drop(*moves, player='Auto', toggle=True, **kws):
    global isFilled
    moves=list(moves)
    n=kws["numMoves"] if "numMoves" in kws else len(moves) if len(moves) else 1

    for l in range(n):
        token = '⚪⚫'[isFilled] if player=='Auto' else piece[player]
        if len(moves) == 0:
            numOptions=0
            for i in range(7):
                if '  ' in B[i]: numOptions+=1
            if numOptions>0:
                t=rnd(numOptions)
                for i in range(7):
                    if '  ' not in B[i]: t+=1; continue
                    if t==i: break
                else:
                    print("Error")
                moves=[i+1]
            else:
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
    r=tuple(zip(*B))
    print("┌──┬──┬──┬──┬──┬──┬──┐")
    for i in range(6):
        print("",*r[i],"",sep="|")
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
