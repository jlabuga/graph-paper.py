graph-paper.py
==============

Simple script to create graph paper (linear or log scale) with `python3` and `matplotlib`. Ones can change the parameters à the beginning of the scripts.
To run it, run (if `matplotlib` is installed):
```
python3 graph-paper.py
```

To select log scale, set `xdecade` and `ydecade` at appropriate number of decades. Setting one of these variable to zero means linear scale.

```python
# Number of decades for log scale
# set to zero for linear scale
xdecades = 3
ydecades = 0
```

To create output file, set `save` to `True` :
```python
save = True
```

To set output file name, set `filename` and `extension`. Some widdcards are availlable :
 * `%x` and `%y` are replaced by the value of `xdecades` and `ydecades`
 * `%s` is replaced by `_semilog_n-decades` or `_log_n-m-decades` (or nothing
   for linear scale).

Example :
```python
filename="Papier%s"
extension=".pdf"
```

To set paper and figure geometry, use following variables :
```python
landscape   = True  # if true, swap width and height
centimeters = True  # if false, length unit is inch (matplotlib defaut)
paperwidth  = 21.0
paperheight = 29.7
figwidth    = 16.0
figheight   = 24.0
rightmargin = 2.5
topmargin   = 2.5
```

To set minor and major grid line style set the following variables :
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

If you want to view the figure, at creation, set `showfig` :
```python
showfig = True
```
