#guess number game

import random

attempts = 0

#ask for user's name
print('Hello, what is your name?')
user_name = input()

#generate number
number = random.randint(1,20)
print('Listen, ' + user_name + ', I have a number in mind, between 1 and 20.')

#make the user guess the number
for attempts in range(6):
    print('Try to guess the number.')
    attempt_value = input()
    attempt_value =  int(attempt_value)

    if attempt_value < number:
        print('Your guess is too low.')
    elif attempt_value > number:
        print('Your guess is too high.')
    elif attempt_value == number:
        break
    
#evaluate result    
if attempt_value == number:
    attempts = str(attempts + 1)
    print('Congratulations, ' + user_name + ', you have won! You have correctly guessed the number in ' + attempts + ' attempts.')
else:
    number = str(number)
    print('I\'m sorry, you\'ve ran out of attempts. The number I had in mind was ' + number + '.')
