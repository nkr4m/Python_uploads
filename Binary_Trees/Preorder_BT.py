#Pre order BT
class BTnode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def take_input():
    rootData = int(input())
    if(rootData == -1):
        return

    root = BTnode(rootData)
    root.left = take_input()
    root.right = take_input()
    return root

def printBT(root):
    if(root) is None:
        return
    print(root.data,end=" ")
    if(root.left) is not None:
        print(root.left.data,end=" ")
    if(root.right) is not None:
        print(root.right.data,end=" ")
    print()
    printBT(root.left)
    printBT(root.right)

root = take_input()
printBT(root)