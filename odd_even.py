while (True):
		
	userinput = raw_input('''choose:
	odd  (a)
	even (b)
			
	exit (z)
	>>>''')
			
	if userinput == 'b':
		
		startnum = 0
		
	elif userinput == 'a':
		
		startnum = 1

	elif userinput == 'z':

		break
			
	userinputb = int(raw_input('''choose number
	>>>'''))
	for x in range(startnum, userinputb+2, +2):
		print (x)
