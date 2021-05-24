import random
print("enter amount you want to invest")
account=int(input())
for i in range(1,10):
  bet=random.randint(1,10)
print("bet",bet)
lucky_draw=random.randint(1,10)
print("lucky_draw",lucky_draw)
if(bet==lucky_draw):
    account=account+900
    print("your balance:",account)
else:
    print("you lost")
    account=account-100
    print("your balance",account)
    
    
    