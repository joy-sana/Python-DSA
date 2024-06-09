from array import *
class DoubleEndedQue:
    def __init__(self,max):
        self.Max = max
        self.deque = array('i',[0] * self.Max)
        self.front = -1
        self.rear = -1
    def isEmpty(self):
        return self.front == self.rear
    def EnQueueFont(self,n):
        if self.front == -1:
            print("inserting not possible")
        else:
            self.deque[self.front] = n
            self.front = self.front - 1
            print(n, " Inserted at front Successfully")
    def EnQueueRear(self,n):
        if self.rear == self.Max - 1:
            print("Queue is Already Full !!!")
        else:
            self.rear = self.rear + 1
            self.deque[self.rear] = n
            print(n, " Inserted at End Successfully")
    def DeQueueFont(self):
        if self.isEmpty():
            print("Queue is Empty !!!")
        else:
            self.front = self.front + 1
            n = self.deque[self.front]
            print(n, " is Deleted from the Start Successfully")
    def DeQueueRear(self):
        if self.isEmpty():
            print("Queue is Empty !!!")
        else:
            n = self.deque[self.rear]
            self.rear = self.rear - 1
            print(n, " is Deleted from the End Successfully")
    def display(self):
        if self.isEmpty():
            print("Queue is Empty !!!")
        else:
            i = self.front + 1
            while(i <= self.rear):
                print(self.deque[i],end=",")
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


