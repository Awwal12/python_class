import random
secret = random.randint(1, 5)
print('Im thinking of a number from 1-5 can u guess it in 3 tries...')

for i in range(1, 4):
    print('Guess')
    guess = int(input())
    if guess > secret:
        print('the guess is lower')
    elif guess < secret:
        print('the guess is higher')
    else:
        break

if guess == secret:
    print('the guess is correct in ' + str(i) + ' steps')
else:
    print('the guess is' + str(secret))
