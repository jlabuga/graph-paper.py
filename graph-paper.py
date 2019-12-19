#!/usr/bin/python3
# -*- coding: utf-8 -*-
##############################
# papier échelles lin et log
# avec python3 et matplotlib
# J. Labbé - septembre 2019
##############################

# Import everything from matplotlib (numpy is accessible via 'np' alias)
from pylab import *

# paramètres
# mettre 0 pour avoir une échelle linéaire
decades_en_x = 2
decades_en_y = 0

# nom fichier sortie
filename="Papier"
extension=".pdf"

# Taille figure (hauteur 25 cm, largeur 17 cm)
# d'après https://stackoverflow.com/questions/29400116/using-matplotlib-how-can-i-print-something-actual-size
largeur_papier = 21.0 # com
hauteur_papier = 29.7 # com
largeur_figure = 18.0 # com
hauteur_figure = 25.0 # com 
marge_gauche   =  1.5 # cm
marge_haut     =  2.0 # cm

marge_droite = largeur_papier - largeur_figure - marge_gauche
marge_bas = hauteur_papier - hauteur_figure - marge_haut

cm2inch = 1/2.54 # inch per cm

fig = figure(figsize=(largeur_papier*cm2inch,hauteur_papier*cm2inch))
ax = fig.add_subplot(111)

xmin = 0
xmax = largeur_figure
ymin = 0
ymax = hauteur_figure

if (decades_en_x > 0):
    xmin = 10
    xmax = xmin*10**decades_en_x
    xscale('log')
    filename += "-"+str(decades_en_x)+"log"
    ax.xaxis.set_minor_locator(matplotlib.ticker.LogLocator(
        subs=[1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9,
              2.1,2.2,2.3,2.4,2.5,2.6,2.7,2.8,2.9,
              3.1,3.2,3.3,3.4,3.5,3.6,3.7,3.8,3.9,
              4.1,4.2,4.3,4.4,4.5,4.6,4.7,4.8,4.9,
              5.1,5.2,5.3,5.4,5.5,5.6,5.7,5.8,5.9,
              6.2,6.4,6.6,6.8,
              7.2,7.4,7.6,7.8,
              8.2,8.4,8.6,8.8,
              9.2,9.4,9.6,9.8]))
    ax.xaxis.set_major_locator(matplotlib.ticker.LogLocator(subs=[1.0,2,3,4,5,6,7,8,9]))
else:
    filename += "-lin"
    ax.xaxis.set_major_locator(matplotlib.ticker.MultipleLocator(1))
    ax.xaxis.set_minor_locator(matplotlib.ticker.MultipleLocator(0.1))

if (decades_en_y > 0):
    ymin = 10
    ymax = ymin*10**decades_en_y
    yscale('log')
    filename += "-"+str(decades_en_y)+"log"
    ax.yaxis.set_minor_locator(matplotlib.ticker.LogLocator(
        subs=[1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9,
              2.1,2.2,2.3,2.4,2.5,2.6,2.7,2.8,2.9,
              3.1,3.2,3.3,3.4,3.5,3.6,3.7,3.8,3.9,
              4.1,4.2,4.3,4.4,4.5,4.6,4.7,4.8,4.9,
              5.1,5.2,5.3,5.4,5.5,5.6,5.7,5.8,5.9,
              6.2,6.4,6.6,6.8,
              7.2,7.4,7.6,7.8,
              8.2,8.4,8.6,8.8,
              9.2,9.4,9.6,9.8]))
    ax.yaxis.set_major_locator(matplotlib.ticker.LogLocator(subs=[1.0,2,3,4,5,6,7,8,9]))
else:
    filename += "-lin"
    ax.yaxis.set_major_locator(matplotlib.ticker.MultipleLocator(1))
    ax.yaxis.set_minor_locator(matplotlib.ticker.MultipleLocator(0.1))

xlim(xmin,xmax)
ylim(ymin,ymax)

# label et ticks
xlabel = ""
ylabel = ""
ax.xaxis.set_ticks_position('none')
ax.yaxis.set_ticks_position('none')

# ax.xaxis.set_major_formatter(NullFormatter())
ax.xaxis.set_minor_formatter(NullFormatter())
ax.xaxis.set_major_formatter(FuncFormatter(lambda value, index: (index)%9+1))


# ax.set_xticklabels(["1","2","3","4","5","6","7","8","9"],minor=True, visible=True)
# ax.set_xticklabels([],minor=True)
ax.set_yticklabels([])
# xticks(color='none')
# yticks(color='none')

# grille
ax.set_axisbelow(True) # grille sous le tracé
grid(True, which='minor', axis='both',linestyle='-',linewidth=0.25,color="black",alpha=0.7)
grid(True, which='major', axis='both',linestyle='-',linewidth=0.5,color="black")

# Marges
#tight_layout(5)
fig.subplots_adjust(left   = marge_gauche / largeur_papier,
                    bottom = marge_bas / hauteur_papier,
                    right  = 1. - marge_droite / largeur_papier,
                    top    = 1. - marge_haut   / hauteur_papier,
                    )

# Sauver
savefig(filename+extension,dpi=600)
print("Fichier "+filename+extension+" créé.")

# Show result on screen
#show()
