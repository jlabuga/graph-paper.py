#!/usr/bin/python3
# -*- coding: utf-8 -*-
##############################
# Graph paper, linear or log scale
# using python3 and matplotlib
# J. Labbé, december 2019
##############################

# Import everything from matplotlib (numpy is accessible via 'np' alias)
from pylab import *

### Parameters ===================================

showfig = False

# Number of decades for log scale
# set to zero for linear scale
xdecades = 0
ydecades = 0

# Output filename
# One cas use wildcards :
#   %x and %y are replaced by the value of xdecades and ydecades
#   %s is replaced by '_semilog_n-decades' or '_log_n-m-decades' (or nothing with linear scale)
save = True
filename="Papier%s"
extension=".pdf"

# Paper and figure
landscape   = False  # if true, swap width and height
centimeters = True  # if false, length unit is inch (matplotlib defaut)
paperwidth  = 21.0
paperheight = 29.7
figwidth    = 16.0
figheight   = 24.0
rightmargin = 2.5
topmargin   = 2.5

# line styles
major_linestyle = '-'
major_linewidth = 0.5
major_color     = "black"
major_alpha     = 1.0

minor_linestyle = '-'
minor_linewidth = 0.25
minor_color     = 'black'
minor_alpha     = 0.7

### End of parameters block =====================

# Axes formatting function
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

# Create figure
unit = 1/2.54 if centimeters else 1
if landscape:
    paperheight, paperwidth = paperwidth, paperheight
    figheight, figwidth = figwidth, figheight
    rightmargin, topmargin = topmargin, rightmargin
fig = figure(figsize=(paperwidth*unit,paperheight*unit))
ax = fig.add_subplot(111)

# x axis
xmin = 0
xmax = figwidth
if (xdecades > 0):
    xmin = 10
    xmax = xmin*10**xdecades
    xscale('log')
    format_log_axis(ax.xaxis)
else:
    format_lin_axis(ax.xaxis)

# y axis
ymin = 0
ymax = figheight
if (ydecades > 0):
    ymin = 10
    ymax = ymin*10**ydecades
    yscale('log')
    format_log_axis(ax.yaxis)
else:
    format_lin_axis(ax.yaxis)

# x and y scales
xlim(xmin,xmax)
ylim(ymin,ymax)

# no ticks
ax.xaxis.set_ticks_position('none')
ax.yaxis.set_ticks_position('none')

# grid
ax.set_axisbelow(True) # grille sous le tracé
grid(True, which='minor', axis='both',linestyle=minor_linestyle,linewidth=minor_linewidth,color=minor_color,alpha=minor_alpha)
grid(True, which='major', axis='both',linestyle=major_linestyle,linewidth=major_linewidth,color=major_color,alpha=major_alpha)

# Margins
# from https://stackoverflow.com/questions/29400116/using-matplotlib-how-can-i-print-something-actual-size
leftmargin = paperwidth - figwidth - rightmargin
bottommargin = paperheight - figheight - topmargin
fig.subplots_adjust(left   = leftmargin / paperwidth,
                    bottom = bottommargin / paperheight,
                    right  = 1. - rightmargin / paperwidth,
                    top    = 1. - topmargin   / paperheight,
                    )

### Show and save

if save:
    if xdecades == 0 and ydecades == 0:
        filename = filename.replace('%s',"")
    elif xdecades != 0 and ydecades != 0:
        filename = filename.replace('%s',"_log_%x-%y-decades")
    elif xdecades + ydecades == 1:
        filename = filename.replace('%s',"_semilog_1-decade")
    else :
        filename = filename.replace('%s',"_semilog_"+str(xdecades+ydecades)+"-decades")
    filename = filename.replace('%x',str(xdecades))
    filename = filename.replace('%y',str(ydecades))
    savefig(filename+extension,dpi=600)
    print("File "+filename+extension+" created.")

if showfig:
    show()
