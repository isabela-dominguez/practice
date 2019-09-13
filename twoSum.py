
def twoSum(arrInts, target): 
    if (len(arrInts) == 0): 
        return False  

    hset = set()

    for i, num in enumerate(arrInts): 
        val = target - arrInts[i]
        if(arrInts[i] in hset): 
            return True 
        else:
            hset.add(val) 

    return False

    

arr = [1, 2, 3, 3, 4, 2, 3, 43, 10, 18, 12, 102]
print(twoSum( arr , 8))