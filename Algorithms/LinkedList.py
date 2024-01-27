class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def insertAtBegin(self, data):
        new_node = Node(data)
        if self.head is None:#if head node is None
            self.head = new_node#head node is the new node
            return
        else:#if node is not none move head node to next node and make new node in head.
            new_node.next = self.head
            self.head = new_node

    def insertAtIndex(self,data,index):
        new_node = Node(data)
        current_node = self.head
        position = 0
        if position == index:#if position is equal to the index
            self.insertAtBegin(data)#insert at the start
        else:
            while(current_node != None and position+1 != index):#while the current nod is not none and the next is not equal to the index.
                position = position+1#increment position
                current_node = current_node.next#and get next node
            if current_node != None:
                new_node.next = current_node.next#new nodes next pointer points to the next node after current node.
                current_node.next = new_node#sets new node = to node after current node
            else:
                print("Index not present")

        def removeLastNode(self):
            if self.head is None:
                return
            current_node = self.head
            while(current_node.next.next):#while the next node has a next node
                current_node = current_node.next #when current node has a next node and is the second to last in the list.
            current_node.next = None#change current node to None

        def remove_at_index(self, index):
            if self.head == None:
                return
 
            current_node = self.head
            position = 0
            if position == index:
                self.remove_first_node()
            else:
                while(current_node != None and position+1 != index):
                    position = position+1
                    current_node = current_node.next
 
            if current_node != None:
                current_node.next = current_node.next.next
            else:
                print("Index not present") 
        