#!/bin/bash

# 4x4 Square - Averages
python simulation.py -st RANDOM -he 4 -w 4 -sh RECTANGLE -n 1000 -d 0 > rect4_4_rand_avg.txt
python simulation.py -st STAIRCASE -he 4 -w 4 -sh RECTANGLE -n 1000 -d 0 > rect4_4_stair_avg.txt
python simulation.py -st SPIRAL -he 4 -w 4 -sh RECTANGLE -n 1000 -d 0 > rect4_4_spiral_avg.txt

# 4x4 Square - Distribution
python simulation.py -st RANDOM -he 4 -w 4 -sh RECTANGLE -n 10000 -d 1 > rect4_4_rand_dist.txt
python simulation.py -st STAIRCASE -he 4 -w 4 -sh RECTANGLE -n 10000 -d 1 > rect4_4_stair_dist.txt
python simulation.py -st SPIRAL -he 4 -w 4 -sh RECTANGLE -n 10000 -d 1 > rect4_4_spiral_dist.txt
