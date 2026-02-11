length,breath=input("Enter the length and breath of the rectangle:").split()
length,breath=int(length),int(breath)
area=length*breath
perimeter=2*(length+breath)
print("the area of rectangle is",area)
print("the perimeter of the rectangle is",perimeter)
if area>perimeter:
	print("Area is greater than perimeter")
elif perimeter>area:
	print("Perimter is greater than area")
else:
	print("invalid input")
