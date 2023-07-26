import time

def countSort(arr):
 
    # The output character array that will have sorted arr
    output = [0 for i in range(len(arr))]
 
    # Create a count array to store count of individual
    # characters and initialize count array as 0
    count = [0 for i in range(256)]
 
    # For storing the resulting answer since the
    # string is immutable
    ans = ["" for _ in arr]
 
    # Store count of each character
    for i in arr:
        count[ord(i)] += 1
 
    # Change count[i] so that count[i] now contains actual
    # position of this character in output array
    for i in range(256):
        count[i] += count[i-1]
 
    # Build the output character array
    for i in range(len(arr)):
        output[count[ord(arr[i])]-1] = arr[i]
        count[ord(arr[i])] -= 1
 
    # Copy the output array to arr, so that arr now
    # contains sorted characters
    for i in range(len(arr)):
        ans[i] = output[i]
    return ans

# ----------------------------------------------------------------------------------------------------------- #

def counting(data, drawdata, speed):
    mval = 0
    for i in range(len(data)):
        drawdata(data, ['red' if x == i else ['black'] for x in range(len(data))])
        time.sleep(speed)
        if data[i] > mval:
            mval = data[i]

    buckets = [0 for i in range(mval + 1)]

    for i in data:
        buckets[i] += 1

    i = 0
    for j in range(mval + 1):
        for _ in range(buckets[j]):
            data[i] = j
            i += 1

    drawdata(data, ['green' for x in range(len(data))])
    
    time.sleep(speed)
    return data