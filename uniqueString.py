


def isUniqueString(s):
   #ascii or unicode string? 
    if(len(s) > 128):
       return False 

    check =  [False for i in range(128)]
    for letter in s: 
        unique_value = ord(letter)
        if(check[unique_value]):
            return False
        else:
            check[unique_value] = True

    return True

s = isUniqueString("yikes")
print(s)