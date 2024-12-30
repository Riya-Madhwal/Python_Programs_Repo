import random                      #importing a random module to generate a random number
n = random.randint(1,100)
p = random.randint(1,200)
q = random.randint(1,300)
dicn={1:n, 2:p, 3:q} #dictionary to store random values
a=-1
guess=0
#variable b for difficulty level chosen by the user
b= int(input('choose the difficulty level:1 for EASY 2 for Moderate, 3 for DIFFICULT: '))
if b==1:
    c=dicn.get(1)  #variable c to store the random value through using the dictionary
elif b==2:
    c=dicn.get(2)
else:
    c=dicn.get(3)

while a!=c:
    a=int(input('guess the number:'))

    if a<c:
        print('higher number please!')
        guess+=1
    elif a>c:
        print('lower number please!')
        guess += 1

    else:
          guess+=1
          print(f'total attempts: {guess}')

if guess==1:
   print('yeah, Great!you guessed it in first attempt')
else:
    print(f'you guessed it in total {guess} attempts')
