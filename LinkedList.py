



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
single=SL()
single.head=Node("aditi")
e2=Node("20BCE10339")
e3=Node("VIT")
single.head.nextval=e2
e2.nextval=e3
single.printList()
