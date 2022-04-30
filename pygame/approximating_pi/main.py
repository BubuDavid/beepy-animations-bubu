# Importamos cosas
from functions import setup, create_point ,update
from random import randrange

#Declaracion de variables
# CONSTANTES
SIZE = 2000
C = SIZE/2
R = SIZE/2
# VARIABLES
run = True
total = 0
in_circle = 0
x = 0
y = 0


window = setup(SIZE)
create_point(window, C, C, (0, 255, 0))

while run:

  for i in range(SIZE * 1000):
    #x = randrange(0, SIZE)
    #y = randrange(0, SIZE)
  
    dist = ((x - C)**2 + (y - C)**2)**(0.5)
  
    if dist < R:
      point_color = (255, 209, 36)
      in_circle += 1
    else:
      point_color = (0, 103, 120)
  
    create_point(window, x, y, point_color)
    total += 1
  
    approx_pi = 4 * in_circle / total
  
  
    x += 1
    if x == SIZE:
      x = 0
      y += 1
      if y == SIZE:
        y = 0
        run = False
  
  update(0)
  print(approx_pi)