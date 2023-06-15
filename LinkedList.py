#Creation and insertion of noes in linked list

class Node:
    def __init__(self,value):
        self.dataval=value
        self.nextval=None




class SL:
    def __init__(self):
        self.head=None
    def printList(self):
        nodes=self.head
        while nodes is not None:
            print(nodes.dataval)
            nodes=nodes.nextval
    def InsertFront(self,newValue):

        new_node=Node(newValue)
        new_node.nextval=self.head

        self.head=new_node
    def InsertEnd(self,newValue):
        new_node=Node(newValue)
        node=self.head
        while node.nextval is not None:
            node=node.nextval
        node.nextval=new_node

    def InsertAtPos(self,newValue,pos):
        count=0
        new_Node=Node(newValue)
        node=self.head
        while node is not None:
            count=count+1
            if count==pos:
                new_Node.nextval=node.nextval
                node.nextval=new_Node

            else:
                node=node.nextval
    def InsertAtMiddle(self,newvalue):
        count=0
        node=self.head
        new_Node=Node(newvalue)
        while node is not None:
            count=count+1
            node=node.nextval
        middle=count/2
        c=0
        NODE=self.head
        while NODE is not None:
            c=c+1
            if c==middle-1:
                new_Node.nextval=NODE.nextval
                NODE.nextval=new_Node
            else:
                NODE=NODE.nextval





single=SL()
single.head=Node("aditi")
e2=Node("20BCE10339")
e3=Node("VIT")
single.head.nextval=e2
e2.nextval=e3
single.printList()
print("------------------")
single.InsertFront("VELLORE INSTITUTE OF TECHNOLOGY")
single.printList()
print("---------------------")
single.InsertEnd("CSE CORE")
single.printList()
print("---------------------")
single.InsertAtPos("Batch OF 24",3)
single.printList()
print("----------------------")
single.InsertAtMiddle("Aarushi is beautiful")
single.printList()




