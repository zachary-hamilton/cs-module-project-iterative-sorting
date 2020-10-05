# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        current_index_value = arr[cur_index] # the value of the current index
        smallest_index = cur_index # this was in the starter code and not sure what for
        
        # getting the value and corresponding index of the smallest value
        small_value = min(arr[cur_index:]) # its value
        small_index = arr.index(small_value) # its index
        
        # swapping the values
        arr[cur_index] = small_value
        arr[small_index] = current_index_value


        

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    for i in range(0, len(arr) - 1): # loop through each element
        for j in range(0, len(arr) - 1): # for each element loop through array
            if arr[j] > arr[j + 1]: # if current element is bigger than the next element swap them
                small = arr[j + 1]
                big = arr[j]
                arr[j] = small
                arr[j + 1] = big


    return arr

'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # Your code here


    return arr
