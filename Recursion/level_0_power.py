def power_of_numbers(a, b):
    
    if b == 0:
        return 1

    return a * power_of_numbers(a, b-1)
    

if __name__ == '__main__':
    a = 3
    b = 4
    print(power_of_numbers(a, b))