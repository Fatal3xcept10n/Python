import random
import time

randvar = random.randint(1, 10)

while (True):

    userdata = int(raw_input('''
    input number from 1 to 10 and try to guess the random generated number
    >>>'''))

    if userdata == randvar:
            
        guessquote = ('Great job the number was %s, you guessed it!')
        print (guessquote % (randvar))
        time.sleep(3)
        break

            
    else:
            
        print ('sorry, try again')
        time.sleep(1)
