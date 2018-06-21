#Problem: Given array of integers, rotate the array by "N" rotations
'''
#Algorithm:
reverse the array
0 to N - 1 reverse
N to length(array) - 1 reverse

'''






def reverse_arr(arr, start, end):
    #if start index is less than end index of arr
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
        
def rotate_arr(arr, n):
    arr_len = len(arr)
    
    # To handle negative n 
    n = n % arr_len
    if n < 0:
        n = n + len(arr)
    #Partition array based on n rotations
    # input arr = [10, 20, 40, 60], n = 2
    # reverse entire arr: 60,40,20,10
    # reverse from 0 to n - 1 (2 - 1 = 1): 40, 60, 20, 10
    # reverse from n to len(arr) - 1 (2, 4-1 = 3) : 40, 60, 10, 20   
    reverse_arr(arr, 0, arr_len - 1)
    reverse_arr(arr, 0, n - 1)
    reverse_arr(arr, n, arr_len - 1)
    
arr = [10, 20, 40, 60]
rotate_arr(arr, -3)
print(arr)
#for i in range(0, len(arr)):
    #print(str(arr[i] )+ ",")
