import random 
comp = str()
def winner(comp,you) :
    if comp == you:
        return None
    if comp ==  'r':
        if you ==  'p':
            return True
        if you ==  's':
            return False
    elif comp ==  'p':
        if you ==  's':
            return True
        if you == 'r':
            return False
    elif comp ==  's':
        if you == 'r':
            return True
        if you ==  'p':
            return False

print("Computer Turn:Rock(r),Paper(p),Sissors(s)? ")
randomno = random.randint(1, 3)
if randomno == 1 :
    comp =  'r'
elif randomno == 2 :
    comp =  'p'
elif randomno == 3 :
    comp =  's'

you = input("Your Turn : Rock(r),Paper(p),Sissors(s)?")
win = winner(comp, you)

print (f"Computer choose {comp}")
print (f"You Choose {you}")
 
if win == None :
    print ("Tie")
elif win :
    print ("You win")
else :
    print ("You lost")