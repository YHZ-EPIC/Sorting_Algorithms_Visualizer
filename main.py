# Project Title : Visualization of Sorting Algorithms

# Sec : 5A
# Group Members : 
#     Yasir Hussain - (19K-0223)

# Large Set of Random Unsorted 300 Values in input.txt were generated using this 
# online tool : https://www.random.org/integer-sets/

# small.txt = 10 Random Numbers
# medium.txt = 1000 Random Numbers
# high.txt = 10,000 Random Numbers

from tkinter import *
from tkinter import ttk
from tkinter import simpledialog
from colors import *
import random
import time

# Importing algorithms 
from Algos.bubbleSort import *
from Algos.mergeSort import *
from Algos.quickSort import *
from Algos.countingSort import *
from Algos.insertionSort import *
from Algos.radixSort import *
from Algos.selectionSort import *
from Algos.heapSort import *

# Main window 
window = Tk()
window.title("Sorting Algorithms Visualization")
window.maxsize(1920, 1080)
window.config(bg = WHITE)

algorithm_name = StringVar()
algo_list = ['Bubble Sort','Merge Sort','Heap Sort','Quick Sort','Radix Sort','Insertion Sort','Selection Sort','Counting Sort']

file_name = StringVar()
file_list = ['Small', 'Medium', 'High']

speed_name = StringVar()
speed_list = ['Fast', 'Medium', 'Slow']

data = []
limit = 300

# This function will draw randomly generated list data[] on the canvas as vertical bars
def drawData(data, colorArray):
    canvas.delete("all")
    canvas_width = 1500
    canvas_height = 400
    x_width = canvas_width / (len(data) + 1)
    offset = 4
    spacing = 2
    normalizedData = [i / max(data) for i in data]

    for i, height in enumerate(normalizedData):
        x0 = i * x_width + offset + spacing
        y0 = canvas_height - height * 390
        x1 = (i + 1) * x_width + offset
        y1 = canvas_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])

    window.update_idletasks()

# This function will generate array from txt files
def generate():
    
    global data
    data = []

    small = 'Algo_Project/small.txt'
    medium = 'Algo_Project/medium.txt'
    high = 'Algo_Project/high.txt'

    if(file_menu.get() == 'Small'):
        my_file = open(str(small), "r")
    elif(file_menu.get() == 'Medium'):
        my_file = open(str(medium), "r")
    elif(file_menu.get() == 'High'):    
        my_file = open(str(high), "r")
  
    line = my_file.read()

    arr = line.split(',')
    data = list(map(int, arr))
    
    print("\n\n ------ Unsorted Array ------ \n")
    print(data)
    my_file.close()

    drawData(data, [BLUE for x in range(len(data))])

# This function will generate array with random values based on our input
def generate_rand():
    global data
    data = []

    USER_INP = simpledialog.askstring(title="User Input", prompt="Enter the size of Array: ")

    val = int(USER_INP)
    data = [random.randint(1,val) for _ in range(val)]

    ## Filling the data into random.txt file
    with open('Algo_Project/random.txt', 'w+') as f:
        f.write(str(data))

    print("\n\n ------ Unsorted Array ------ \n")
    print(data) 

    if(val <= limit):
        drawData(data, [BLUE for x in range(len(data))])

# This function will open a new Window displaying the sorted array
def new_window():
    global data

    master = Tk()
    master.title("For Large Input Size")
    master.maxsize(1280, 720)
    master.config(bg = WHITE)

    l = Label(master, text = "Printing the Sorted Array", font=("Courier", 14))
    text_widget = Text(master, height=350, width=700, bg=BLACK, fg=YELLOW, borderwidth= 33, relief=SOLID, wrap= WORD)

    l.pack()
    text_widget.pack()

    text_widget.insert(END, data)

# This function will set sorting speed
def set_speed():
    if speed_menu.get() == 'Slow':
        return 0.3
    elif speed_menu.get() == 'Medium':
        return 0.1
    else:
        return 0.001

# This funciton will trigger a selected algorithm and start sorting
def sort():
    global data
    timeTick = set_speed()

    if algo_menu.get() == 'Bubble Sort':
        start = time.time()
        if(len(data) > limit):
            bubbleSort(data)
        else:    
            bubble_sort(data, drawData, timeTick)
        end = time.time()

    elif algo_menu.get() == 'Merge Sort':
        start = time.time()
        if(len(data) > limit):
            mergeSort(data)
        else: 
            merge_sort(data, 0, len(data)-1, drawData, timeTick)
        end = time.time()
        
    elif algo_menu.get() == 'Quick Sort':
        start = time.time()
        if(len(data) > limit):
            quickSort(data, 0, len(data)-1)
        else: 
            quick_sort(data, 0, len(data)-1, drawData, timeTick)    
            drawData(data, ['Green' for x in range(len(data))])
        end = time.time()

    elif algo_menu.get() == 'Counting Sort':
        start = time.time()
        if(len(data) > limit):
            countSort(data)
        else: 
            counting(data, drawData, timeTick)    
        end = time.time()

    elif algo_menu.get() == 'Insertion Sort':
        start = time.time()
        if(len(data) > limit):
            insertionSort(data)
        else: 
            insertion(data, drawData, timeTick)
        end = time.time()

    elif algo_menu.get() == 'Radix Sort':
        start = time.time()
        if(len(data) > limit):
            radix_Sort(data)
        else: 
            radixSort(data, drawData, timeTick) 
            drawData(data, ['Green' for x in range(len(data))])   
        end = time.time()

    elif algo_menu.get() == 'Selection Sort':
        start = time.time()
        if(len(data) > limit):
            selectionSort(data)
        else: 
            selection(data, drawData, timeTick)     
        end = time.time()
    elif algo_menu.get() == 'Heap Sort':
        start = time.time()
        if(len(data) > limit):
            heapSort(data)
        else: 
            heap_sort(data, drawData, timeTick) 
        end = time.time()
    
    new_window()
    print("\n ------ Sorted Array ------ \n")
    print(data)
    print(f"\n\n ---> Runtime of the program is {end - start} seconds \n\n")

### User interface here ###
UI_frame = Frame(window, width= 900, height=300, bg=WHITE)
UI_frame.grid(row=0, column=0, padx=10, pady=5)

# dropdown to select Sorting algorithm 
l1 = Label(UI_frame, text="Algorithm: ", bg=WHITE)
l1.grid(row=0, column=0, padx=10, pady=5, sticky=W)
algo_menu = ttk.Combobox(UI_frame, textvariable=algorithm_name, values=algo_list)
algo_menu.grid(row=0, column=1, padx=5, pady=5)
algo_menu.current(0)

# dropdown to select Input Files
l = Label(UI_frame, text="Files: ", bg=WHITE)
l.grid(row=0, column=2, padx=5, pady=5, sticky=W)
file_menu = ttk.Combobox(UI_frame, textvariable=file_name, values=file_list)
file_menu.grid(row=0, column=3, padx=5, pady=5)
file_menu.current(0)

# dropdown to select Sorting Speed 
l2 = Label(UI_frame, text="Sorting Speed: ", bg=WHITE)
l2.grid(row=1, column=0, padx=10, pady=5, sticky=W)
speed_menu = ttk.Combobox(UI_frame, textvariable=speed_name, values=speed_list)
speed_menu.grid(row=1, column=1, padx=5, pady=5)
speed_menu.current(0)

# Sort Button 
b1 = Button(UI_frame, text="    Sort    ", command=sort, bg=LIGHT_GRAY)
b1.grid(row=2, column=1, padx=5, pady=5)

# button for Generating Array from File
b3 = Button(UI_frame, text="Generate Array From File", command=generate, bg=LIGHT_GRAY)
b3.grid(row=2, column=0, padx=5, pady=5)

# button for Generating Random Array
b4 = Button(UI_frame, text="Generate Random Array", command=generate_rand, bg=LIGHT_GRAY)
b4.grid(row=2, column=2, padx=5, pady=5)

# Canvas to Show our Visualization  
canvas = Canvas(window, width=1500, height=416, bg=WHITE)
canvas.grid(row=1, column=0, padx=10, pady=5)

window.mainloop()