# Question: Given a sorted array of integers, return the index of the given key. Return -1 if not found.
'''
#Points to remeber for binary search
- Binary search is used to find index of an sorted array.
- Algorithm divides an array by half every step, if element is not found,
again divides array in half. so 0(logn)
- Sorted array
- Divide and Conquer

#Iterative solution complexity
Time complexity: logarithmic O(logn)
Mmeory complexity: constant(1)

#Algorithm
At every step, consider the array between low and high indices
Calculate the mid index.
If element at the mid index is the key, return mid.
If element at mid is greater than the key, then reduce the array size such that high becomes mid - 1. Index at low remains the same.
If element at mid is less than the key, then reduce the array size such that low becomes mid + 1. Index at high remains the same.
When low is greater than high, key doesn't exist. Return -1.
'''

# Can also be solved with recursion

#Binary Search iterative solution
def binary_search(a, key):
    #Set low and high values
    low = 0
    high = len(a) - 1
    
    while low <= high:
        # Find mid
        mid = low + ((high - low)//2)
        
        
        if a[mid] == key:
            return mid
        #if value of key is greater than value at mid
        #low is same and array is divided
        if a[mid] > key:
            high = mid - 1
        #high is same and array is divided  
        else:
            low = mid + 1
    #if low > high, no match    
    return -1
       
