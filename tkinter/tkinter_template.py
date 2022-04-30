import tkinter as tk
from time import sleep

UPDATE_TIME = 0.8
WIDTH = 600
HEIGHT = 600

def setup():
  global window, canvas
  
  window = tk.Tk()
  canvas = tk.Canvas(
    window,
    bg = 'white',
    height = HEIGHT,
    width = WIDTH
  )
  canvas.pack()

def draw():
  global window
  



setup()

while True:
  draw()
  window.update()
  sleep(UPDATE_TIME)

window.mainloop()