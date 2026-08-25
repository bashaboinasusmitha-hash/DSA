class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
head = Node(1)
head.next = Node(2)
head.next.next = Node(6)
head.next.next.next = Node(3)
head.next.next.next.next = Node(4)
head.next.next.next.next.next = Node(5)
head.next.next.next.next.next.next = Node(6)
val=6
while head and head.val==val:
    head=head.next
temp=head
while temp and temp.next:
    if temp.next.val==val:
        temp.next=temp.next.next
    else:
        temp=temp.next
temp=head
while temp:
    print(temp.val,end="->")
    temp=temp.next
print("NULL")#1->2->3->4->5->NULL

#display a linkedlist:
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
head=Node(10)
head.next=Node(20)
head.next.next=Node(30)
temp=head
while temp:
    print(temp.data,end="->")
    temp=temp.next
print("NULL")#10->20->30->NULL

#adding a node at the beginning:
class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
#create list manually
head=Node(200)
head.next=Node(300)
new_node=Node(100)
new_node.next=head
head=new_node
temp=head
while temp:
    print(temp.val,end="->")
    temp=temp.next  
print("NULL")#100->200->300->NULL

#create node at end:
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
head=Node(100)
head.next=Node(200)
head.next.next=Node(300)
new_node=Node(400)
temp=head
while temp.next:
    temp=temp.next
temp.next=new_node
temp=head
while temp:
    print(temp.data,end="->")
    temp=temp.next
print("NULL")#100->200->300->400->NULL

#insert the node at particular position:
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
head=Node(10)
head.next=Node(20)
head.next.next=Node(40)
#insert value:
value=30
pos=2
new_node=Node(value)
if pos==0:
    new_node.next=head
    head = new_node
else:
    temp=head
    for i in range(pos-1):
        temp=temp.next#temp becomes 20 (temp=10 now assigning temp.next to temp)
    new_node.next=temp.next #(assigning the address of 40 to new node)
    temp.next=new_node
temp=head
while temp:
    print(temp.data,end="->")
    temp=temp.next
print("NULL")#10->20->30->40->NULL

#delete a node:
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
head=Node(10)
head.next=Node(20)
head.next.next=Node(40)
head.next.next.next=Node(30)

key=20
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
print("NULL")#20->40->30->NULL

#delete node at the beginning:
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
head=Node(10)
head.next=Node(20)
head.next.next=Node(40)
head.next.next.next=Node(30)
head=head.next
temp=head
while temp:
    print(temp.data,end="->")
    temp=temp.next
print("NULL")#20->40->30->NULL

