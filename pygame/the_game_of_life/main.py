# Import things
#from functions import setup, update, create_random_matrix
from functions import *

# CONSTANTS
SIZE = 600
CELL_SIZE = 10
N_CELLS = SIZE//CELL_SIZE

# VARIABLES
run = True
matrix = create_random_matrix(N_CELLS)

# Setup
window = setup(SIZE)

# Main Loop
while run:
  draw_grid(window, matrix, CELL_SIZE)
  matrix = update_matrix(matrix)

  # print("---------update-----------")
  update(window, 0)


print("DONE!")