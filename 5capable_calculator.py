import time

while (True):

	fts = raw_input('''

choose:
	addition        (a)
	subtraction     (b)
	division        (c)
	multiplication  (d)
	squaring        (e)
	
	exit            (z)
	
	>>>''')
	
	
	if fts == 'a':
	
		addvara = float(raw_input('enter first number >>>'))
		addvarb = float(raw_input('enter second number >>>'))
		addtot = (addvara+addvarb)
		addqou = ('%s+%s is = %s')
		print (addqou % (addvara, addvarb, addtot))
		time.sleep(3)
	
	elif fts == 'b':
	
		dedvara = float(raw_input('enter number to be subtracted >>>'))
		dedvarb = float(raw_input('enter number to subtract with >>>'))
		dedtot = (dedvara-dedvarb)
		dedqou = ('%s-%s is = %s')
		print (dedqou % (dedvara, dedvarb, dedtot))
		time.sleep(3)	

	elif fts == 'c':
	
		devvara = float(raw_input('enter number to be divided >>>'))
		devvarb = float(raw_input('enter number to divide with >>>'))
		devtot = (devvara/devvarb)
		devqou = ('%s/%s is = %s')
		print (devqou % (devvara, devvarb, devtot)) 
		time.sleep(3)
	
	elif fts == 'd':

		mulvara = float(raw_input('enter first number >>>'))
		mulvarb = float(raw_input('enter second number >>>'))
		multot = (mulvara*mulvarb)
		mulqou = ('%sx%s is = %s')
		print (mulqou % (mulvara, mulvarb, multot))
		time.sleep(3)

	elif fts == 'e':
	
		squvara = float(raw_input('enter number to be squared >>>'))
		squtot = (squvara*squvara)
		squqou = ('%s squared is = %s')
		print (squqou % (squvara, squtot))
		time.sleep(3)

	elif fts == 'z':

		print ('Thank you for using Python Calculator! Bye!')
		time.sleep(3)		
		break
	  
	    
