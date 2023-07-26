import time

def insertionSort(arr):
 
    for i in range(1, len(arr)):
 
        key = arr[i]

        j = i-1
        while j >= 0 and key < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key

# ----------------------------------------------------------------------------------------------------------- #

def insertion(data, drawdata, speed):
    k = 0
    for i in range(len(data) - 1):
        if data[k] > data[k + 1]:
            data[k], data[k + 1] = data[k + 1], data[k]
            drawdata(data, ['red' if x == k or x == k + 1 else ['black'] for x in range(len(data))])
            time.sleep(speed)
            k += 1
            for j in range(len(data[:k])):
                k = 0
                if data[k] > data[k + 1]:
                    data[k], data[k + 1] = data[k + 1], data[k]
                    drawdata(data, ['red' if x == k or x == k + 1 else ['black'] for x in range(len(data))])
                    time.sleep(speed)
                    k += 1
                else:
                    k += 1
                    return insertion(data, drawdata, speed)
        else:
            k += 1

    drawdata(data, ['green' for x in range(len(data))])
    time.sleep(speed)