#!/bin/bash

# Circle - Radius 1 - Averages
#python simulation.py -st RANDOM -r 1 -sh CIRCLE -n 1000 -d 0 > circ_1_rand_avg.txt
#python simulation.py -st STAIRCASE -r 1 -sh CIRCLE -n 1000 -d 0 > circ_1_stair_avg.txt
python simulation.py -st SPIRAL -r 1 -sh CIRCLE -n 1000 -d 0 > circ_1_spiral_avg.txt

# Circle - Radius 1 - Distribution
#python simulation.py -st RANDOM -r 1 -sh CIRCLE -n 10000 -d 1 > circ_1_rand_dist.txt
#python simulation.py -st STAIRCASE -r 1 -sh CIRCLE -n 10000 -d 1 > circ_1_stair_dist.txt
python simulation.py -st SPIRAL -r 1 -sh CIRCLE -n 10000 -d 1 > circ_1_spiral_dist.txt
