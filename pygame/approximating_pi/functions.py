import pygame

def setup(SIZE):
  # Iniciamos el juego
  pygame.init()
  # Creamos componentes de pygame
  window = pygame.display.set_mode((SIZE, SIZE))
  pygame.display.set_caption("Approximating PI")
  window.fill((255, 255, 255))
  # Dibujamos lo necesario para empezar
  pygame.draw.rect(
    window,
    (0, 110, 127),
    (0, 0, SIZE, SIZE),
    2
  )

  pygame.draw.circle(
    window,
    (248, 203, 46),
    (SIZE/2, SIZE/2),
    SIZE/2,
    2
  )
  
  pygame.display.update()

  return window



def create_point(window, x, y, color):
  pygame.draw.circle(
    window,
    color,
    (x, y),
    4
  )

def update(time):
  pygame.time.delay(time)
  pygame.display.update()