def precedence(op):
    if op == '+' or op == '-':
        return 1
    if op == '*' or op == '/':
        return 2
    if op == '^':
        return 3
    return 0
def infixToPostfix(expression):
    stack = []
    output = []
    for char in expression:
        if char.isalnum():
            output.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
        else:
            while stack and precedence(stack[-1]) >= precedence(char):
                output.append(stack.pop())
            stack.append(char)
    while stack:
        output.append(stack.pop())
    return ''.join(output)
    
def infixToPrefix(expression):
    expression = expression[::-1]
    expression = expression.replace('(', 'temp')
    expression = expression.replace(')', '(')
    expression = expression.replace('temp', ')')
    postfix = infixToPostfix(expression)
    prefix = postfix[::-1]
    return prefix

expression = "a+b*(c^d-e)^(f+g*h)-i"
print("Infix expression:", expression)
print("Postfix expression:", infixToPostfix(expression))
