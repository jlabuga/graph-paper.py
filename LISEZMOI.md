graph-paper.py
==============

Simple script pour créer des papiers quadrillés avec `python3` et
`patplotlib`. Les paramètres sont configurés au début du script. Si
`matplotlib` est installé, lancer le script avec :
```
python3 graph-paper.py
```

On peut choisir le nombre de décades, en abscisse et en ordonnée avec les
variables `xdecade` and `ydecade`. Pour avoir une échelle linéaire, régler une
de ces variables à zéro. Par exemple, pour un papier semi-logarithmique, avec
trois décades en abscisse et une échelle linéaire en ordonnée, utiliser :

```python
xdecades = 3
ydecades = 0
```

Pour que le fichier de sortie soit créé, il faut configurer la variable `save` :
```python
save = True
```

Le nom du fichier de sortie, et son extension, sont déterminés par les variables
`filename` et `extension`. Certains motifs peuvent être utilisés :
 * `%x` sont `%y` sont remplacés par les valeurs de `xdecades` et `ydecades` ;
 * `%s` est remplacé par `_semilog_n-decades` ou `_log_n-m-decades` (ou par une
   chaîne de caractères vide pour une échelle linéaire).

Exemple :
```python
filename="Papier%s"
extension=".pdf"
```

Les dimensions de la page et de la figure, et leur orientation, sont déterminées par les
variables suivantes  :
```python
landscape   = True  # if true, swap width and height
centimeters = True  # if false, length unit is inch (matplotlib default)
paperwidth  = 21.0
paperheight = 29.7
figwidth    = 16.0
figheight   = 24.0
rightmargin = 2.5
topmargin   = 2.5
```

Le style des lignes utilisées pour tracer les lignes de la grilles (*minor* et
*major*) sont déterminés par les variables :
```python
major_linestyle = '-'
major_linewidth = 0.5 
majorcolor _    = "black"
majoralpha      = 1.0

minor_linestyle = '-'
minor_linewidth = 0.25
minor_color     = 'black'
minor_alpha     = 0.7
```

Il est enfin possible d'afficher la figure, lors de sa création, avec `showfig` :
```python
showfig = True
```
