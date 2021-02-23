# Random Walk Simulation
Bellman's lost in a forest problem simulation in Python.

## Dependencies
- Python Version 3.X
- [numpy](https://pypi.org/project/numpy/) installed in your python environments (e.g., via `pip install numpy`)
- [shapely](https://pypi.org/project/Shapely/) installed in your python environments (e.g., via `pip install shapely`)

## Run Me
`` python3 simulation.py -st [STRATEGY] -sh [SHAPE] -r [RADIUS] - he [HEIGHT] -w [WIDTH]``

Optional arguments:
- ``-st [the strategy to use]``, where the different strategies are: RANDOM, ZIGZAG, SPIRAL
- ``-sh [the shape of the forest to use]``, where the different shapes available to simulate are: RECTANGLE, CIRCLE, L-SHAPE
- ``-r [if using a circle as the forest's shape, the radius of the circle]``
- ``-he [if using a rectangle as the forest's shape, the height of the rectangle]``
- ``-w [if using a rectangle as the forest's shape, the width of the rectangle]``