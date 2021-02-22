# RandomWalkSimulation
Bellman's lost in a forest problem simulation in Python.

## Dependencies
- Python Version 3.X
- [numpy](https://pypi.org/project/numpy/) installed in your python environments (e.g., via `pip install numpy`)
- [shapely](https://pypi.org/project/Shapely/) installed in your python environments (e.g., via `pip install shapely`)

## Run Me
`` python3 simulation.py -st [STRATEGY] -sh [SHAPE] -r [RADIUS] - he [HEIGHT] -w [WIDTH] -l [LENGTH]``

e.g. - to simulate the forest problem with a circle-shaped forest of radius of 30 with the just walk up strategy:
- `` python3 simulation.py -st UP -sh CIRCLE -r 30``

to simulate the forest problem with a rectangle-shaped forest with a height of 5 and width of 7 with the just walk right strategy:
- `` python3 simulation.py -st RIGHT -sh RECTANGLE -h 5 -w 7``

to simulate the forest problem with a triangle-shaped forest with a length of 5 with the walk in a zig-zag strategy:
- `` python3 simulation.py -st ZIGZAG -sh TRIANGLE -l 5``


Optional arguments:
- ``-st [the strategy to use]``, where the different strategies are: RIGHT, UP, ZIGZAG, SPIRAL
- ``-sh [the shape of the forest to use]``, where the different shapes available to simulate are: RECTANGLE, CIRCLE, TRIANGLE, OCTAGON, HEXAGON
- ``-r [if using a circle as the forest's shape, the radius of the circle]``
- ``-he [if using a rectangle as the forest's shape, the height of the rectangle]``
- ``-w [if using a rectangle as the forest's shape, the width of the rectangle]``
- ``-l [if using a triangle/hexagon/octagon as the forest's shape, the length of the edge]``