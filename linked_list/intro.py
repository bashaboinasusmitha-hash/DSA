'''linked list is a linear data structures.made up of two nodes.
each node consists "Data" and "reference to next node".Not stored in contiguous memory.'''
#Node Structure:
'''node=Data+Pointer
Representation: [data|next]->[data|next]->NULL'''
#key idea:
'''Arrays=move with index.
Linkedlist=moves using links(next)'''
#Types of linkedlists:
'''There are mainly Three types of linkedlist:
1) Singly linkedlist
2) double linkedlist
3) circular linkedlist.'''
#Singly linkedlist:
'''in single linkedlist each node consists of "Data" and "pointer to next node only"
it traverse in only forward direction.
Representation:[10| ]->[20| ] ->[30| ]'''
#Double linkedlist:
'''in double inkedlist each node consists of "Data","pointer to next node","pointer to previous node".
it travere both forward nd backward.
Representation:NULL <- [10| | ]-><- [20| | ]->NULL'''
#Circular linkedlist:
'''in circular linked list there is no NULL at the end.
The last node connects back to first node(head).forms a cycle
Representation: [10| ]->[20| ]->[30| ]
                  |<---------------<|'''