'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word, count=0):
    target = "th"
    #base case we work toward.. if len < 2 it cannot meet target.. return
    #"The basic concept of recursion is that each call consumes part of the input, reducing it until it matches the base case."
    if len(word) < 2:
        return count
    #check if first 2 letters meets target, if they do we must increment our counter
    if word[0:2] == target:
        count += 1
    #cut off next letter and run again until we meet the base case of len < 2
    return count_th(word[1:], count)