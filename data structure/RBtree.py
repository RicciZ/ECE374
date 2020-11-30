class RBTreeNode(object):
    def __init__(self, x):
        self.key = x
        self.left = None
        self.right = None
        self.parent = None
        self.color = 'black'
        self.size=None
        
class RBTree(object):
    def __init__(self):
        self.nil = RBTreeNode(0)
        self.root = self.nil

    def RBSearch(self,key):
        x = self.root
        while x != self.nil:
            if x.key == key:
                return x
            elif x.key > key:
                x = x.left
            else:
                x = x.right
        return None

    def LeftRotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.nil:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == self.nil:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def RightRotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.nil:
            y.right.parent = x
        y.parent = x.parent
        if x.parent == self.nil:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def RBInsert(self, z):
        y = self.nil
        x = self.root
        while x != self.nil:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.parent = y
        if y == T.nil:
            T.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z
        z.left = self.nil
        z.right = self.nil
        z.color = 'red'
        self.RBInsertFixup(z)

    def RBInsertFixup(self, z):
        while z.parent.color == 'red':
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right
                if y.color == 'red':
                    z.parent.color = 'black'
                    y.color = 'black'
                    z.parent.parent.color = 'red'
                    z = z.parent.parent
                else:
                    if z == z.parent.right:
                        z = z.parent
                        self.LeftRotate(z)
                    z.parent.color = 'black'
                    z.parent.parent.color = 'red'
                    self.RightRotate(z.parent.parent)
            else:
                y = z.parent.parent.left
                if y.color == 'red':
                    z.parent.color = 'black'
                    y.color = 'black'
                    z.parent.parent.color = 'red'
                    z = z.parent.parent
                else:
                    if z == z.parent.left:
                        z = z.parent
                        self.RightRotate(z)
                    z.parent.color = 'black'
                    z.parent.parent.color = 'red'
                    self.LeftRotate(z.parent.parent)
        self.root.color = 'black'

    def RBTransplant(self, u, v):
        if u.parent == self.nil:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def TreeMinimum(self, x):
        while x.left != self.nil:
            x = x.left
        return x

    def RBDelete(self, z):
        y = z
        y_original_color = y.color
        if z.left == self.nil:
            x = z.right
            self.RBTransplant(z, z.right)
        elif z.right == self.nil:
            x = z.left
            self.RBTransplant(z, z.left)
        else:
            y = self.TreeMinimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self.RBTransplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self.RBTransplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        if y_original_color == 'black':
            self.RBDeleteFixup(x)

    def RBDeleteFixup(self, x):
        while x != self.root and x.color == 'black':
            if x == x.parent.left:
                w = x.parent.right
                if w.color == 'red':
                    w.color = 'black'
                    x.parent.color = 'red'
                    self.LeftRotate(x.parent)
                    w = x.parent.right
                if w.left.color == 'black' and w.right.color == 'black':
                    w.color = 'red'
                    x = x.parent
                else:
                    if w.right.color == 'black':
                        w.left.color = 'black'
                        w.color = 'red'
                        self.RightRotate(w)
                        w = x.parent.right
                    w.color = x.parent.color
                    x.parent.color = 'black'
                    w.right.color = 'black'
                    self.LeftRotate(x.parent)
                    x = self.root
            else:
                w = x.parent.left
                if w.color == 'red':
                    w.color = 'black'
                    x.parent.color = 'red'
                    self.RightRotate(x.parent)
                    w = x.parent.left
                if w.right.color == 'black' and w.left.color == 'black':
                    w.color = 'red'
                    x = x.parent
                else:
                    if w.left.color == 'black':
                        w.right.color = 'black'
                        w.color = 'red'
                        self.LeftRotate(w)
                        w = x.parent.left
                    w.color = x.parent.color
                    x.parent.color = 'black'
                    w.left.color = 'black'
                    self.RightRotate(x.parent)
                    x = self.root
        x.color = 'black'

def preorder(x):
    if x!= None:
        if x.key!=0:
            print(f"key: {x.key}, x.parent: {x.parent.key}, color: {x.color}")
        preorder(x.left)
        preorder(x.right)
        
nodes = [11,2,14,1,7,15,5,8,4]
T = RBTree()
for node in nodes:
    T.RBInsert(RBTreeNode(node))
print('preorder')
preorder(T.root)
T.RBDelete(T.root)
print('preorder')
preorder(T.root)
T.RBDelete(T.root)
print('preorder')
preorder(T.root)