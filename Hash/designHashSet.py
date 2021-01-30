"""
Design a hashset with out using a hashtable library.
you can add, remove or check a number present or not.
1M rows posssible.

"""

# create a bucket of 1000 , each bucket can keep 1000 elements.
class HashSet:

    def __init__(self):
        self.array = [[] for _ in range(1000)]
    
    def add(self, key: int) -> None:
        subkey = key % 1000
        if not self.contains(key):
            self.array[subkey].append(key)
    
    def remove(self, key: int) -> None:
        subkey = key % 1000
        if  self.contains(key):
            self.array[subkey].remove(key)

    def contains(self, key: int) -> bool:
        subkey = key % 1000
        return key in self.array[subkey]


if __name__ == '__main__':
    dhash = HashSet()
    dhash.add(100)
    dhash.add(100000)
    dhash.add(5)
    print(dhash.contains(100))
    print(dhash.contains(1000))
    print(dhash.contains(5))
    print(dhash.remove(5))
    print(dhash.contains(5))