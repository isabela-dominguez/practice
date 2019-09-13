class LinkedListNode(): 

   def __init__(self, value, nextNode=None):        
       self.value = value        
       self.nextNode = nextNode


    def insertNode(head, valuetoInsert):
        currentNode = head
        while currentNode is not None:
            if currentNode.nextNode is None:
                currentNode.nextNode = linkedListNode(valuetoInsert)
                return head
            currentNode = currentNode.nextNode 


    def deleteNode(head, valueToDelete):
        currentNode = head
        previousNode = None
        while currentNode is not None:
            if currentNode.value == valueToDelete:
                if previousNode is None:
                    newHead = currentNode.nextNode
                    currentNode.nextNode = None
                    return newHead
                previousNode.nextNode = currentNode.nextNode
                return head
            previousNode = currentNode
            currentNode = currentNode.nextNode
        return head  # Value to delete was not found.