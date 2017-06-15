#taking inputs from user for length and breadth of the rectangle
length = input("Please enter a value for length of the rectangle:")
breadth = input("Please enter a value for breadth of the rectangle:")

#typecasting the length and breadth input into integer
l = int(length)
b = int(breadth)

#Calculating the area of the rectangle
area = l * b
perimeter = 2 * (l + b)

#displaying the area and perimeter of a rectangle
print("Area of a rectangle is", area)
print("Perimeter of a rectangle is", perimeter)
