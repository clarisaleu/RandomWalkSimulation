#!/bin/bash

# Circle - Radius 4 - Averages
python simulation.py -st RANDOM -r 4 -sh CIRCLE -n 1000 -d 0 > circ_4_rand_avg.txt
python simulation.py -st STAIRCASE -r 4 -sh CIRCLE -n 1000 -d 0 > circ_4_stair_avg.txt
python simulation.py -st SPIRL -r 4 -sh CIRCLE -n 1000 -d 0 > circ_4_spiral_avg.txt

# Circle - Radius 4 - Distribution
python simulation.py -st RANDOM -r 4 -sh CIRCLE -n 10000 -d 1 > circ_4_rand_dist.txt
python simulation.py -st STAIRCASE -r 4 -sh CIRCLE -n 10000 -d 1 > circ_4_stair_dist.txt
python simulation.py -st SPIRL -r 4 -sh CIRCLE -n 10000 -d 1 > circ_4_spiral_dist.txt
