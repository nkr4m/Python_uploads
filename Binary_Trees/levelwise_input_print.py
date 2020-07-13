#level wise input and print

import queue
class BTnode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def take_input():
    q = queue.Queue()
    print("Enter the root data")
    rootData = int(input())
    if(rootData == -1):
        return None
    root = BTnode(rootData)
    q.put(root)

    while(not(q.empty())):
        curr_node = q.get()
        print("Enter the left child of ", curr_node.data)
        leftCdata = int(input())
        if(leftCdata != -1):
            leftC = BTnode(leftCdata)
            curr_node.left = leftC
            q.put(leftC)

        print("Enter the right child of ", curr_node.data)
        rightCdata = int(input())
        if (rightCdata != -1):
            rightC = BTnode(rightCdata)
            curr_node.right = rightC
            q.put(rightC)

    return root

def print_BT(root):
    q = queue.Queue()
    if(root) is None:
        return
    q.put(root)

    while(not(q.empty())):
        curr_node = q.get()
        print(curr_node.data,end=":")
        if(curr_node.left) is not None:
            print(curr_node.left.data,end=" ")
            q.put(curr_node.left)
        if(curr_node.right) is not None:
            print(curr_node.right.data,end=" ")
            q.put(curr_node.right)

        print()

root = take_input()
print_BT(root)