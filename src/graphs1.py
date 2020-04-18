import sys
import pygame
import numpy as np
from pygame.locals import *
import Uppsetning as U
import Hopur as H
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.backends.backend_agg as agg

class graphs():
   
   def plot(self, t, heilb, sykt, batnad, latnir):
      fig = plt.figure(figsize=[6, 1]) # 3 inches by 3 inches
      ax = fig.add_subplot(111)
      canvas = agg.FigureCanvasAgg(fig)
      
      #ax.plot(x, y, color='black') # plot y vs x as lines
      ax.stackplot(t, heilb, sykt, batnad, latnir, colors=['blue', 'orange', 'purple', 'black']) # stacked plot of vectors y and (y+2)
      canvas.draw()
      renderer = canvas.get_renderer()

      raw_data = renderer.tostring_rgb()
      size = canvas.get_width_height()
      return pygame.image.fromstring(raw_data, size, "RGB")
   


