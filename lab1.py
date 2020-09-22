class Set:
    def __init__(self,contents=[],loadMax=0.75,loadMin=0.25):
        self.items = [None] * 20
        self.numItems = 0
        self.loadMax = loadMax
        self.loadMin = loadMin
        for e in contents:
            self.add(e)
    
    def __contains__(self,item):
        index = hash(item) % len(self.items)
        while self.items[index] != None:
            if self.items[index] == item:
                return True
            index = (index + 1) % len(self.items)
        return False
    
    def __iter__(self):
        for e in self.items:
            if e != None and type(e) != Set.__Placeholder:
                yield e

    ## punlic functions
    def add(self,item):
        if Set.__add(item,self.items):
            self.numItems += 1
            if self.numItems / len(self.items) >= self.loadMax:
                self.items = Set.__rehash(self.items,[None]*(2*len(self.items)))

    def addlist(self,items):
        for e in items:
            self.add(e)

    def remove(self,item):
        if Set.__remove(item,self.items):
            self.numItems -= 1
            if self.numItems / len(self.items) <= self.loadMin:
                self.items = Set.__rehash(self.items,[None]*(len(self.items)//2))
        else:
            raise KeyError("Item not in the set")

    def removelist(self,items):
        for e in items:
            self.remove(e)

    def delete(self,item):
        if Set.__remove(item,self.items):
            self.numItems -= 1
            if self.numItems / len(self.items) <= self.loadMin:
                self.items = Set.__rehash(self.items,[None]*(len(self.items)//2))

    def intersect(self,other):
        res = []
        for i in self:
            if i in other:
                res.append(i)
        return Set(res)

    def union(self,other):
        res = []
        for i in self:
            res.append(i)
        for i in other:
            if i not in self:
                res.append(i)
        return Set(res)

    def differ(self,other):
        res = []
        for i in self:
            if i not in other:
                res.append(i)
        return Set(res)

    def subsetof(self,other):
        for i in self:
            if i not in other:
                return False
        return True

    def length(self):
        return self.numItems

    def noCommonWith(self,other):
        for i in self:
            if i in other:
                return False
        return True

    def removeIntersection(self,other):
        for i in self:
            if i in other:
                self.remove(i)
    
    def print(self):
        for e in self:
            print(e,end=' ')
        print()

    ## Hidden Helper Class
    class __Placeholder:
        def __init__(self):
            pass
        def __eq__(self,other):
            return False

    ## private functions
    def __add(item,items):
        index = hash(item) % len(items)
        location = -1
        while items[index] != None:
            if items[index] == item:
                return False
            if location < 0 and type(items[index]) == Set.__Placeholder:
                location = index
            index = (index + 1) % len(items)
        if location < 0:
            location = index
        items[location] = item
        return True

    def __remove(item,items):
        index = hash(item) % len(items)
        while items[index] != None:
            nextIndex = (index + 1) % len(items)
            if items[index] == item:
                if items[nextIndex] == None: # check the next one
                    items[index] = None
                else:
                    items[index] = Set.__Placeholder()
                return True
            index = nextIndex
        return False

    def __rehash(olditems,newitems):
        for e in olditems:
            if e != None and type(e) != Set.__Placeholder:
                Set.__add(e,newitems)
        return newitems


# a) create a set
s = Set([i*2 for i in range(10)])

# b) iterate over sets
for i in s:
    print(i,end=' ')
print()

# c) add member(s)
print("c)")
s.add(23)
print("add 23")
s.print()
s.addlist([34,45,56,67])
print("add a list")
s.print()

# d) remove item(s)
print("d)")
s.remove(45)
# s.remove(77)
print("remove 45")
s.print()
s.removelist([23,67])
print("remove a list")
s.print()

# e) remove an item from a set if it is present in the set
print("e)")
s.delete(10)
print("delete 10")
s.print()
s.delete(77)
print("delete non-exist element 77")
s.print()

# f) intersection
print("f)")
s1 = Set([i for i in range(1,10)])
s2 = Set([i for i in range(6,17)])
print("two sets")
s1.print()
s2.print()
print("intersection")
s3 = s1.intersect(s2)
s3.print()

# g) union
print("g)")
print("two sets")
s1.print()
s2.print()
print("union")
s3 = s1.union(s2)
s3.print()

# h) difference
print("h)")
print("two sets")
s1.print()
s2.print()
print("difference")
s3 = s1.differ(s2)
s3.print()

# i) subset of
print("i)")
print("s1,s2,s1-s2")
s1.print()
s2.print()
s3 = s1.differ(s2)
s3.print()
print("(s1-s2) is subset of s1? s2?")
print(s3.subsetof(s1),s3.subsetof(s2))

# j) length
print("j)")
print("set")
s1.print()
print(f"length is {s1.length()}")

# k) no elements in common
print("k)")
s1.print()
s2.print()
print(s1.noCommonWith(s2))

# l) remove intersection
print("l)")
s1.print()
s2.print()
s1.removeIntersection(s2)
print("remove intersection")
s1.print()