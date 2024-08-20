import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator
from matplotlib.ticker import FuncFormatter
import numpy as np

formatter = FuncFormatter(lambda x, _: f"{x:.0f}")

def print_scheme_itog(D,d):
  centers_1_x=[]
  centers_1_y=[]
  centers_2_x=[]
  centers_2_y=[]

  fig, ax = plt.subplots(figsize=(10, 10))
  circle_0 = plt.Circle((0,0), D/2, edgecolor='#D44B46', facecolor='#1A1A1A')
  ax.add_patch(circle_0)

  d_itog=D

  n_1 = int((d_itog/2-d/2)// d)
  n_itog=(n_1)*2+1
  n_2 = int((d_itog/2-d/2)// (d*np.sin(np.radians(60))))
  n_itog_2=(n_2)*2+1

  for i in range(-n_1-1,n_1+2):
    for j in range(-n_2,n_2+1):
      if j%2==0:
        x=i*d
        y=j*d*np.sin(np.radians(60))
      else:
        x=i*d+d/2
        y=j*d*np.sin(np.radians(60))
      if np.sqrt(x ** 2 + y ** 2) + d/2 <= d_itog/2:
        if (abs(i))%3==0 and j%2==0:
            circle = plt.Circle((x,y), d/2, edgecolor='#D44B46', facecolor='#D44B46')
            ax.add_patch(circle)
            centers_1_x.append(x)
            centers_1_y.append(y)
        elif ((i))%3==1 and j%2==1 :
            circle = plt.Circle((x,y), d/2, edgecolor='#D44B46', facecolor='#D44B46')
            ax.add_patch(circle)
            centers_1_x.append(x)
            centers_1_y.append(y)
        else:
            circle = plt.Circle((x,y), d/2, edgecolor='white', facecolor='#1A1A1A')
            ax.add_patch(circle)
            centers_2_x.append(x)
            centers_2_y.append(y)

  ax.set_aspect('equal', adjustable='box')
  ax.set_xlim(-D / 2 - d, D / 2 + d)
  ax.set_ylim(-D / 2 - d, D / 2 + d)
  ax.tick_params(axis='x', colors='white', labelsize=14)
  ax.tick_params(axis='y', colors='white', labelsize=14)
  ax.grid(True, color='#D44B46', linestyle='--', linewidth=0.1)
  ax.grid(which='major', color='gray', linestyle='--', linewidth=0.1)
  ax.grid(which='minor', color='gray', linestyle='--', linewidth=0.1)
  ax.xaxis.set_minor_locator(AutoMinorLocator())
  ax.yaxis.set_minor_locator(AutoMinorLocator())
  ax.title.set_color('white')
  fig.patch.set_facecolor('#1A1A1A')
  ax.set_facecolor('#1A1A1A')
  fig.subplots_adjust(left=0.07, bottom=0.05, right=0.98, top=0.98)
  ax.xaxis.set_major_formatter(formatter)
  ax.yaxis.set_major_formatter(formatter)
  ax.tick_params(axis='x', colors='white', labelsize=15)
  ax.tick_params(axis='y', colors='white', labelsize=15)
  plt.show()
  return centers_1_x,centers_1_y,centers_2_x,centers_2_y

centers_1_x,centers_1_y,centers_2_x,centers_2_y=print_scheme_itog(300,18)
print("RED")
for x,y in zip(centers_1_x,centers_1_y):
  print(f'X={x}     Y={y}')
print(f'\nWHITE')
for x,y in zip(centers_2_x,centers_2_y):
  print(f'X={x}     Y={y}')

