class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def PrintList(self):
    node = self.head
    while node is not None:
        print("", node.data)
        node = node.next

def mergeSort(head1,head2):
    node1=head1
    node2=head2
    arr1=[]
    arr2=[]
    while node1 is not None:
        arr1.append(node1.data)
        node1=node1.next
    while node2 is not None:
        arr2.append(node2.data)
        node2=node2.next
    arr1=sorted(arr1)
    arr2=sorted(arr2)
    return (arr1+arr2)


e1=Node(1)
e2=Node(3)
e3=Node(7)
e4=Node(0)
e5=Node(-1)
e1.next=e2
e2.next=e3
e3.next=e4
e4.next=e5


b1=Node(45)
b2=Node(5)
b3=Node(67)
b4=Node(9)
b1.next=b2
b2.next=b3
b3.next=b4
print(mergeSort(e1,b1))







