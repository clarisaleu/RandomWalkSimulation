#!/bin/bash

# 2x2 Square - Averages
#python simulation.py -st RANDOM -he 2 -w 2 -sh RECTANGLE -n 1000 -d 0 > rect2_2_rand_avg.txt 
#python simulation.py -st STAIRCASE -he 2 -w 2 -sh RECTANGLE -n 1000 -d 0 > rect2_2_stair_avg.txt
#python simulation.py -st SPIRAL -he 2 -w 2 -sh RECTANGLE -n 1000 -d 0 > rect2_2_spiral_avg.txt

# 2x2 Square - Distribution
#python simulation.py -st RANDOM -he 2 -w 2 -sh RECTANGLE -n 10000 -d 1 > rect2_2_rand_dist.txt 
#python simulation.py -st STAIRCASE -he 2 -w 2 -sh RECTANGLE -n 10000 -d 1 > rect2_2_stair_dist.txt
#python simulation.py -st SPIRAL -he 2 -w 2 -sh RECTANGLE -n 10000 -d 1 > rect2_2_spiral_dist.txt


python simulation.py -st RANDOM -he 4 -w 4 -sh RECTANGLE -n 10000 -d 1 > rect4_4_rand_dist.txt 
python simulation.py -st STAIRCASE -he 4 -w 4 -sh RECTANGLE -n 10000 -d 1 > rec4_4_stair_dist.txt
python simulation.py -st SPIRAL -he 4 -w 4 -sh RECTANGLE -n 10000 -d 0 > rect4_4_spiral_avg.txt
