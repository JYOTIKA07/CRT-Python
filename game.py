import dice
print("👣"*15,"HILL CLIMB AND FALL","👣"*15)
player_1=input("enter player_1 name:")
player_2=input("enter player_2 name:")
list_a=[]
list_b=[]
i=0
while(sum(list_a)!=10 and sum(list_b)!=10):
    if(i%2==0 and input(" player_1 enter p to play:")=='p'):
        if(sum(list_a)<10):
            diceno=dice.diceroll()
            print("\n dice no.->",diceno)
            list_a.append(diceno)
        else:
            list_a.clear()
        print("Step no->",sum(list_a))
        i+=1
    elif(i%2!=0 and input("player_2 enter p to play:")=='p'):
         if(sum(list_b)<10):
            diceno=dice.diceroll()
            print("\n dice no.->",diceno)
            list_b.append(diceno)
         else:
            list_b.clear()
         print("Step no->",sum(list_b))
         i+=1
    else:
        print("Thank you...")
        break
if(sum(list_a)==10):
    print(player_1,"is the winner🏅🏅🏆")
elif(sum(list_b)==10):
    print(player_2,"is the winner🏅🏅🏆")
else:
    print("Thank youu...")