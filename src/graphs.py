import sys
import pygame
import numpy as np
from pygame.locals import *

# Code for integrating Matplotlib with pygame taken from
# https://subscription.packtpub.com/book/game_development/9781782162865/1/ch01lvl1sec13/using-matplotlib-with-pygame-simple

####
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.backends.backend_agg as agg

# Setup a matplotlib canvas to draw on
fig = plt.figure(figsize=[3, 3]) # 3 inches by 3 inches
ax = fig.add_subplot(111)
canvas = agg.FigureCanvasAgg(fig)

def plot(x, y):
   #ax.plot(x, y, color='black') # plot y vs x as lines
   ax.stackplot(x, y, y + 2, colors=['green','orange']) # stacked plot of vectors y and (y+2)
   canvas.draw()
   renderer = canvas.get_renderer()

   raw_data = renderer.tostring_rgb()
   size = canvas.get_width_height()
   return pygame.image.fromstring(raw_data, size, "RGB")
####

# set up the colors (RGB - red-green-blue values)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# set up pygame
pygame.init()

# set up the window. Upper left corner is (0,0)
xmax = 600
ymax = 400
windowSurface = pygame.display.set_mode((xmax, ymax))
pygame.display.set_caption('pyGame prufa')

FRAMES_PER_SECOND = 30
fpsClock = pygame.time.Clock()

x_coord = []
y_coord = []
t = 1

# run the main loop
while True:
    # Clear screen
    windowSurface.fill(WHITE)

    # Generate some (x,y) coordinates for plot
    if t <= 50:
        x_coord.append(t)
        y_coord.append(np.random.rand())
        t += 1

    ####
    # Draw graph via matplotlib
    surf = plot(np.array(x_coord), np.array(y_coord))
    windowSurface.blit(surf, (100, 100))
    ####

    # Draw components
    pygame.draw.circle(windowSurface, BLUE, (200, 300), 32)

    # Event handling
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FRAMES_PER_SECOND)