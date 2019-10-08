import sys
import os

# determine whether or not each input is nummeric
def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

# recursive permute function which uses N to track how many characters remaining to permute
def permute(N, L):
    # enpty array to store results
    result = []
    if N == 1:
        # if N = 1, L is our base case so return L instead of result.
        return L.copy()

    # loop over values in L
    for i, l in enumerate(L):

        # get all permutations from lower levels
        subperm = permute(N-1, L)

        #loop over values in subperm
        for j in range(0,len(subperm)):

            # append the current letter to the beginning of the subperm
            subperm[j] = l + subperm[j]

        #add the subperm list to the result list
        result += subperm

    # return overall result
    return result
