ram, shyam, ajay=(input("Enter the age of ram shyam and ajay:")).split()
ram, shyam, ajay = int(ram),int(shyam),int(ajay)
if ((ram<shyam) and (ram<ajay)):
	print("ram is younger")
elif ((shyam<ram) and (shyam<ajay)):
	print("shyam is younger")
elif ((ajay<shyam) and (ajay<ram)):
	print("ajay is younger")
else:
	print("invalid input")
