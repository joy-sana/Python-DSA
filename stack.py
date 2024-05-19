from array import *
MAX = 5

class StackArray:
    stack = array('i',[0,0,0,0,0])
    top = -1
    def push(self,n):
        if self.top == MAX - 1:
            print (" stack overflow")
        else:
            self.top = self.top + 1
            self.stack[self.top] = n
            print(n,"is pushhed in stack")
    def pop(self):
        if self.top == -1:
            print('Stack underflow')
        else:
            n = self.stack[self.top]
            self.top = self.top - 1
            print(n, ' poped')
    def display(self):
        if self.top == -1:
            print("stack under flow")
        else:
            print("here is the stack::")
            print(" ")
            for i in range (self.top,-1,-1):         
                print("*",self.stack[i],"*")
            print("******")

s = StackArray()

while True:
    ch = int(input('''Press: 1 for push
Press: 2 for pop
press:3 for display
press:0 for exit
enter your choise:: '''))
    
    if(ch == 1):
        n = int(input("Enter data: "))
        s.push(n)
    elif(ch == 2):
        s.pop()
    elif ch == 3:
        s.display()
    elif ch == 0:
        break
    else:
        print("enterd wrong choice")


