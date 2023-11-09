string1=input("Enter a string:\n")
string2=input("Enter another string:\n")
string1 = string1.lower()
string2 = string2.lower()
if (len(string1) <= 1 or len(string2) <= 1):
    if (string1[0-1] == string2[-1]):
        print(True)
    elif (string2[0-1] == string1[-1]):
        print(True)
    else:
        print(False)
else:
    if (string1[0-1] == string2[-1]) and (string1[0-2] == string2[-2]):
        print(True)
    elif (string2[0-1] == string1[-1]) and (string2[0-2] == string1[-2]):
        print(True)
    else:
        print(False)

