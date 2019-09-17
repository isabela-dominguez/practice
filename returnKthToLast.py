from linkedList import *

def return_Kth_to_last(ll, k): 

    i = 0 
    curr = ll.head 
    #print(curr.value)

    while ll: 
        n = k - i
        if(n == 0): 
            return curr
        
        i += 1
        curr.next = curr.next  

    return False 


ll = randomLinkedList(5, 0, 100)
print(ll)
print(return_Kth_to_last(ll, 1))

p = "letter"
print(p[0])
n = p*2 
print(n)