import time

def counting__Sort(arr, exp1):
 
    n = len(arr)
 
    # The output array elements that will have sorted arr
    output = [0] * (n)
 
    # initialize count array as 0
    count = [0] * (10)
 
    # Store count of occurrences in count[]
    for i in range(0, n):
        index = arr[i] // exp1
        count[index % 10] += 1
 
    # Change count[i] so that count[i] now contains actual
    # position of this digit in output array
    for i in range(1, 10):
        count[i] += count[i - 1]
 
    # Build the output array
    i = n - 1
    while i >= 0:
        index = arr[i] // exp1
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1
 
    # Copying the output array to arr[],
    # so that arr now contains sorted numbers
    i = 0
    for i in range(0, len(arr)):
        arr[i] = output[i]
 
# Method to do Radix Sort
def radix_Sort(arr):
 
    # Find the maximum number to know number of digits
    max1 = max(arr)
 
    # Do counting sort for every digit. Note that instead
    # of passing digit number, exp is passed. exp is 10^i
    # where i is current digit number
    exp = 1
    while max1 / exp >= 1:
        counting__Sort(arr, exp)
        exp *= 10

# ----------------------------------------------------------------------------------------------------------- #

def countingSort(data, exp1, drawdata, speed): 

    n = len(data)

    output = [0] * (n) 
    count = [0] * (10)

    for i in range(0, n):
        index = (data[i] / exp1) 
        count[int(index % 10)] += 1

    for i in range(1, 10): 
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0: 
        index = (data[i] / exp1) 
        output[count[int(index % 10)] - 1] = data[i]
        count[int(index % 10)] -= 1
        i -= 1

    for i in range(0, len(data)): 
        data[i] = output[i]

    drawdata(data, ['black' for x in range(n)])
    time.sleep(speed + 0.3)

def radixSort(data, drawdata, speed): 
    max1 = max(data)

    exp = 1
    numss = len(str(max(data)))

    while numss != 0: 
        countingSort(data, exp, drawdata, speed)
        exp *= 10
        numss -= 1

    return data