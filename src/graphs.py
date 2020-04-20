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
   h=H.Hopur()
   
   def plot(self, t, heilb, sykt, ein, batnad, latnir):
      plt.cla()
      plt.clf()
      plt.close()
      fig = plt.figure(figsize=[6, 1.6]) # 3 inches by 3 inches
      ax = fig.add_subplot(111)
      canvas = agg.FigureCanvasAgg(fig)
      #ax.stackplot(t , heilb, sykt, batnad, latnir ,colors=['blue', 'orange', 'purple', 'black'], baseline='zero')
      ax.stackplot(t , latnir, batnad, ein, sykt, heilb ,colors=['black', 'purple', 'red', 'orange', 'blue'], baseline='zero')
      canvas.draw()
      renderer = canvas.get_renderer()

      raw_data = renderer.tostring_rgb()
      size = canvas.get_width_height()
      return pygame.image.fromstring(raw_data, size, "RGB")
