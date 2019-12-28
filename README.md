graph-paper.py
==============

**[→ Version française](LISEZMOI.md)** (link to french readme).


Simple script to create graph papers (with linear or log scale) using `python3` 
and `matplotlib`. Ones can set the parameters à the beginning of the scripts.
To use it, run (if `matplotlib` is installed):
```
python3 graph-paper.py
```

To select log scale, set `xdecade` and `ydecade` at the appropriate number of
decades. Setting one of these variables to zero means linear scale. Example, for
semi-log paper with three log modules on the x-axis and a linear y-axis, use :
```python
# Number of decades for log scale
# set to zero for linear scale
xdecades = 3
ydecades = 0
```

The output file is created only if the variable `save` is set to `True` :
```python
save = True
```

The output file name is set with `filename` and `extension`. Some widdcards are
availlable :
 * `%x` and `%y` are replaced by the value of `xdecades` and `ydecades`.
 * `%s` is replaced by `_semilog_n-decades` or `_log_n-m-decades` (or nothing
   for linear scale).

For example :
```python
filename="Papier%s"
extension=".pdf"
```

The paper and figure geometries are set by the following variables :
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

Line style of minor and major grid lines are set by the following variables :
```python
major_linestyle = '-'
major_linewidth = 0.5
major_color     = "black"
major_alpha     = 1.0

minor_linestyle = '-'
minor_linewidth = 0.25
minor_color     = 'black'
minor_alpha     = 0.7
```

To show the figure, at the moment of the creation, use :
```python
showfig = True
```
