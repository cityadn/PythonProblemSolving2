string=input("Enter a string:\n")
if "xyz" in string:
    x_index = string.index("xyz")
    if string[x_index-1] == ".":
        string = string[x_index+1:]
        if len(string) < 3:
            print(False)
        else:
            x_index = string.index("xyz")
            if string[x_index+1] == "y" and string[x_index+2] == "z":
                if (string[x_index+1] == "x") and (string[x_index+2] == "y"):
                    print(True)
                else:
                    print(True)
                
    elif string[x_index+1] == "y" and string[x_index+2] == "z":
        if (string[x_index+1] == "x") and (string[x_index+2] == "y"):
            print(True)
        else:
            print(True)
else:
    print(False)
