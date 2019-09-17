def set_to_false(x): 
    return False

def find_distinct(arr1, arr2): 
    reps = []
    distinct = arr1


    for n in arr2: 
        if n in arr1:
            reps.append(n)
            distinct.remove(n)
            
          
            
    
    return reps
            
        
        


  


arr1 = [1,2,3,4]
h = find_distinct([1,2,3,4], [2,4,6,8])
print(h)