#take an input from user to be reversed
number = input("please enter a number to reverse: ")
#conversting into integer
input_val = int(number)
data = input_val
output_val = 0
while(input_val>0):
    output_val = output_val*10 + input_val%10
    input_val = input_val//10

print("Reversed value of the provided input data" , data, 'is :' ,output_val)

