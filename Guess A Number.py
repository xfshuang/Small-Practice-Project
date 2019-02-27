import random
secret_number = random.randint(0,100)
guess= -1
attempt = 0 
while (secret_number != guess):
    guess = int(input('Give me a number from 0 - 100'))
    attempt +=1
    if (attempt == 10):
        print('You have used all your guesses')
        break
    if (guess < secret_number):
           print('Your guess is low!')
    elif (guess> secret_number):
           print('Your guess is high!')
    else:
           print('You guessed right!')
           

