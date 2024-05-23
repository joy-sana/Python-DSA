'''
Simply Linked List

1. Display [Done]
2. Insert at Begining 
3. Insert at Ending [Done]
4. Count no of node 
5. Search an element (Linear Search)
6. Deletion
7. Main function
'''

class Node:
    def __init__ (self,data):
        self.data = data
        self.next = None

def Display(head):
    temp = head

    if temp == None:
        print("Empty List")
    else:
        print("Elements of Linked List: ")
        while(temp):
            print(temp.data)
            temp = temp.next

def InsertEnd(head,value):
    if head == None:
        head = Node(value)
        return head
    else:
        temp = head
        while(temp):
            prev = temp
            temp = temp.next
        newNode = Node(value)
        prev.next = newNode
        return head
    
    
def InsertBeg(head,value):
    if head == None:
        head = Node(value)
        return head
    
    temp = head
    newNode = Node(value)
    newNode.next = temp

    return newNode

def Count(head):
    temp = head
    count = 0
    while(temp):
        temp = temp.next
        count += 1
    return count

def Search(head,n):
    temp = head
    count = 1
    flag = 0
    while(temp):
        if temp.data == n:
            flag = 1
            print(f"{n} Element is Found on {count} Number Index. ")
        temp = temp.next
        count += 1

    if flag == 0:
        print("Element NOT FOUND")


def Deletion(head, index):
    if head is None:
        print("List is empty.")
        return head

    temp = head

    if index == 0:
        head = temp.next
        temp = None
        return head

    for i in range(index - 1):
        temp = temp.next
        if temp is None:
            break

    if temp is None or temp.next is None:
        print("Index out of range.")
        return head

    next = temp.next.next
    temp.next = None
    temp.next = next
    return head


head = None
while True:
    x = int(input('''
Press: 1 for Display
Press: 2 for Insert at End
press: 3 for Insert at Beg
press: 4 for Counting Number of Element
press: 5 for Seaching any Element by Value
press: 6 for delete by Index
press: 0 for exit
enter your choise:: '''))
    print("")

    match x:
        case 1:
            Display(head)
        case 2:
            data = int(input("Enter data to insert at End:: "))
            head = InsertEnd(head,data) 
        case 3:
            data = int(input("Enter data to insert at first:: "))
            head = InsertBeg(head,data)
        case 4:
            NumberOfNode = Count(head)
            print(f"Number of Element present on Linked list is :: {NumberOfNode}")
        case 5:
            n = int(input("Enter the number you want to search:: "))
            Search(head,n)
        case 6:
            n = int(input("Enter the index for deletion: "))
            head = Deletion(head,n)
        case 0: 
            break
        case _:
            print("Wrong Choice") 
