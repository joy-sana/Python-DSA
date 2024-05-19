from array import *
Max = 5

class QueueArray:
    queue = array('i', [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
    rear = -1
    front  = -1
    def insertion(self,n):
        if (self.rear == Max -1):
            print('queue overflow:')
        else:
            self.rear += 1
            self.queue[self.rear] = n
            print(n, 'is inserted')
    def deletion(self):
        if self.rear == self.front:
            print('empty queue!!')
        else:
            n = self.queue[self.front+1]
            self.front += 1
            print(n, "is deleted from queue")
    def display(self):
        if self.rear == self.front:
            print('empty queue')
        else:
            print("*** queue ***")
            for i in range(self.front+1,self.rear+1):
                print(self.queue[i],end=", ")

Q = QueueArray()

while True:
    ch = int(input('''
Press: 1 for insert
Press: 2 for delete
press: 3 for display
press: 0 for exit
enter your choise:: '''))
    
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
        print("enterd wrong choice")

            