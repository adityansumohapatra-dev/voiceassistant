import random
a=random.choice(range(1,101))
chance=5
while chance>0:
     b=int(input(f"Enter a number between 1 and 100, you have {chance} no. of chances:"))
     if(a==b):
        print("You're correct")
        break
     elif(a>b):
        chance-=1
        print(f"nuh-uh, guess a higher number, and you have {chance} number of chances")
     else:
        chance-=1
        print(f"nuh-uh, guess a lower number, and you have {chance} number of chances")
print("Sorry you have no more chances, better luck next time")
