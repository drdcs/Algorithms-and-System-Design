"""
Given a stack, sort it using recursion. Use of any loop constructs like while, for..etc is not allowed. We can only use the following ADT functions on Stack S: 

is_empty(S)  : Tests whether stack is empty or not.
push(S)        : Adds new element to the stack.
pop(S)         : Removes top element from the stack.
top(S)         : Returns value of the top element. Note that this
                 function does not remove element from the stack.


Input:  -3  <--- Top
        14 
        18 
        -5 
        30 

Output: 30  <--- Top
        18 
        14 
        -3 
        -5 

"""

# Until stack is empty or having element greater than top element then Push it.
# else pop the top element and recursively 

class Stack:

    def __init__(self):
        self.arr = []
    
    def push(self, element):
        return self.arr.append(element)

    def pop(self):
        if self.isEmpty:
            return self.arr.pop()
    
    def peek(self):
        return self.arr[-1]

    def isEmpty(self):
        return len(self.arr) == 0

    def printStack(self):
        return self.arr


def sortStack(stack: Stack):
    if not stack.isEmpty():
        temp = stack.pop()
        print("temp: ", temp)
        sortStack(stack)
        sortedInsert(stack, temp)

def sortedInsert(s: Stack, element: int):

    # base condition: either stack is empty or newly inserted 
    # element is greater than top of the stack.
    print("element: ",element)
    if s.isEmpty() or element > s.peek():
        s.push(element)
        return

    else:
        temp = s.pop()
        sortedInsert(s, element)
        s.push(temp)

if __name__ == '__main__':
    s = Stack()
    s.push(30)
    s.push(-5)
    s.push(18)
    s.push(14)
    s.push(-3)
    print("stack: before sorting", s.printStack())
    sortStack(s)
    print("stack: after sorting", s.printStack())

    ## Test Stack
    # stack = Stack()
    # stack.push(1)
    # stack.push(2)
    # print(stack.peek())
    # stack.pop()
    # print(stack.peek())
    # print(stack.isEmpty())
    # stack.pop()
    # print(stack.isEmpty())