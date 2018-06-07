# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 23:55:48 2018

Linked list implimentation

@author: inkdhakshn
"""

class Node():
    
    def __init__(self, data, nextNode=None):
        self.data = data
        self.next = nextNode

class linkList():
    
    def __init__(self, head=None):
        self.head = head
        self.size = 0
        
    def getSize(self):
        return self.size
    
# Adding Items to the list    
    
    def addNode(self, prev, data):
        if self.size == 0:
            newNode = Node(data)
            self.head = newNode
            self.size += 1
            return self.head
        else:
            nextNode = Node(data)
            prev.next = nextNode
            self.size += 1
            return prev.next
        
    def addAtBeginning(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode
        self.size += 1
        return True
        
    def addInBetween(self, afterNode, data):
        midNode = self.head
        if midNode.next != None:
            while midNode.next != None:
                #prev = midNode
                if midNode.data == afterNode:
                    newNode = Node(data)
                    newNode.next = midNode.next
                    midNode.next = newNode
                    self.size += 1
                    return
                midNode = midNode.next
            print("Node Not found")
            return
        else:
            print("Empty List")
            return 
    
    def addAtTheEnd(self, data):
        lastNode = self.head
        if lastNode.next != None:
            while lastNode.next:
                lastNode = lastNode.next
            lastNode.next = Node(data)
            self.size += 1
        else:
            self.head.next = Node(data)
            self.size += 1
        return True

# Deleting from the list
        
    def deleteFromBeginning(self):
        self.head = self.head.next
        return
              
    def deleteFromLast(self):
        getToLast = self.head
        while getToLast.next != None:
            prev = getToLast
            getToLast = getToLast.next
        prev.next = None
        return
    
    def deleteFromInbetween(self, data):
        midNode = self.head
        prev = midNode
        if midNode.next != None:
            while midNode.next != None:
                if midNode.data == data:
                    prev.next = midNode.next
                    self.size -= 1
                    return
                prev = midNode
                midNode = midNode.next
            print("Node Not found")
            return
        else:
            print("Empty List")
            return         
        
    def printList(self):
        currNode = self.head
        while currNode is not None:
            print(currNode.data)
            currNode = currNode.next            

def main():
    lList = linkList()
    n = lList.addNode(None, 10)
    n = lList.addNode(n, 20)
    n = lList.addNode(n, 30)
    print('after adding three values')
    
    lList.printList()
    print('current Size : {}'.format(lList.getSize()))
    
    n = lList.addAtBeginning(5)
    print('after adding 5 at beginning')    
    
    lList.printList()
    n = lList.addAtTheEnd(50)
    print('after adding 50 at end')        
    
    lList.printList()
    n = lList.addInBetween(30, 40)
    print('after adding 40 between 30 and 50')            
    
    lList.printList()
    print('Current Size after modification is {}'.format(lList.getSize()))
    
    lList.deleteFromBeginning()
    print('After Deleting from beginning')
    lList.printList()
    
    lList.deleteFromLast()
    print('After Deleting from last')
    lList.printList()
    
    lList.deleteFromInbetween(20)
    print('after Deleting 20')
    lList.printList()
    
if '__main__' == __name__:
    main()
    