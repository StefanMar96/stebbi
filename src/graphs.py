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
   
   def plot(self, t, heilb, sykt, ein, batnad, latnir):#í þessu falli er grafið teiknað
      plt.cla()
      plt.clf()
      plt.close()
      fig = plt.figure(figsize=[6, 1.6]) #stærð plottsins (6*1.6 tommur)
      ax = fig.add_subplot(111) #höfum 1 subplot
      canvas = agg.FigureCanvasAgg(fig)
      #Hér eru gildin tekin og settir eru viðeigandi litir
      ax.stackplot(t , latnir, batnad, ein, sykt, heilb ,colors=['black', 'magenta', 'red', 'orange', 'blue'], baseline='zero')
      canvas.draw()
      renderer = canvas.get_renderer()

      raw_data = renderer.tostring_rgb()
      size = canvas.get_width_height()
      return pygame.image.fromstring(raw_data, size, "RGB")
