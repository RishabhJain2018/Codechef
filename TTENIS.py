a=int(raw_input())
for i in xrange(a):
	b=raw_input()
	b=list(b)
	if b[-1] == "1":
		print "WIN"
	else:
		print "LOSE"