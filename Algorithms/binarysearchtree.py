class TreeNode:
    def __init__ (self,value): #initializes nodes and values.
        self.left = None
        self.right = None
        self.value = value
        self.content = None

    def insert(self, value, content = None): #inserts a value
        if value < self.value:#If value is less the current node
            if self.left is None:#if left node is None
                self.left = TreeNode(value) #left node is a new TreeNode with the value.
                self.left.content = content
            else:
                self.left.insert(value,content)#if there is a value step to next node.
        else:
            if self.right is None:#if value is greater than current node
                self.right = TreeNode(value)#Right node is a new TreeNode with the value given
                self.right.content = content
            else:
                self.right.insert(value,content)#apply above steps to next node if node is full

    def inorder_traversal(self):#traverses in order, left half of the tree first
        if self.left:#If left node exists
            self.left.inorder_traversal()#calls function on left node, pushing further down the left column.
        print(self.value)#prints last left node.
        if self.right:#if right exists
            self.right.inorder_traversal()#traverse further right.

    def preorder_traversal(self):#traverses in order and prints first
        print(self.value)
        if self.left:#If left node exists
            self.left.preorder_traversal()#calls function on left node, pushing further down the left column.
        if self.right:#if right exists
            self.right.preorder_traversal()#traverse further right
    
    def postorder_traversal(self):#traverses from the bottom up
        if self.left:#If left node exists
            self.left.postorder_traversal()#calls function on left node, pushing further down the left column.
        if self.right:#if right exists
            self.right.postorder_traversal()#traverse further right
        print(self.value)
    
    def find(self,value): #finds a value in the tree returns true if it exists and false if it doesnt.
        if value < self.value:
            if self.left is None:
                return None
            else:
                return self.left.find(value)
        elif value > self.value:
            if self.right is None:
                return None
            else:
                return self.right.find(value)
        else:
            return self


tree = TreeNode(10)
tree.insert(15)
tree.insert(13, {"name": "Sammie :)"})
tree.insert(12)
tree.insert(4)
tree.insert(5)
tree.insert(7)
tree.postorder_traversal()
print(tree.find(13).content['name'])


                     