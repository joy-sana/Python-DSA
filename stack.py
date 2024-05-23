from array import array

class StackArray:
    def __init__(self, MAX):
        self.MAX = MAX
        self.stack = array('i', [0] * self.MAX)
        self.top = -1

    def push(self, n):
        if self.top == self.MAX - 1:
            print("Stack overflow")
        else:
            self.top += 1
            self.stack[self.top] = n
            print(n, "is pushed in stack")

    def pop(self):
        if self.top == -1:
            print('Stack underflow')
        else:
            n = self.stack[self.top]
            self.top -= 1
            print(n, 'is popped')

    def display(self):
        if self.top == -1:
            print("Stack underflow")
        else:
            print("Here is the stack:")
            for i in range(self.top, -1, -1):
                print("*", self.stack[i], "*")
            print("******")

s = StackArray(3)
print('''Press: 1 for push
Press: 2 for pop
Press: 3 for display
Press: 0 for exit
''')
while True:
    ch = int(input('''Enter your choice: '''))
    
    if ch == 1:
        n = int(input("Enter data: "))
        s.push(n)
    elif ch == 2:
        s.pop()
    elif ch == 3:
        s.display()
    elif ch == 0:
        break
    else:
        print("Entered wrong choice")
