class InfixToPostfix:
    def __init__(self, infix):
        self.infix = infix
        self.stack = []
        self.stream = []
    
    def genPostfix(self):
        for c in self.infix:
            if c in '*/+-%^()':
                if c == '+' or c == '-':
                    while len(self.stack) != 0 and self.stack[-1] != '(':
                        self.stream.append(self.stack.pop())
                    self.stack.append(c)
                elif c == '^' or c == '(':
                    self.stack.append(c)
                elif c == ')':
                    while len(self.stack) != 0 and self.stack[-1] != '(':
                        self.stream.append(self.stack.pop())
                    if len(self.stack) == 0:
                        raise RuntimeError('Mismatched Parentheses')
                    elif self.stack[-1] == '(':
                        self.stack.pop()
                elif c == '*' or c == '/' or c == '%':
                    while len(self.stack) != 0 and not (self.stack[-1] != '+' or self.stack[-1] != '-'):
                        self.stream.append(self.stack.pop())
                    self.stack.append(c)
                else:
                    raise RuntimeError('Unknown Operator in Infix')
            else:
                self.stream.append(c)
    
        while len(self.stack) != 0 and self.stack[-1] != '(':
            self.stream.append(self.stack.pop())
    
        return ''.join(self.stream)
    
for _ in range(int(input())):
    i = InfixToPostfix(input())
    print(i.genPostfix()) 