"""
given an array: [2,7,4,9,5,1,3]
sum = 10
find all the triplets that have sum less than or equal to 10 ?

"""


def findAllTriplets(input, sum, triplet = [], comb= [], begin = 0):
    
    # base condition

    if len(comb) == 3:
        triplet.append(comb.copy())
        return

    i = begin
    while i < len(input) and input[i] <= sum:
        comb.append(input[i])
        findAllTriplets(input, sum - input[i], triplet, comb, i+1)
        comb.pop()
        i += 1

if __name__ == '__main__':
    input = [2,7,4,9,5,1,3]
    sum = 10
    input.sort()
    triplets = []
    findAllTriplets(input, sum, triplets)
    for trip in triplets:
        print(trip)