"""
Given a stack with push(), pop(), empty() operations, delete middle of it without using any additional data structure.

Input  : Stack[] = [1, 2, 3, 4, 5]
Output : Stack[] = [1, 2, 4, 5]

Input  : Stack[] = [1, 2, 3, 4, 5, 6]
Output : Stack[] = [1, 2, 4, 5, 6]

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

def deleteMid(stack: Stack, n: int, curr: int):

    # base condition.
    # if stack is empty
    # and all elements are traversed

    if stack.isEmpty() or curr == n:
        return

    temp = stack.peek()
    stack.pop()

    deleteMid(stack, n, curr +1)

    if curr != int(n/2):
        stack.push(temp)


if __name__ == '__main__':
    s = Stack()
    arr = [1, 2, 3, 4, 5, 6]
    for item in arr:
        s.push(item)
    print("before deletion: ", s.prints())
    deleteMid(s, len(arr), 0)
    print("after deletion: ", s.prints())