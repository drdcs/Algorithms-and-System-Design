"""
Given two strings text1 and text2, return the length of their longest common subsequence.
A subsequence of a string is a new string generated from the original string with some characters(can be none) 
deleted without changing the relative order of the remaining characters.
 (eg, "ace" is a subsequence of "abcde" while "aec" is not). 
 A common subsequence of two strings is a subsequence that is common to both strings.

Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.

            " " a  b  c  d  e
         " " 0  0  0  0  0  0
          a  0  1  1  1  1  1
          c  0  1  1  2  2  2
          e  0  1  1  2  2  3

          Every element has 2 options : either include or exclude,
          If the element matches the 1 + left diagonal(matrix[row-1][col-1])
          If not matches then either we can leave the element by 
                matrix[row][col-1] or leave the existing combination by matrix[row-1][column]
                by taking the maximum of both the criteria can give us the maximum of the two. 

"""

def longestCommonSubsequence(str1, str2):
    str1_l = len(str1)
    str2_l = len(str2)
    DP = [[0 for x in range(str1_l+1)] for y in range(str2_l+1)]
    # str2 is row and str1 is column from above dp construction .. 
    for i in range(1, str2_l+1):
        for j in range(1, str1_l+1):
            if str1[j-1] == str2[i-1]:
                DP[i][j] = 1 + DP[i-1][j-1]
            else:
                DP[i][j] = max(DP[i-1][j], DP[i][j-1])
    return DP[-1][-1]


if __name__ == '__main__':
    str1 = "abcde"
    str2 = "ace"
    print(longestCommonSubsequence(str1, str2))
