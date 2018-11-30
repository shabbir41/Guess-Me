import random
high=100
c=0
ans=random.randint(1,high)
guess=int(input("enter ur guess here"))
while guess!=ans:
    if guess > ans:
        guess=int(input("guess lower"))
    elif guess==0 or c==4:
        print("sorry!! timezz up..!!")
        break
    else:
        guess=int(input("guess higher"))
    c+=1
else:
    print("u guessed correctly!!!")
