"""
str = '{[([])]}

check brackets ?

"""

class Stack:

    def __init__(self):
        self.stack = []
    
    def isEmpty(self):
        return len(self.stack) == 0

    def push(self, val):
        self.stack.append(val)
    
    def pop(self):
        if self.isEmpty():
            print("Error: stack is empty")
        else:
            return self.stack.pop() 

    def __repr__(self):
        return f"value: {self.stack}"

def checkParenthesis(str):
    match = {
        ')' : '(',
        '}' : '{',
        ']' : '['
    }
    check = "({["
    s = Stack()
    for i in str:
        if i in check:
            s.push(i)
        else:
            ele = s.pop()
            if ele != match[i]:
                return False

    if s.isEmpty() == False:
        return False
    return True
                
if __name__ == '__main__':
    str = '{[('
    print(checkParenthesis(str))