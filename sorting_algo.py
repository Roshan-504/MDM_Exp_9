# Bubble sort
# worst time complexity O(N*2)
# best case O(N)
# space complexity is O(1)
# stable algorithm
def bubble_sort(arr):
    l=len(arr)
    for i in range(l-1):
        flag = 0 
        for j in range(l-1-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                flag = 1
        if flag == 0:
            break
    return arr
a=[23,12,34,11,100,56,78]
# bubble_sort(a)



# selection sort
# time complexity O(N*2)
# Best complexity: n^2
# space complexity O(1)
####### selection sort takes less time to sort than bubble
#  if array is not sorted already
# not addaptive
# not stable
# less swapping take less time
def selection_sort(arr):
    l=len(arr)
    for i in range(l-1):
        min=i
        for j in range(i+1,l):
            if arr[j]<arr[min]:
                min=j
        arr[i],arr[min]=arr[min],arr[i]
    return arr
a1=[23,12,34,11,100,56,78]
# selection_sort(a1)



# Merge sort
# python default sorting algo called timsort is made of merge sort
# time complexity O(Nlog(N))
# Best complexity: n*log(n)
# space complexity O(N) ----> recursion
# not addaptive
# stable
def merge_sort(myList):
    if len(myList) > 1:
        mid = len(myList) // 2
        left = myList[:mid]
        right = myList[mid:]

        merge_sort(left)
        merge_sort(right)

        i = 0
        j = 0
        k = 0
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                myList[k] = left[i]
                i += 1
            else:
                myList[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            myList[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            myList[k]=right[j]
            j += 1
            k += 1

    return myList

arr1=[2,8,3,4,9,6,7,1,5]
print(merge_sort(arr1))





# Quick sort
# Stable: No
# Best complexity: n*log(n)
# Average complexity: n*log(n)





