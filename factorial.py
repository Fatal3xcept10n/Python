userinput = int(raw_input('''insert number
>>>'''))
ans = userinput
for x in range(userinput-1, 1, -1):
	ans = (x*ans)
quote = ('factorial of %s = %s')
print (quote % (userinput, ans))