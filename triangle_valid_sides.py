a,b,c=input("Enter the three sides of triangle:").split()
a,b,c=int(a),int(b),int(c)
if (a>b) and (a>c):
	if(c+b)>a:
		print("valid triangle")
	else:
		print("invalid Triangle")
elif (b>c) and (b>a):
	if (a+c)>b:
		print("Valid triangle")
	else:
		print("invalid triangle")
elif(c>b) and (c>a):
	if(b+a)>c:
		print("valid triangle")
	else:
		print("invalid triangle")

elif (a==b) or (b==c) or (c==a):
	print("valid triangle")
