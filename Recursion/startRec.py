def printNum(n: int):
    if n==7:
        return 1
    print(n, end= "->")
    printNum(n+1)

def printNumReverse(n: int):
    if n==0:
        return 1
    print(n, end="->")
    printNumReverse(n-1)
    
if __name__ == '__main__':
    printNum(1)
    print('\n')
    printNumReverse(6)
    print('\n')