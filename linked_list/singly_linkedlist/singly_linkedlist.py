#program tto display linkedlist:
class Node :
    def __init__(self,data):
        self.data=data
        self.next=None
#create manual list:
head=Node(10)
head.next=Node(20)
head.next.next=Node(30)
#Traversal :
temp=head
while temp:
    print(temp.data,end="->")
    temp=temp.next
print("NULL")#10->20->30->NULL

#inserting a node at beginning:
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
head=Node(40)
head.next=Node(50)
new_node=Node(30)
new_node.next=head
head=new_node
temp=head
while temp:
    print(temp.data,end="->")
    temp=temp.next
print("NULL")#30->40->50->NULL

#Insertion at the end:
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
#Create manual list:
head=Node(100)
head.next=Node(200)
#create new node:
new_node=Node(300)
temp=head
while temp.next:
    temp=temp.next
#display the linkedlist:
temp.next=new_node
temp=head
while temp:
    print(temp.data,end="->")
    temp=temp.next
print("NULL")#100->200->300->NULL

#delete a node:
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
head=Node(500)
head.next=Node(600)
head.next.next=Node(700)
key=500
temp=head
prev=None
while temp and temp.data!=key:
    prev=temp
    temp=temp.next
if temp==head:
    head=head.next
elif temp:
    prev.next=temp.next
temp=head
while temp:
    print(temp.data,end="->")
    temp=temp.next
print("NULL")#500->700->NULL