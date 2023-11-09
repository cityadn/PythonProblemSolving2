active = True
i = 0

num_list = []

def end_game(num, i):
    return("Number of inputs = ", i, 'Sum of your inputs = ', sum(num_list))

def out_of_range(num):
    return("Try again\n")

def not_odd(num):
    num_list.append(num)
    return("Even", num_list)
    

def not_even(num):
    num_list.append(num)
    return("Odd", num_list)
    
while active:
    num = int(input("Enter an integer between 1 and 10, or type -1 to quit:\n"))
    if num == -1:
        print(end_game(num, i))
        break
    elif num > 10 or num < 1:
        print(out_of_range(num))
    elif num % 2 == 0:
        i = i + 1
        print(not_odd(num))
    elif num % 2 != 0:
        i = i + 1
        print(not_even(num))
