import random

class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class SelfOrganizingList:
    def __init__(self,elements=[]):
        self.first = None
        self.last = None
        for i in elements:
            self.insert(i)

    def insert(self,x):
        temp = Node(x)
        if self.first == None:
            self.first = self.last = temp
        else:
            self.last.next = temp
            self.last = temp
    
    def delete(self,x):
        prev = None
        curr = self.first
        while curr != None:
            if curr.val == x:
                if prev != None:
                    prev.next = curr.next
                else:
                    self.first = None
                return True
            prev = curr
            curr = curr.next
        return False
    
    def search(self,x):
        prev = None
        curr = self.first
        while curr != None:
            if curr.val == x:
                if prev != None:
                    prev.next = curr.next
                    curr.next = self.first
                    self.first = curr
                return True
            prev = curr
            curr = curr.next
        return False
    
    def printSOL(self):
        if self.first == None:
            print("Empty List")
            return
        temp = self.first
        while temp != None:
            print(temp.val,end='')
            if temp.next != None:
                print(" -> ",end='')
            temp = temp.next
        print()

l = random.sample(range(-10,10),10)
SOL = SelfOrganizingList(l)
print("before search")
SOL.printSOL()
a = random.choice(l)
print(f"search {a}: {SOL.search(a)}")
SOL.printSOL()
a = random.choice(l)
print(f"search {a}: {SOL.search(a)}")
SOL.printSOL()
a = random.choice(l)
print(f"search {a}: {SOL.search(a)}")
SOL.printSOL()
print(f"search {a}: {SOL.search(a)}")
SOL.printSOL()
print(f"search {a}: {SOL.search(a)}")
SOL.printSOL()
print(f"search 20: {SOL.search(20)}")
SOL.printSOL()
for i in range(10):
    SOL.search(i)
print("sequential search from 0 to 9")
SOL.printSOL()
