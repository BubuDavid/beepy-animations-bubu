import pygame
import numpy as np
import random

def setup(size):
  # Init
  pygame.init()
  # Display options
  window = pygame.display.set_mode((size, size))
  pygame.display.set_caption("The Game Of Life")  
  window.fill((161, 227, 216))

  return window



def update(window, time):
  pygame.time.delay(time)
  #input("Continue......")
  pygame.display.update()


def create_random_matrix(n_cells):

  matrix = np.zeros((n_cells, n_cells))
  
  for row in range(n_cells):
    for column in range(n_cells):
      matrix[row][column] = random.randint(0, 1)

  return matrix

def draw_rectangle(window, x, y, size, color):
  pygame.draw.rect(
    window,
    color,
    (x, y, size, size),
  )

  pygame.draw.rect(
    window,
    (0, 85, 85),
    (x, y, size, size),
    1
  )

def draw_grid(window, matrix, cell_size):
  n_cells = len(matrix)
  cell_color1 = (0, 85, 85)
  cell_color2 = (161, 227, 216)
  
  for row in range(n_cells):
    for column in range(n_cells):
      x = column * cell_size
      y = row * cell_size

      if matrix[row][column]:
        color = cell_color1
      else:
        color = cell_color2
        
      draw_rectangle(window, x, y, cell_size, color)


def check_neighbors(matrix, row, column):
  n_alive_cells = 0
  n_cells = len(matrix)
  #print("---------checking neighbor--------------------")
  
  for i in range(-1, 2):
    for j in range(-1, 2):
      neighbor_row = row + i
      neighbor_col = column + j
      if neighbor_row >= 0 and neighbor_row < n_cells and neighbor_col >= 0 and neighbor_col < n_cells:
        if matrix[neighbor_row][neighbor_col] and (i or j):
          n_alive_cells += 1
          #print(neighbor_row, neighbor_col, "->", n_alive_cells)

  #print(n_alive_cells)
  if matrix[row][column]:
    return n_alive_cells in [2,3]
  else:
    return n_alive_cells == 3
    


def update_matrix(matrix):
  n_cells = len(matrix)
  new_matrix = np.zeros((n_cells, n_cells))
  
  for row in range(n_cells):
    for column in range(n_cells):
      new_cell = check_neighbors(matrix, row, column)
      #print(int(new_cell))
      new_matrix[row][column] = int(new_cell)

  #print(new_matrix)
  return new_matrix