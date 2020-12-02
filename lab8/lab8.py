import random

class Node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.next = []

class SkipList:
    def __init__(self,elements,MaxLevel=5):
        self.MaxLevel = MaxLevel
        self.header = Node(-float('inf'),None)
        self.header.next = [None]*self.MaxLevel
        self.level = 1
        for x in elements:
            self.insert(x[0],x[1])
            
    def search(self,key):
        x = self.header
        for i in range(self.level-1,-1,-1):
            while x.next[i] and x.next[i].key < key:
                x = x.next[i]
        x = x.next[0]
        if x and x.key == key:
            return x.value
        else:
            return None

    def insert(self,key,value):
        lvl = self.randomlevel()
        newnode = Node(key,value)
        newnode.next = [None]*lvl
        update = [self.header]*lvl
        x = self.header
        for i in range(lvl-1,-1,-1):
            while x.next[i] and x.next[i].key < key:
                x = x.next[i]
            update[i] = x
        x = x.next[0]
        if x and x.key == key:
            x.value = value
            return
        if self.level < lvl:
            self.level = lvl
        for i in range(lvl):
            newnode.next[i] = update[i].next[i]
            update[i].next[i] = newnode

    def delete(self,key):
        update = [None]*self.level
        x = self.header
        for i in range(self.level-1,-1,-1):
            while x.next[i] and x.next[i].key < key:
                x = x.next[i]
            update[i] = x
        x = x.next[0]
        if x and x.key == key:
            for i in range(self.level):
                if update[i].next[i] and update[i].next[i].key == key:
                    update[i].next[i] = x.next[i]
            while self.level > 1 and self.header.next[self.level-1]==None:
                self.level -= 1

    def randomlevel(self):
        lvl = 1
        while random.random() < 0.5 and lvl < self.MaxLevel:
            lvl += 1
        return lvl

    def printSL(self):
        for i in range(self.level-1,-1,-1):
            x = self.header
            print("header->",end="")
            while x.next[i]:
                print((x.next[i].key,x.next[i].value),end="->")
                x = x.next[i]
            print("tail\n")
    
    def printKey(self):
        x = self.header
        while x.next[0]:
            x = x.next[0]
            print(f"Key: {x.key}, Number of Levels: {len(x.next)}")
        print()

# build the Skip List and test insert
inputlist = [[random.randint(1,10) for j in range(1,3)] for i in range(1,11)]
print(f"the input list is {inputlist}\n")
SL = SkipList(inputlist)
SL.printSL()
SL.printKey()

# Test search
x = random.choice(inputlist)[0]
print(f"test search: the value of {x} is {SL.search(x)}")
print()

# Test delete
SL.delete(random.choice(inputlist)[0])
SL.delete(random.choice(inputlist)[0])
SL.printSL()
SL.printKey()