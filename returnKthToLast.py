from linkedList import *

def return_Kth_to_last(ll, k): 

    i = 0 
    curr = ll.head

    while ll: 
        n = k - i
        if(n == 0): 
            return curr
        
        i += 1
        curr = curr.next  

    return False 


ll = randomLinkedList(8, 0, 100)
print(ll)
print(return_Kth_to_last(ll,12))
