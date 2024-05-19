from array import *

class DoubleEndedQue:
    def __init__(self,max):
        self.duque = array('i',[0] * max)
        self.Max = max
        self.front = -1
        self.rear = -1


    def isFull(self):
        return self.rear == self.Max - 1
        
    def isEmpty(self):
        return self.front == self.rear

    def EnQueueFont(self,n):
        if self.front == -1:
            print("inserting not possible")
        else:
            self.front = self.front - 1
            self.duque[self.front] = n
            print(n, " Inserted at End Successfully")
        self.display()
        
    def EnQueueRear(self,n):
        if self.isFull():
            print("Queue is Already Full !!!")
        else:
            self.duque[self.rear] = n
            self.rear = self.rear + 1
            print(n, " Inserted at End Successfully")
        self.display()

    def DeQueueFont(self):
        if self.isEmpty():
            print("Queue is Empty !!!")
        else:
            n = self.duque[self.front]
            self.front = self.front + 1
            print(n, " is Deleted from the Start Successfully")
        self.display()

    def DeQueueRear(self):
        if self.isEmpty():
            print("Queue is Empty !!!")
        else:
            self.rear = self.rear - 1
            n = self.duque[self.rear]
            print(n, " is Deleted from the Start Successfully")
        self.display()

    def display(self):
        if self.isEmpty():
            print("Queue is Empty !!!")
        else:
            i = self.front 
            while(i < self.rear):
                print(self.duque[i],end="--")
                i = i + 1

DE = DoubleEndedQue(8)

while True:
    ch = int(input('''
Press: 1 for insert at front
Press: 2 for insert at end
press: 3 for delete at front
press: 4 for delete at end
press: 5 for display
press: 0 for exit
enter your choice:: '''))
    
    if(ch == 1):
        n = int(input("Enter data: "))
        DE.EnQueueFont(n)
    elif(ch == 2):
        n = int(input("Enter data: "))
        DE.EnQueueRear(n)
    elif ch == 3:
        DE.DeQueueFont()
    elif ch == 4:
        DE.DeQueueRear()
    elif ch == 5:
        DE.display()
    elif ch == 0:
        break
    else:
        print("enterd wrong choie")


