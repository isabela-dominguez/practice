# write code to remove duplicates from an unsorted linked list 
from linkedList import LinkedList

def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        current = head
        while(current != None): 
            runner = current 
            while (runner.next != None): 
                if(runner.next.val == current.val): 
                    runner.next = runner.next.next 
                else: 
                    runner = runner.next 
                    
            current = current.next 
            
        return head


        


