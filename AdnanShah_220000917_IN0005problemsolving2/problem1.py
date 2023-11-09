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
