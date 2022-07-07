#Python program for implementation of heap Sort
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
# To heapify subtree rooted at index i.
# n is size of heap
def heapify(arr, n, i):   
 largest = i # Initialize largest as root
 l = 2 * i + 1  # left = 2*i + 1
 r = 2 * i + 2  # right = 2*i + 2
 
 # See if left child of root exists and is
 # greater than root
 if l < n and arr[i] < arr[l]:
  largest = l
 
 # See if right child of root exists and is
 # greater than root
 if r < n and arr[largest] < arr[r]:
  largest = r
 
 # Change root, if needed
 if largest != i:
  arr[i],arr[largest] = arr[largest],arr[i] # swap
 
  # Heapify the root.
  heapify(arr, n, largest)
 
# The main function to sort an array of given size
def heapSort(arr):
 global max_pass   
 n = len(arr)
 
 # Build a maxheap.
 # Since last parent will be at ((n//2)-1) we can start at that location.
 for i in range(n // 2 - 1, -1, -1):
  heapify(arr, n, i)
 
 # One by one extract elements
 for i in range(n-1, 0, -1):
  load_item_coordinates(print_start_index, gap_between_lines, array, page_depth)
  max_pass += 1  
  arr[i], arr[0] = arr[0], arr[i] # swap
  heapify(arr, i, 0)
 
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
heapSort(array)
print("After sorting")
print(array)

#Function call view sorting
view_sorting(array, page_width, page_depth, max_pass - 1)