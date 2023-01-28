class Node:
    def __init__(self,data):
        """ creating each separate nodes
        """
        self.data=data
        self.ref=None
        
class LinkedList:
    def __init__(self):
        self.head=None
        
    def print_llist(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            current_node=self.head
            while current_node is not None:
                print(current_node.data,"->",end = " ")
                current_node=current_node.ref
                
                
                
    def add_begin(self,data):
        new_node=Node(data)
        new_node.ref=self.head
        self.head=new_node
        
    def add_end(self,data):
        new_node=Node(data)
        current_node=self.head
        if self.head is None: #if linkedlist is empty
            self.head=new_node 
        else:
            while(current_node.ref is not None): #until finding tailnode
                current_node=current_node.ref
            current_node.ref=new_node    
            
            
    def add_after_node(self,data,after_node):
        current_node=self.head
        while current_node is not None:
            if(current_node.data==after_node):
                break
            current_node=current_node.ref
        if current_node is None:
            print("Not found")
        else:
            new_node=Node(data)
            new_node.ref=current_node.ref
            current_node.ref=new_node
            
            
    def add_before_node(self,data,before_node):
        if self.head is None:
            print("LL is empty")
            return
        if(self.head.data==before_node):
            new_node=Node(data)
            new_node.ref=self.head
            self.head=new_node
            return
        current_node=self.head
        while(current_node.ref is not None):
            if(current_node.ref.data==before_node):
                break
            current_node=current_node.ref
             
        if current_node.ref is None:
            print("Not found")
        else:
            new_node=Node(data)
            new_node.ref=current_node.ref
            current_node.ref=new_node
            
    def insert_at_empty_ll(self,data):
        if self.head is None:
            new_node=Node(data)
            self.head=new_node
            return
        print('LL is not empty')  
        
    def del_begin(self):
        if self.head is None:
            print("LL is Empty")
            return
        self.head=self.head.ref
    
    def del_end(self):
        current_node=self.head
        if self.head is None:
            print("LL is Empty")
            return 
        if self.head.ref is None: #only one node
            self.head=None
            return
        while(current_node.ref.ref is not None):
            current_node=current_node.ref
        current_node.ref=None
    
    def del_by_value(self,data):
        
        if self.head is None:
            print('LL is Empty') 
        elif self.head.data==data: 
            self.head=self.head.ref
        else:
            current_node=self.head
            while(current_node.ref is not None): 
                #reached lastnode 
                # (can be written in single statement using and operator )( while (current_node.ref is not None) and current_node.ref.data != data:)
                if current_node.ref.data==data: #found,previous node
                    break
                current_node=current_node.ref
            if current_node.ref is None:
                print('Not Found to delete')
            else:
                current_node.ref=current_node.ref.ref 
            
            
            
        
           
            
                    
LL1=LinkedList()

LL1.insert_at_empty_ll(22345)

LL1.add_begin(56)
LL1.add_begin(76)
LL1.add_begin(96)

LL1.add_end(456)
LL1.add_end(234)
LL1.add_end(908)

LL1.add_after_node(1000,456)
LL1.add_after_node(1000,1000)

LL1.add_before_node(999,9699)

LL1.del_beg()
LL1.del_end()
LL1.del_by_value(908)

LL1.print_llist()