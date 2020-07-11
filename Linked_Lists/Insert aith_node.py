class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def input_LL():
    print("Enter the linked list and terminate by -1.")
    li = [int(x) for x in input().split()]
    head = None
    tail = None
    for ele in li:
        if(ele == -1):
            break

        newNode = Node(ele)
        if(head) is None:
            head = newNode
            tail = newNode
        if(head) is not None:
            tail.next = newNode
            tail = newNode
    return head

def length_LL(head):
    count = 0
    while(head) is not None:
        count = count + 1
        head = head.next
    return count

def insert_aith(head, pos, data):
    if(pos<0 or pos>length_LL(head)):
        return None

    count = 0
    prev = None
    curr = head
    while(count<pos):
        prev = curr
        curr = curr.next
        count = count + 1

    newNode = Node(data)
    if(prev) is None:
        head = newNode
    if(prev) is not None:
        prev.next = newNode
    newNode.next = curr

def print_LL(head):
    while(head) is not None:
        print(head.data,end=" ")
        head = head.next

head = input_LL()
print("Linked List which you entered is.")
print_LL(head)
print()
print("Enter the position on which you want to add a node.")
pos = int(input())
print("Enter the data for the new node.")
data = int(input())
insert_aith(head, pos, data)
print("Updated Linked List, with a new node at position:",pos,"with data:", data,"is.")
print_LL(head)