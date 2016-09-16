input_string = raw_input()
c = 0
ch = 0
che = 0
chef = 0
for i in xrange(len(input_string)):
	if(input_string[i]=="C"):
		c+=1
	elif(input_string[i]=="H"):
		if(c>0):
			c=c-1
			ch+=1
	elif(input_string[i]=="E"):
		if(ch>0):
			ch=ch-1
			che+=1
	elif(input_string[i]=="F"):
		if(che>0):
			che=che-1
			chef+=1
print chef
