import time

def selectionSort(array):
    size = len(array)
    for step in range(size):
        min_idx = step

        for i in range(step + 1, size):
         
            # to sort in descending order, change > to < in this line
            # select the minimum element in each loop
            if array[i] < array[min_idx]:
                min_idx = i
         
        # put min at the correct position
        (array[step], array[min_idx]) = (array[min_idx], array[step])

# ----------------------------------------------------------------------------------------------------------- #

def selection(data, drawdata, speed):
    for i in range(len(data)):
        minV = i

        for j in range(i, len(data)):
            if data[j] < data[minV]:
                minV = j
                drawdata(data, ['red' if  x == minV else ['black'] for x in range(len(data))])
                time.sleep(speed)

        data[minV], data[i] = data[i], data[minV] 
        
        drawdata(data, ['yellow' if  x == data[i] else ['black'] for x in range(len(data))])
        time.sleep(speed)

    drawdata(data, ['green' for x in range(len(data))])
    return data