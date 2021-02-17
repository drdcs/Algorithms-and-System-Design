

def subsequence_string(s, output):

    if len(s)== 0:
        print(output, end = " ")
        return

    # adding the 1st character in string
    subsequence_string(s[:-1], output + s[-1])
    # not adding the 1st character of the string
    # because the concept of subsequence is pick one.
    # i.e either the character is present or not.
    subsequence_string(s[:-1], output)

if __name__ == '__main__':
    s = 'abc'
    subsequence_string(s, '')
    
    