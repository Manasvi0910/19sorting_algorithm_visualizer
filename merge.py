#merge sort
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
        clock.tick(100)
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
 
def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
 
    # create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)
 
    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[l + i]
 
    for j in range(0, n2):
        R[j] = arr[m + 1 + j]
 
    # Merge the temp arrays back into arr[l..r]
    i = 0     # Initial index of first subarray
    j = 0     # Initial index of second subarray
    k = l     # Initial index of merged subarray
 
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
 
    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
 
    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
 
# l is for left index and r is right index of the
# sub-array of arr to be sorted
 
 
def mergeSort(arr, l, r):
    global max_pass
    if l < r:
 
        # Same as (l+r)//2, but avoids overflow for
        # large l and h
        m = l+(r-l)//2
 
        # Sort first and second halves
        mergeSort(arr, l, m)
        #Function call loading item coordinates
        load_item_coordinates(print_start_index, gap_between_lines, array, page_depth)
        max_pass += 1
        mergeSort(arr, m+1, r)
        load_item_coordinates(print_start_index, gap_between_lines, array, page_depth)
        max_pass += 1
        merge(arr, l, m, r)
        load_item_coordinates(print_start_index, gap_between_lines, array, page_depth)
        max_pass += 1
 
 
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

#initialize pass no.
max_pass = 0

array = load_array(array)

#checking to print unsorted array 
print("Before Sorting")
print(array)

#Function call loading item coordinates
load_item_coordinates(print_start_index, gap_between_lines, array, page_depth)
 
mergeSort(array, 0, array_size-1)
print("After sorting")
print(array)

#Function call view sorting
view_sorting(array, page_width, page_depth, max_pass - 1)