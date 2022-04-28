def create_circle(x, y, r, canvas, fill = ""):
  x0 = x - r
  y0 = y - r
  x1 = x + r
  y1 = y + r
  outline = "black"
  if fill:
    outline = fill
  return canvas.create_oval(x0, y0, x1, y1, fill=fill, outline = outline)


def create_square(x, y, size, canvas):
  x0 = x - size
  y0 = y - size
  x1 = x + size
  y1 = y + size
  return canvas.create_rectangle(x0, y0, x1, y1)