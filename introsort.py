def load_array(array):
    s=0
    while s < array_size:
        r = random.randint(1, 600)
        if r not in array:
            array.append(r)
            s += 1
    return array

def load_item_coordinates(print_start_index, gap_between_lines, array, page_depth):
    array_size = len(array)
    for a in range(print_start_index, array_size):
        #LINE REPRESENTATION
        A_X.append(gap_between_lines)
        A_Y.append(page_depth)
        B_X.append(gap_between_lines)
        B_Y.append(page_depth - array[a])

        #move to next point
        gap_between_lines += gap_between_lines_incr

#function definition view sorting                
def view_sorting(array, page_width, page_depth, max_pass):
    #initialize module pygame
    pygame.init()
    #design game canvas(screen)
    screen = pygame.display.set_mode((page_width, page_depth))

    array_size = len(array)
    run_cnt = 0 
    print_index_start = 0
    print_index_end = array_size
    pass_print_cnt = 0
    r, g, b = 0, 255, 255

    clock = pygame.time.Clock()



    #Infinite game loop
    running = True

    #game loop quit condition
    while running:
        clock.tick(50)
        screen.fill((0,0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False    
        
        #draw a sample line
        #pygame.draw.line(screen, (0, 255, 0), (400, 0), (400, 600))
        #drawing multiple lines representing list
        for k in range(print_index_start, print_index_end):
            pygame.draw.line(screen, (r,g,b), (A_X[k], A_Y[k]), (B_X[k], B_Y[k]))

        if pass_print_cnt <= max_pass:
            print_index_start = print_index_end
            print_index_end = print_index_end + array_size
        else:
            k = print_index_start
            r, g, b = 0, 255, 0
        
        pass_print_cnt += 1
        pygame.display.flip()

    #update game window to view
    pygame.display.update()
def introsort(alist):
    maxdepth = (len(alist).bit_length() - 1)*2
    introsort_helper(alist, 0, len(alist), maxdepth)
 
def introsort_helper(alist, start, end, maxdepth):
    if end - start <= 1:
        return
    elif maxdepth == 0:
        heapsort(alist, start, end)
    else:
        p = partition(alist, start, end)
        introsort_helper(alist, start, p + 1, maxdepth - 1)
        introsort_helper(alist, p + 1, end, maxdepth - 1)
 
def partition(alist, start, end):
    pivot = alist[start]
    i = start - 1
    j = end
 
    while True:
        i = i + 1
        while alist[i] < pivot:
            i = i + 1
        j = j - 1
        while alist[j] > pivot:
            j = j - 1
 
        if i >= j:
            return j
 
        swap(alist, i, j)
 
def swap(alist, i, j):
    alist[i], alist[j] = alist[j], alist[i]
 
def heapsort(alist, start, end):
    build_max_heap(alist, start, end)
    for i in range(end - 1, start, -1):
        swap(alist, start, i)
        max_heapify(alist, index=0, start=start, end=i)
 
def build_max_heap(alist, start, end):
    def parent(i):
        return (i - 1)//2
    length = end - start
    index = parent(length - 1)
    while index >= 0:
        max_heapify(alist, index, start, end)
        index = index - 1
 
def max_heapify(alist, index, start, end):
    global max_pass
    def left(i):
        return 2*i + 1
    def right(i):
        return 2*i + 2
 
    size = end - start
    l = left(index)
    r = right(index)
    if (l < size and alist[start + l] > alist[start + index]):
        load_item_coordinates(print_start_index, gap_between_lines, array, page_depth)
        max_pass += 1
        largest = l
    else:
        load_item_coordinates(print_start_index, gap_between_lines, array, page_depth)
        max_pass += 1
        largest = index
    if (r < size and alist[start + r] > alist[start + largest]):
        load_item_coordinates(print_start_index, gap_between_lines, array, page_depth)
        max_pass += 1
        largest = r
    if largest != index:
        load_item_coordinates(print_start_index, gap_between_lines, array, page_depth)
        max_pass += 1
        swap(alist, start + largest, start + index)
        max_heapify(alist, largest, start, end)
 
# Driver code to test above
#driver code
#non repeating integers

import random
import pygame
import pyautogui


#designing a window 800X600
#page_width = 800
#page_depth = 600
page_width, page_depth = pyautogui.size()
page_width = int(page_width * .95)
page_depth = int(page_depth * .95)
gap_between_lines = 0
gap_between_lines_incr = 5
print_start_index = 0
array_size = int(page_width / gap_between_lines_incr)
array = []
#list of points representing list items
A_X, A_Y, B_X, B_Y = [], [], [], []
up = 1
#initialize pass no.
max_pass = 0

array = load_array(array)

#checking to print unsorted array 
print("Before Sorting")
print(array)

#Function call loading item coordinates
load_item_coordinates(print_start_index, gap_between_lines, array, page_depth)
introsort(array)
print("After sorting")
print(array)

#Function call view sorting
view_sorting(array, page_width, page_depth, max_pass - 1)