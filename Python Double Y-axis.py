import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import openpyxl
from pathlib import Path
import gc

data = pd.read_csv('FHr.csv', usecols = ['STATION','Electrical Conductivity', 'Total Dissolved Solids' , 'Chloride', 'Sulphate','Sodium', 'Bicarbonate', 'Carbonate', 'Fluoride', 'Bromide', 'Ion Balance', 'DATE', 'Water', 'Ground Level'])
print(data.head())
print(data)



grouped = data.groupby('STATION')



### Bicarbonate



def Bicarbonate():
   grouped = data.groupby('STATION')
   for name,group in grouped:
      print (name)
      print (group)

      fig, ax = plt.subplots() # Create the figure and axes object

      # Plot the first x and y axes:
      group.plot(x = 'DATE', y = 'Bicarbonate', ax = ax, title = name) 
      # Plot the second x and y axes. By secondary_y = True a second y-axis is requested:
      # (see https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.html for details)
      group.plot(x = 'DATE', y = 'Water', ax = ax, secondary_y = True)
      group.plot(x = 'DATE', y = 'Ground Level', ax= ax, secondary_y = True)
      plt.savefig(name + ' Bicarbonate', dpi=500, bbox_inches='tight')
      plt.close()


def Electrical_Conductivity():
   for name,group in grouped:
      print (name)
      print (group)

      fig, ax = plt.subplots() # Create the figure and axes object

      # Plot the first x and y axes:
      group.plot(x = 'DATE', y = 'Electrical Conductivity', ax = ax, title = name) 
      # Plot the second x and y axes. By secondary_y = True a second y-axis is requested:
      # (see https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.html for details)
      group.plot(x = 'DATE', y = 'Water', ax = ax, secondary_y = True)
      group.plot(x = 'DATE', y = 'Ground Level', ax= ax, secondary_y = True)
      plt.savefig(name + ' Electrical Conductivity', dpi=500, bbox_inches='tight')
      plt.close()


def Chloride():
   for name,group in grouped:
      print (name)
      print (group)

      fig, ax = plt.subplots() # Create the figure and axes object

      # Plot the first x and y axes:
      group.plot(x = 'DATE', y = 'Chloride', ax = ax, title = name) 
      # Plot the second x and y axes. By secondary_y = True a second y-axis is requested:
      # (see https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.html for details)
      group.plot(x = 'DATE', y = 'Water', ax = ax, secondary_y = True)
      group.plot(x = 'DATE', y = 'Ground Level', ax= ax, secondary_y = True)
      plt.savefig(name + ' Chloride', dpi=500, bbox_inches='tight')
      plt.close()


def Sulphate():
   for name,group in grouped:
      print (name)
      print (group)

      fig, ax = plt.subplots() # Create the figure and axes object

      # Plot the first x and y axes:
      group.plot(x = 'DATE', y = 'Sulphate', ax = ax, title = name) 
      # Plot the second x and y axes. By secondary_y = True a second y-axis is requested:
      # (see https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.html for details)
      group.plot(x = 'DATE', y = 'Water', ax = ax, secondary_y = True)
      group.plot(x = 'DATE', y = 'Ground Level', ax= ax, secondary_y = True)
      plt.savefig(name + ' Sulphate', dpi=500, bbox_inches='tight')
      plt.close()


def Sodium():
   for name,group in grouped:
      print (name)
      print (group)

      fig, ax = plt.subplots() # Create the figure and axes object

      # Plot the first x and y axes:
      group.plot(x = 'DATE', y = 'Sodium', ax = ax, title = name) 
      # Plot the second x and y axes. By secondary_y = True a second y-axis is requested:
      # (see https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.html for details)
      group.plot(x = 'DATE', y = 'Water', ax = ax, secondary_y = True)
      group.plot(x = 'DATE', y = 'Ground Level', ax= ax, secondary_y = True)
      plt.savefig(name + ' Sodium', dpi=500, bbox_inches='tight')
      plt.close()

def Carbonate():
   for name,group in grouped:
      print (name)
      print (group)

      fig, ax = plt.subplots() # Create the figure and axes object

      # Plot the first x and y axes:
      group.plot(x = 'DATE', y = 'Carbonate', ax = ax, title = name) 
      # Plot the second x and y axes. By secondary_y = True a second y-axis is requested:
      # (see https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.html for details)
      group.plot(x = 'DATE', y = 'Water', ax = ax, secondary_y = True)
      group.plot(x = 'DATE', y = 'Ground Level', ax= ax, secondary_y = True)
      plt.savefig(name + ' Carbonate', dpi=500, bbox_inches='tight')
      plt.close()

def Fluoride():
   for name,group in grouped:
      print (name)
      print (group)

      fig, ax = plt.subplots() # Create the figure and axes object

      # Plot the first x and y axes:
      group.plot(x = 'DATE', y = 'Fluoride', ax = ax, title = name) 
      # Plot the second x and y axes. By secondary_y = True a second y-axis is requested:
      # (see https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.html for details)
      group.plot(x = 'DATE', y = 'Water', ax = ax, secondary_y = True)
      group.plot(x = 'DATE', y = 'Ground Level', ax= ax, secondary_y = True)
      plt.savefig(name + ' Fluoride', dpi=500, bbox_inches='tight')
      plt.close()

def Bromide():
   for name,group in grouped:
      print (name)
      print (group)

      fig, ax = plt.subplots() # Create the figure and axes object

      # Plot the first x and y axes:
      group.plot(x = 'DATE', y = 'Bromide', ax = ax, title = name) 
      # Plot the second x and y axes. By secondary_y = True a second y-axis is requested:
      # (see https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.html for details)
      group.plot(x = 'DATE', y = 'Water', ax = ax, secondary_y = True)
      group.plot(x = 'DATE', y = 'Ground Level', ax= ax, secondary_y = True)
      plt.savefig(name + ' Bromide', dpi=500, bbox_inches='tight')
      plt.close()

def Ion_Balance():
   for name,group in grouped:
      print (name)
      print (group)

      fig, ax = plt.subplots() # Create the figure and axes object

      # Plot the first x and y axes:
      group.plot(x = 'DATE', y = 'Ion Balance', ax = ax, title = name) 
      # Plot the second x and y axes. By secondary_y = True a second y-axis is requested:
      # (see https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.html for details)
      group.plot(x = 'DATE', y = 'Water', ax = ax, secondary_y = True)
      group.plot(x = 'DATE', y = 'Ground Level', ax= ax, secondary_y = True)
      plt.savefig(name + ' Ion Balance', dpi=500, bbox_inches='tight')
      plt.close()



Bicarbonate()
gc.collect()
Electrical_Conductivity()
Chloride()
gc.collect()
Sulphate()
Sodium()
gc.collect()
Carbonate()
Fluoride()
gc.collect()
Bromide()
gc.collect()
Ion_Balance()

      
