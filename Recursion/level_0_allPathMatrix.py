def numberOfPaths(m,n):
    if m == 1 or n == 1:
        return 1
    return numberOfPaths(m-1, n) + numberOfPaths(m, n-1)

if __name__ == '__main__':
    m = 4
    n = 5
    print(numberOfPaths(m,n))