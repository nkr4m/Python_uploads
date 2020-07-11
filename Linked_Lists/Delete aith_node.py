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

def delete_aith(head, pos):
    if(pos<0 or pos>length_LL(head)):
        return

    count = 0
    prev = None
    curr = head
    while(count<pos and curr is not None):
        prev = curr
        curr = curr.next
        count = count + 1

    if(curr)is None:
        prev.next = None
    if(curr) is not None:
        prev.next = curr.next

def print_LL(head):
    while(head) is not None:
        print(head.data,end=" ")
        head = head.next

head = input_LL()
print("Linked List which you entered is.")
print_LL(head)
print()
print("Enter the positon which you want to delete.")
pos = int(input())
delete_aith(head, pos)
print("Updated LL.")
print_LL(head)
