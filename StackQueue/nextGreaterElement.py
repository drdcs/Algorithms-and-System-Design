"""
Next greater element:

input: [18,7,6,12,15]
output:[-1,12,12,15,-1]

18, 7, 6, 
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

def getNextGreater(array):
    s = Stack()
    s.push(array[0])
    for i in range(1, len(array)):
        next = array[i]
        if s.isEmpty() == False:
            # if stack is not empty
            element = s.pop()
            # if poped element is smaller than the next
            # append the result
            # keep popping up while element are smaller
            # and stack is not empty
            while element < next:
                print("element: ", element, "next: ", next)
                if s.isEmpty == True:
                    break
                element = s.pop()
            # if element is greater than next then push
            # the element
            if element > next:
                s.push(element)
        s.push(next)

if __name__ == '__main__':
    array = [18,7,6,1,15]
    # stack = Stack()
    # for i in array:
    #     stack.push(i)
    # print(stack)
    # stack.pop()
    # stack.pop()
    # print(stack)
    print(getNextGreater(array))