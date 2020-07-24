'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # Use recursion to solve problem of counting 'th' within any given word.
    # No for loops
    count = 0
    # Check if 'th' exists using python "in"
    if 'th' in word:

        # increment count by 1
        count = count + 1
        # get index of the first 'th'
        idx = word.index('th')
    
        return count + count_th(word[idx+2:])
    
    else:
        # no more th's in the word
        return count