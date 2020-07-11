class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def input_LL():
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

def print_LL(head):
    while(head) is not None:
        print(head.data,end=" ")
        head = head.next

head = input_LL()
print_LL(head)
