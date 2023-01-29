class Node:
     def __init__(self,data):
         self.data=data
         self.pref=None
         self.nref=None
         
class DoublyLinkedList:
    def __init__(self):
        self.head=None
    
    def print_forward_LL(self):
        if self.head is None:
            print("LL is empty FF")
            return
        current_node=self.head
        while(current_node is not None):
            print(current_node.data,"--f-->",end=" ")
            current_node=current_node.nref
            
    def print_backward_LL(self):
        if self.head is None:
            print("LL is empty BB")
            return
        current_node=self.head
        while(current_node.nref is not None):#reach lastnode
            current_node=current_node.nref
        while(current_node is not None):
            print(current_node.data,"--b-->",end=" ")
            current_node=current_node.pref
            
    def add_begin(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return
        new_node.nref=self.head
        self.head.pref=new_node
        self.head=new_node
        
    def add_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return
        current_node=self.head
        while(current_node.nref is not None): # reach lastnode
            current_node=current_node.nref
        new_node.pref=current_node
        current_node.nref=new_node
            
    def insert_empty(self,data):
        if self.head is None:
            new_node=Node(data)
            self.head =new_node
            return
        print("DLL is not empty") 
          
          
    def add_afternode(self,data,after_node):
        if self.head is None:
            print("DLL is Empty")
            return
        current_node=self.head
        while(current_node is not None):
            if current_node.data == after_node:
                break
            current_node=current_node.nref
        if current_node is None:
            print("Not Found")
            return
        new_node=Node(data)
        new_node.pref=current_node
        if current_node.nref is not None:
             current_node.nref.pref=new_node
        new_node.nref=current_node.nref     
        current_node.nref=new_node
       
    
    def add_beforenode(self,data,before_node):
        if self.head is None:
            print("DLL is Empty")
            return
        
        current_node=self.head
        new_node=Node(data)
        if current_node.data==before_node:
            current_node.pref=new_node
            new_node.nref=current_node
            self.head=new_node
            return
        while(current_node.nref is not None):
            if current_node.nref.data==before_node:
                break
            current_node=current_node.nref
        if current_node.nref is None:
            print("Not Found")
        else:
            new_node.nref=current_node.nref
            new_node.pref=current_node
            current_node.nref.pref=new_node
            current_node.nref=new_node
            
    
    
    def del_begin(self):
        if self.head is None:
            print("DLL is empty")
        elif self.head.nref is None:
            self.head=None
        else:
            self.head=self.head.nref
            self.head.pref=None
            
    def del_end(self):
        if self.head is None:
            print("DLL is empty")
        elif self.head.nref is None:
            self.head=None
        else:
            current_node=self.head
            while(current_node.nref is not None):
                current_node=current_node.nref
            current_node.pref.nref=None
            
    def del_by_value(self,data):
        if self.head is None:
            print("DLL is empty")
        elif self.head.nref is None:
            if self.head.data==data:
                self.head =None
            else:
                print("Not found")
        else:
            current_node=self.head
            while(current_node.nref is not None):
                if current_node.data==data:
                    break
                current_node=current_node.nref
            if current_node.nref is not None:
                current_node.pref.nref=current_node.nref
                current_node.nref.pref=current_node.pref
            else:
                if current_node.data==data:
                    current_node.pref.nref=None
                else:
                    print("Not found")
                
                
            
            
            
            
            
            
            
            
            
            
        
        
        

            
            
            
            
            
            
            
            
DLL=DoublyLinkedList()

DLL.insert_empty(45342)
DLL.add_begin(56)
DLL.add_begin(786)
DLL.add_begin(980)
DLL.add_end(2380)

DLL.add_beforenode(7456,980)
DLL.add_afternode(3456,786)

DLL.del_begin()
DLL.del_end()
DLL.del_by_value(2380)

DLL.print_forward_LL()
print()
DLL.print_backward_LL()
