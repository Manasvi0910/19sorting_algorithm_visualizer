#Bitonic Sort Brick Sort Bubble Sort Cocktail Sort Comb Sort Counting Sort Cycle Sort Gnome Sort Heap Sort Insertion Sort Intro Sort Merge Sort Pancake Sort Pigeon hole sort Quick Sort Radix Sort Selection Sort Shell Sort Tim Sort
#bubble sort
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


#defining bubble sort
#loop through list
def bubble_sort(array):
    global max_pass
    for outer_pass in range(0, array_size - 1):
        #loop through list for next items
        for inner_pass in range(outer_pass+1, array_size):
            #if greater then swap
            if array[inner_pass] > array[outer_pass]:
                temp = array[inner_pass]
                array[inner_pass] = array[outer_pass]
                array[outer_pass] = temp

        load_item_coordinates(print_start_index, gap_between_lines, array, page_depth )
        max_pass +=1
    return array
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
            pygame.draw.line(screen, (r, g, b), (A_X[k], A_Y[k]), (B_X[k], B_Y[k]))

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

array = bubble_sort(array)
#need to define bubble sort above

print("After sorting")
print(array)

#Function call view sorting
view_sorting(array, page_width, page_depth, max_pass - 1)

