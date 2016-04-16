def gcd(a,b):
	while(b!=0):
		a,b=b,a%b
	return a

tc=int(raw_input())
for i in range(0, tc):
	a=int(raw_input())
	arr=[]
	for i in range(0,a):
		b=int(raw_input())
		arr.append(b)
	g=reduce(gcd, arr)
	if g==0:
		g=1
	else:
		for i in arr:
			print i/g,
		print ""

