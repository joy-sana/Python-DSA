from array import *
MAX = 5

class CirculerQueue:
    CQueue = array('i',[0,0,0,0,0])
    front = 0
    rear = 0
    
    def insertion (self, n):
        if ((self.rear + 1) % MAX == self.front):
            print("Queue Overflow!!!")
        else:
            self.CQueue[self.rear] = n
            self.rear = (self.rear + 1) % MAX
            print("One Item Added!")
        self.display()

    def deletion(self):
        if (self.front == self.rear):
            print("Queue is Empty!")
        else:
            n = self.CQueue[self.front]
            self.front = (self.front + 1) % MAX
            print(n , " is Deleted")
        self.display()


    def display(self):
        if (self.front == self.rear):
            print("Queue is Empty!")
        else: 
            print("***QUEUE***")
            i = self.front
            while(i != self.rear):
                print(self.CQueue[i],end="--")
                i = (i + 1) % MAX


Q = CirculerQueue()

while True:
    ch = int(input('''
Press: 1 for insert
Press: 2 for delete
press: 3 for display
press: 0 for exit
enter your choice:: '''))
    
    if(ch == 1):
        n = int(input("Enter data: "))
        Q.insertion(n)
    elif(ch == 2):
        Q.deletion()
    elif ch == 3:
        Q.display()
    elif ch == 0:
        break
    else:
        print("enterd wrong choie")
