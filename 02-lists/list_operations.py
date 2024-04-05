"""
You are given an array arr(0-based indexing). The size of the array is given by n.
You need to get the element at index i and return it.
 If no element exists at i then return -1.
Input:
n = 6
arr[] = {1 2 3 4 5 6}
index = 0
Output: 1
Explanation: The array is {1 2 3 4 5 6}.
The index given is 0. so element at 0th
index is 1.

"""


def getByIndex(arr, n, idx):
    # return required ans
    if idx in range(0, len(arr)):
        return arr[idx]
    if idx > (len(arr) + 1) or idx < 0:
        return -1


# User function Template for python3

# You only need to insert the given element at
# the end, i.e., at index sizeOfArray - 1. You may
# assume that the array already has sizeOfArray - 1
# elements.
def insertAtEnd(arr, sizeOfArray, element):
    arr.append(element)
    return


'''You need to insert the given element at the given index. 
    After inserting the elements at index, elements
    from index onward should be shifted one position ahead
     You may assume that the array already has sizeOfArray - 1
    elements.'''


def insertAtIndex(self, arr, sizeOfArray, index, element):
    # Your code here
    arr.insert(index, element)
    return

def getByIndex(arr,n,idx):
    # return required ans
    if idx > len(arr):
        return -1
    return arr.pop(idx)
