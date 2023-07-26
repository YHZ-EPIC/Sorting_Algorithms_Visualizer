import time


def _heapify(arr, N, i):
    largest = i
    l = 2 * i + 1 
    r = 2 * i + 2  
 
    if l < N and arr[largest] < arr[l]:
        largest = l
 
    if r < N and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        _heapify(arr, N, largest)
 
def heapSort(arr):
    N = len(arr)
 
    # Build a maxheap.
    for i in range(N//2 - 1, -1, -1):
        _heapify(arr, N, i)
 
    # One by one extract elements
    for i in range(N-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        _heapify(arr, i, 0)

# ----------------------------------------------------------------------------------------------------------- #

colordata = []  

def heapify(data, n, i, drawData, timeTick):
    largest = i
    l = 2*i
    r = 2*i + 1

    if l < n and data[largest] < data[l]:
        largest = l

    if r < n and data[largest] < data[r]:
        largest = r
        
    if largest != i:
        data[i], data[largest] = data[largest], data[i]

        drawData(data, ['lightblue' if x == i or x == largest else colordata[x] for x in range(len(data))])
        time.sleep(timeTick)

        heapify(data, n, largest, drawData, timeTick)


def heap_sort(data, drawData, timeTick):
    global colordata

    colordata = ['#3b4249' for x in range(len(data))]

    n = len(data)
    for i in range(n//2 - 1, -1, -1):
        heapify(data, n, i, drawData, timeTick)
    
    for i in range(n-1, 0, -1):
        data[i], data[0] = data[0], data[i]

        drawData(data, ['lightyellow' if x == i or x == 0 else colordata[x] for x in range(len(data))])
        time.sleep(timeTick)
        # colordata[i] = 'green'

        heapify(data, i, 0, drawData, timeTick)

    drawData(data, ['green' for x in range(len(data))])