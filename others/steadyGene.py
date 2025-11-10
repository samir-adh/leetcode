#!/bin/python3

#
# Complete the 'steadyGene' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING gene as parameter.
#
# given a string s we must find the smallest substring that can be replaced 
# to make s steady
# note : we don't care about the exact order of the letters containing the replacing substring
# example : n = 8, actgaaag -> a : 4, c: 1, t:1, g: 2
# that means we need to add 1 c, 1 t and remove 2 a
# naive idea: start with window_size = 2 because we need to make 2 changes
# slide a window of size window_size to see if there is somewhere that contains 2 a, if so return window_size
# else increase window_size by one and repeat
# optimized idea:
# diffs = number of changes to make (how do we calculate it ?)
# min_len = n
# start with left = 0 and right = 2
# while left < n :
#   if len(diffs) <= right-left :
#       right += 1
#   if s[left:right] contains the chars to remove:
#       min_len = min(min_len, right-left)
#       left += 1
#   else:
#       right += 1
# actgaag
# 


def steadyGene(gene):
    # Write your code here
    char_count = {k: 0 for k in 'ACTG'}
    for char in gene:
        char_count[char] += 1
    n = len(gene)
    target = n // 4
    
    excess_chars = {}
    for char, value in char_count.items():
        if value > target:
            excess_chars[char] = value-target

    if not excess_chars:
        return 0
    
    window_count= {k: 0 for k in 'ATCG'}
    left = 0
    right = 0
    min_len = n
    while right <= n:
        substring_is_valid = True
        for char, num_to_remove in excess_chars.items():
            if window_count[char] < num_to_remove:
                substring_is_valid=False
                break
        if not substring_is_valid:
            if right < n:
                window_count[gene[right]] += 1
            right += 1
            
        else :
            min_len = min(min_len, right-left)
            window_count[gene[left]] -= 1
            left += 1   

    return min_len        
         
if __name__ == '__main__':
    gene = 'GAAATAAA'
    print(steadyGene(gene))
