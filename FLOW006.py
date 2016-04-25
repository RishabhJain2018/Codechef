t= input()
for i in xrange(t):
	count = 0
	a=int(raw_input())
	while(a>0):
		r=a%10
		count+=r
		a=a/10

	print count