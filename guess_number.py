import random

top_range_num = input('Give a number: ')
# check if user gives a number 
# and greater than 0
if top_range_num.isdigit():
    top_range_num = int(top_range_num)

    if top_range_num <= 0:
        print('Please give a number greater than 0')
        quit()
else:
    print('Please give a number')
    quit()
random_number = random.randint(0, top_range_num)
guesses = 0
while True:
    guesses += 1
    user_guess = input('make a guess: ')
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Please give a number')
        continue
   
    if user_guess == random_number:
        print("You got it!")
        break
    else: 
        if user_guess > random_number:
            print('You were above the number')
        else:
            print('You were below the number')

print("You got it", guesses, "guesses")