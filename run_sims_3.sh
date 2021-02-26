#!/bin/bash

# Circle - Radius 2 - Averages
python simulation.py -st RANDOM -r 2 -sh CIRCLE -n 10000 -d 0 > circ_2_rand_avg.txt
python simulation.py -st STAIRCASE -r 2 -sh CIRCLE -n 10000 -d 0 > circ_2_stair_avg.txt
python simulation.py -st SPIRL -r 2 -sh CIRCLE -n 10000 -d 0 > circ_2_spiral_avg.txt

# Circle - Radius 2 - Distribution
python simulation.py -st RANDOM -r 2 -sh CIRCLE -n 10000 -d 1 > circ_2_rand_dist.txt
python simulation.py -st STAIRCASE -r 2 -sh CIRCLE -n 10000 -d 1 > circ_2_stair_dist.txt
python simulation.py -st SPIRL -r 2 -sh CIRCLE -n 10000 -d 1 > circ_2_spiral_dist.txt
