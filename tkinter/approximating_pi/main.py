#from tkinter import *
import tkinter as tk
from time import sleep
from random import randrange
from math import pi

from tools import *

UPDATE_TIME = 0.2
SIZE = 300
R = SIZE/2
in_circle = 0
total = 0
best_diff = 100000000

def setup():
  global window, canvas
  
  window = tk.Tk()
  canvas = tk.Canvas(
    window,
    bg = 'white',
    height = SIZE,
    width = SIZE
  )
  canvas.pack()

  # There is not a create_circle function on tkinter
  create_circle(R, R, R, canvas)
  # Create the rectangle is no problem at all
  create_square(R, R, R, canvas)
  

def draw():
  global window, canvas, in_circle, total, best_diff

  for i in range(100):
    x = randrange(0, SIZE)
    y = randrange(0, SIZE)
  
    dist = (x-R)**2 + (y-R)**2
    
    if dist**(0.5) < R:
      create_circle(x, y, 2, canvas, fill="#F8CB2E")
      in_circle += 1
    else:
      create_circle(x, y, 2, canvas, fill="#001E6C")

    total += 1

    approximation_pi = 4 * in_circle/total
    if abs(pi - approximation_pi) < best_diff:
      print(approximation_pi)
      best_diff = abs(pi - approximation_pi)


setup()

while True:
  draw()
  window.update()
  #sleep(UPDATE_TIME)

window.mainloop()