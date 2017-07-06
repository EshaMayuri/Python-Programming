# Input list on which the operations would be performed
list = [{'course': 'python', 'LastGPA': 90, 'CurrentGPA': 80},
        {'course': 'python', 'LastGPA': 95, 'CurrentGPA': 80},
        {'course': 'python', 'LastGPA': 100, 'CurrentGPA': 100}]
# Initialising the list that would store the average
newList = []
i = 0

# Variable to store average at each level
avg = 0

# Iterating through the loop and calculating the averages
while i < len(list):
    for key in list[i]:
        if(key == "LastGPA"):
            denotion = "LastGPA"
            avg = list[i][key]
        elif(key == "CurrentGPA"):
            avg = avg + list[i][key]
            newList.append(avg/2)
    i +=1
print("Original list of dictionaries:\n", list)

# To pop out the numerical items of the dictionaries
[d.pop('LastGPA') for d in list]
[d.pop('CurrentGPA') for d in list]

# updating the dictionaries with the averages
for d,num in zip(list, newList):
    d['LastGPA+CurrentGPA'] = num

# printing the updated list of dictionaries

print("Updated list of dictionaries:\n",list)

# (OR)

list_2 = [{'course': 'python', 'LastGPA': 90, 'CurrentGPA': 80},
        {'course': 'python', 'LastGPA': 95, 'CurrentGPA': 80},
        {'course': 'python', 'LastGPA': 100, 'CurrentGPA': 100}]

def Task2(dictList):
    i = 0
    for i in dictList:
        lastGpa = i.pop('LastGPA')
        currentGpa = i.pop('CurrentGPA')
        i['LastGPA + CurrentGPA'] = ((lastGpa + currentGpa)/2)
    return dictList
print("Original list of dictionaries:\n", list_2)
print("Updated list of dictionaries:\n",Task2(list_2))