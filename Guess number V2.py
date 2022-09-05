# Written by Rob James

# Importing random number library
import random

# Importing time/sleep library
import time

# Storing randomly generated number
number = str(random.randint(1,10))

print ('This is a game of chance!')

# Pause for 1 second
time.sleep (2)

print ('I will pick a number between 1 and 10 and you try to guess it')

time.sleep (3)

responce = input('Are you ready?')

if responce == 'yes':
    # Pause for 1 second
    time.sleep (1)
    print ('Lets go!')
    
elif responce == 'Yes':
    # Pause for 1 second
    time.sleep (1)
    print ('Lets go!')

else:
    print ('Play properly')
    exit()

# Pause for 1 second
time.sleep (1)
    
guess = input('What number am I thinking of? ')

if guess == number:
    # Pause for 1 second
    time.sleep (1)
    print (number + ' is the correct answer!')
    exit()

if guess != number:
    # Pause for 1 second
    time.sleep (1)
    print ('Wrong!')

secondg = input('I will give you one more guess ')
    
if secondg == number:
    # Pause for 1 second
    time.sleep (1)
    print (number + ' is the correct answer!')

if secondg != number:
    print ('Wrong! I was thinking of ' + number + '!')
    # Pause for 1 second
    time.sleep (1)
    print ('Better luck next time')

# Clean exit from code 
exit()
