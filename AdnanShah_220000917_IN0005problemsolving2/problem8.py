#problem 1
def fibonacci(num):
    a = 0
    b = 1
    num_list = [0,1]
    if num < 0:
        return('Invalid Input')
    elif num == 0:
        return a
        num_list.append(a)
    elif num == 1:
        return b
        num_list.append(b)
    else:
        for i in range (2, num):
            total = a + b
            a = b
            b = total
            num_list.append(b)
    return num_list
   
num = int(input('How many numbers do you want inside the sequence:\n'))
print(fibonacci(num))

print('\n')

#problem 4
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

print('\n')

#problem 5
def xyz_ending(string):
    if "xyz" in string:
        x_index = string.index("xyz")
        if string[x_index-1] == ".":
            string = string[x_index+1:]
            if len(string) < 3:
                return(False)
            else:
                x_index = string.index("xyz")
                if string[x_index+1] == "y" and string[x_index+2] == "z":
                    if (string[x_index+1] == "x") and (string[x_index+2] == "y"):
                        return(True)
                    else:
                        return(True)
                    
        elif string[x_index+1] == "y" and string[x_index+2] == "z":
            if (string[x_index+1] == "x") and (string[x_index+2] == "y"):
                return(True)
            else:
                return(True)
    else:
        return(False)

string=input("Enter a string:\n")
print(xyz_ending(string))

print('\n')

#problem 6
def friend(day_of_week):
    day = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]

    lowercase = day_of_week.lower()
    if lowercase in day:
        return(f"{day_of_week} has the index of", day.index(day_of_week)+1)

def meeting(days):
    day = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]
    num_of_days = ((day.index(day_of_week)) + days) % 7
    meeting_day = day[num_of_days]
    return(f"We'll meet on {meeting_day}")

day_of_week = input("Enter the day of the week:\n")
print(friend(day_of_week))
days = int(input("In how many days are we meeting:\n"))
print(meeting(days))

print('\n')

#problem 7
def end(string1, string2):
    string1 = string1.lower()
    string2 = string2.lower()
    if (len(string1) <= 1 or len(string2) <= 1):
        if (string1[0-1] == string2[-1]):
            return(True)
        elif (string2[0-1] == string1[-1]):
            return(True)
        else:
            return(False)
    else:
        if (string1[0-1] == string2[-1]) and (string1[0-2] == string2[-2]):
            return(True)
        elif (string2[0-1] == string1[-1]) and (string2[0-2] == string1[-2]):
            return(True)
        else:
            return(False)

string1=input("Enter a string:\n")
string2=input("Enter another string:\n")
print(end(string1, string2))
