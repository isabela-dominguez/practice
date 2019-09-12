def urlify(s, l):
    new_length = l

    for letter in s:
        if(letter == " "):
            new_lenght += 1

    for i in reversed(range(s)):
        if(letter == " "): 
            #start backwards becuase extra space is given
            new_length += 1
            n += "%20"
        else: 
            n += letter 

    return n 

    


print(urlify("this is my banana    ", 4))