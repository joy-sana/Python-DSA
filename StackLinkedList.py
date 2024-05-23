class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def push(top, n):
    newnode = Node(n)
    newnode.next = top
    top = newnode
    return top  
def pop(top):
    if top == None:
        print("Empty Stack")
        return top
    else:
        print("Deleted item", top.data)
        top = top.next
        return top
def display(top):
    temp = top
    if temp == None:
        print("Empty Stack")
    while(temp):
        print(temp.data)
        temp = temp.next
top = None
while True:
    print("**** Main Menu ****")
    print("1. PUSH")
    print("2. POP")
    print("3. DISPLAY")
    print("0. EXIT")
    
    ch = int(input("Enter your choice: "))

    if(ch==1):
        n = int(input("Enter data:"))
        top = push(top, n)
    elif(ch==2):
        top = pop(top)
    elif(ch==3):
        display(top)
    elif(ch==0):
        break
    else:
        print("Wrong Input")
        pass