angle1,angle2,angle3=input("Enter the value of Angle1,Angle2,Angle3:").split()
angle1,angle2,angle3=int(angle1),int(angle2),int(angle3)
if ((angle1+angle2+angle3)>180) or ((angle1+angle2+angle3)<180):
	print("This is a invalid triangle")
elif((angle1+angle2+angle3)==180):
	print("This is a valid triangle ")
else:
	print("invalid input")
