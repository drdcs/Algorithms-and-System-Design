"""
Merge M sorted List:

Input: 4 sorted lists of variable length
 
[ 10, 20, 30, 40 ]
[ 15, 25, 35 ]
[ 27, 29, 37, 48, 93 ]
[ 32, 33 ]

O/P : 10 15 20 25 27 29 30 32 33 35 37 40 48 93


Approach: Construct a min heap of size M and insert the first element of ach 
list into it.
Then pop the root (which is min) from the heap and insert the next element
from the same list which is poped.
repeat till the heap exhausted.

"""

code: https://www.techiedelight.com/merge-m-sorted-lists-variable-length/



