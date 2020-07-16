import queue
class Node:
    def __init__(self,data):
        self.data = data
        self.children = list()

def take_input():
    q = queue.Queue()
    print("Enter the root data")
    rootData = int(input())
    if(rootData == -1):
        return
    root = Node(rootData)
    q.put(root)

    while(not(q.empty())):
        curr_node = q.get()
        print("Enter the number of childrens of", curr_node.data)
        num_child = int(input())
        count = 1
        for child in range(0,num_child,1):
            print("Enter the child data number:", count)
            count = count + 1
            childData = int(input())
            childN = Node(childData)
            curr_node.children.append(childN)
            q.put(childN)
    return root

def printGT(root):
    q = queue.Queue()
    if(root) is None:
        return
    q.put(root)
    while(not(q.empty())):
        curr_node = q.get()
        print(curr_node.data,end=" ")
        for child in curr_node.children:
            print(child.data,end=" ")

        print()
        for child in curr_node.children:
            printGT(child)

root = take_input()
printGT(root)
