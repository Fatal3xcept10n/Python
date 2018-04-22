import random
import time

randvar = random.randint(1, 100)
print (randvar)

while (True):

    userdata = float(raw_input('''
    input number from 1 to 100 and try to guess the random generated number
    >>>'''))

    if userdata == randvar:
            
        guessquote = ('Great job the number was %s, you guessed it!')
        print (guessquote % (randvar))
        time.sleep(3)
        break

            
    elif userdata>randvar:
            
        print ('too big')
        time.sleep(0.5)

    elif userdata<randvar:

	print ('too small')
	time.sleep(0.5)