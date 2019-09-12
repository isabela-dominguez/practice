def urlify(s, l):
    n =""
    for letter in s:
        if(letter == " "):
            n += "%20"
        else: 
            n += letter 

    return n 


print(urlify("hi mi ", 4))