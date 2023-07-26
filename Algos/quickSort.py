# Extension Quick Sort Code
# importing time module
import time

def partition(array, low, high):
  
    # Choose the rightmost element as pivot
    pivot = array[high]
  
    # Pointer for greater element
    i = low - 1
  
    # Traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if array[j] <= pivot:
            # If element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1
  
            # Swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])
  
    # Swap the pivot element with 
    # e greater element specified by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])
  
    # Return the position from where partition is done
    return i + 1
  
# Function to perform quicksort
  
  
def quickSort(array, low, high):
    if low < high:
  
        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(array, low, high)
  
        # Recursive call on the left of pivot
        quick_sort(array, low, pi - 1)
  
        # Recursive call on the right of pivot
        quick_sort(array, pi + 1, high)


# ----------------------------------------------------------------------------------------------------------- #

# to implement divide and conquer
def partition(data, head, tail, drawData, timeTick):
	border = head
	pivot = data[tail]

	drawData(data, getColorArray(len(data), head,
								tail, border, border))
	time.sleep(timeTick)

	for j in range(head, tail):
		if data[j] < pivot:
			drawData(data, getColorArray(
				len(data), head, tail, border, j, True))
			time.sleep(timeTick)

			data[border], data[j] = data[j], data[border]
			border += 1

		drawData(data, getColorArray(len(data), head,
									tail, border, j))
		time.sleep(timeTick)

	# swapping pivot with border value
	drawData(data, getColorArray(len(data), head,
								tail, border, tail, True))
	time.sleep(timeTick)

	data[border], data[tail] = data[tail], data[border]

	return border


# head --> Starting index,
# tail --> Ending index
def quick_sort(data, head, tail,
			drawData, timeTick):
	if head < tail:
		partitionIdx = partition(data, head,
								tail, drawData,
								timeTick)

		# left partition
		quick_sort(data, head, partitionIdx-1,
				drawData, timeTick)

		# right partition
		quick_sort(data, partitionIdx+1,
				tail, drawData, timeTick)
				
# Function to apply colors to bars while sorting:
# Grey - Unsorted elements
# Blue - Pivot point element
# White - Sorted half/partition
# Red - Starting pointer
# Yellow - Ending pointer
# Green - after all elements are sorted

# assign color representation to elements

def getColorArray(dataLen, head, tail, border,
				currIdx, isSwaping=False):
	colorArray = []
	for i in range(dataLen):
		# base coloring
		if i >= head and i <= tail:
			colorArray.append('Grey')
		else:
			colorArray.append('White')

		if i == tail:
			colorArray[i] = 'Blue'
		elif i == border:
			colorArray[i] = 'Red'
		elif i == currIdx:
			colorArray[i] = 'Yellow'

		if isSwaping:
			if i == border or i == currIdx:
				colorArray[i] = 'Green'

	return colorArray