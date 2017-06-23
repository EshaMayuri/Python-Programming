# task 1
def print_horiz_line():
  return " --- "

def print_vert_line():
    return "|    "

def task1():
    dimensions = input("specify the number of columns that you want to have: ")
    # rows = input("specify the number of rows that you want to have: ")
    result = ""
    c = int((dimensions.split("*"))[0])
    # r =int(rows)
    for i in range(0,c):
        # for j in range(0,c):
        result = result + print_horiz_line()*c + "\n"
        result = result + print_vert_line()
        for j in range(0,c):
            result = result + print_vert_line()
        result = result + "\n"
    result = result + print_horiz_line()*c
    print(result)

# task 2
def task2():
    n = input("number of digits you want to enter:")
    # for i in range(0,n):
    #     list[i] = input()
    print(n)
    list = [n[0]] + [n[-1]]
    print(list)

task1()
task2()
