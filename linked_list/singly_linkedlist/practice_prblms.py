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
