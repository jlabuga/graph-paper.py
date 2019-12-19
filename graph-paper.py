#!/usr/bin/python3
# -*- coding: utf-8 -*-
##############################
# Graph paper, linear or log scale
# using python3 and matplotlib
# J. Labbé, december 2019
##############################

# Import everything from matplotlib (numpy is accessible via 'np' alias)
from pylab import *

### Parameters

showfig = False

# Number of decades for log scale
# set to zero for linear scale
xdecades = 4
ydecades = 0

# Output filename
save = True
filename="Papier"
extension=".pdf"

### Paper geometry

paperwidth  = 29.7 # cm
paperheight = 21.0 # cm
figwidth    = 25.0 # cm
figheight   = 18.0 # cm
leftmargin  =  (paperwidth - figwidth)/2 # cm
topmargin   =  (paperheight - figheight)/2 # cm

cm2inch = 1/2.54 # inch per cm
fig = figure(figsize=(paperwidth*cm2inch,paperheight*cm2inch))
ax = fig.add_subplot(111)

xmin = 0
xmax = figwidth
ymin = 0
ymax = figheight

### Axes formatting function

def format_lin_axis(axis):
    axis.set_major_locator(matplotlib.ticker.MultipleLocator(1))
    axis.set_minor_locator(matplotlib.ticker.MultipleLocator(0.1))
    axis.set_major_formatter(NullFormatter())
    axis.set_minor_formatter(NullFormatter())

def format_log_axis(axis):
    axis.set_major_locator(matplotlib.ticker.LogLocator(subs=arange(1,10)))
    minorsubs = []
    minorsubs.extend(arange(1.,6.,0.1))
    minorsubs.extend(arange(6.,10.,0.2))
    axis.set_minor_locator(matplotlib.ticker.LogLocator(subs=minorsubs))
    axis.set_major_formatter(FuncFormatter(lambda value, index: index%9+1 if index%9+1 > 1 else '')) # show log scale position
    axis.set_minor_formatter(NullFormatter())
    axis.set_tick_params(labelsize=6,pad=0)

### Set lin or log scale

# x axis
if (xdecades > 0):
    xmin = 10
    xmax = xmin*10**xdecades
    xscale('log')
    filename += "-"+str(xdecades)+"log"
    format_log_axis(ax.xaxis)
else:
    filename += "-lin"
    format_lin_axis(ax.xaxis)

# y axis
if (ydecades > 0):
    ymin = 10
    ymax = ymin*10**ydecades
    yscale('log')
    filename += "-"+str(ydecades)+"log"
    format_log_axis(ax.yaxis)
else:
    filename += "-lin"
    format_lin_axis(ax.yaxis)

### Final configuration

# x and y scales
xlim(xmin,xmax)
ylim(ymin,ymax)

# no ticks
ax.xaxis.set_ticks_position('none')
ax.yaxis.set_ticks_position('none')

# grid
ax.set_axisbelow(True) # grille sous le tracé
grid(True, which='minor', axis='both',linestyle='-',linewidth=0.25,color="black",alpha=0.7)
grid(True, which='major', axis='both',linestyle='-',linewidth=0.5,color="black")

# Margins
# from https://stackoverflow.com/questions/29400116/using-matplotlib-how-can-i-print-something-actual-size
rightmargin = paperwidth - figwidth - leftmargin
bottommargin = paperheight - figheight - topmargin
fig.subplots_adjust(left   = leftmargin / paperwidth,
                    bottom = bottommargin / paperheight,
                    right  = 1. - rightmargin / paperwidth,
                    top    = 1. - topmargin   / paperheight,
                    )

### Show and save

if save:
    savefig(filename+extension,dpi=600)
    print("File "+filename+extension+" created.")

if showfig:
    show()
