import random 
def win(comp, you):
    if comp == you:
        return None
    elif comp == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True
    elif comp == 'w':
        if you == 's':
            return True
        elif you == 'g':
            return False
    elif comp == 'g':
        if you == 'w':
            return True
        elif you == 's':
            return True
print(" computer turn : snake(s), water(w) or gun(g) ")        
randno = random.randint(1,3)
if randno == 1:
    comp = 's'
elif randno == 2:
    comp = 'w'
elif randno == 3:
    comp = 'g'

    
you = input(" your turn : snake(s), water(w) or gun(g) ")

print(f"computer choose {comp}")
print(f"you choose {you}")
gamewin = win(comp, you)
if gamewin == None:
    print("The game is tie")
elif gamewin:
    print("you win")
else:
    print("you lose")

