"""
set[]={3, 4, 5, 2}
sum=9
(x, y)= 'x' is the left number of elements,
'y' is the required sum
  
              (4, 9)
             {True}
           /        \  
        (3, 6)       (3, 9)
               
        /    \        /   \ 
     (2, 2)  (2, 6)   (2, 5)  (2, 9)
     {True}  
     /   \ 
  (1, -3) (1, 2)  
{False}  {True} 
         /    \
       (0, 0)  (0, 2)
       {True} {False}      

"""

def isSubsetSum(coins, W, N):

    # base case: 
        ## if the Weight/Sum is 0 , then return True.
        ## if there is no coin , we can't exchange , so False
    
    if (W == 0):
        return True
    if (N == 0):
        return False

    # if the element is greater than the Weight just exclude it

    if coins[N-1] > W:
        return isSubsetSum(coins, W, N-1)
    
    # else check if sum can be obtained 
    # by any of the following.
    # (a) including the element
    # (b) excluding the element

    return (isSubsetSum(coins, W, N-1) 
                or isSubsetSum(coins, W - coins[N-1], N-1))

if __name__ == '__main__':

    coins = [1, 6, 7, 8]
    W = 43
    N = len(coins)
    print(isSubsetSum(coins, W, N))