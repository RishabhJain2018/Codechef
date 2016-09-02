input_string = raw_input("Enter the string of characters.")
input_string = list(input_string)
copy_string = input_string
a=0
for i in xrange(0, len(input_string)):
	if input_string[i]=="F":
		input_string.pop(i)
		for j in xrange(i-1, 0, -1):
			if input_string[j]=="E":
				input_string.pop(j)
				for k in xrange(j-1, 0, -1):
					if input_string[k]=="H":
						input_string.pop(k)
						for l in xrange(k-1,0,-1):
							if input_string[l]=="C":
								input_string.pop(l)
								a+=1

print a




