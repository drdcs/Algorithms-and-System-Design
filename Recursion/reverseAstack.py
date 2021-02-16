"""
Given a stack with push(), pop(), empty() operations,
reverse the stack.

Input  : Stack[] = [1, 2, 3, 4, 5]
Output : Stack[] = [5, 4, 3, 2, 1]

"""

class Stack: 

    def __init__(self): 
        self.items = [] 
       
    def isEmpty(self): 
        return self.items == [] 
       
    def push(self, item): 
        self.items.append(item) 
       
    def pop(self): 
        return self.items.pop() 
       
    def peek(self): 
        return self.items[-1] 
       
    def size(self): 
        return len(self.items)

    def prints(self):
        return self.items


def insertAtBottom(stack: Stack, item):
    if stack.isEmpty():
        stack.push(item)
    else:
        temp = stack.pop()
        insertAtBottom(stack, item)
        stack.push(temp)

def reverseStack(stack: Stack):
    if not stack.isEmpty():
        temp = stack.pop()
        reverseStack(stack)
        insertAtBottom(stack, temp)
        

if __name__ == '__main__':
    s = Stack()
    arr = [1, 2, 3, 4, 5, 6]
    for item in arr:
        s.push(item)
    
    print("before deletion: ", s.prints())
    reverseStack(s)
    print("after deletion: ", s.prints())
