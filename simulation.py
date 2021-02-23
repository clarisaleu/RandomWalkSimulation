#
# By: Clarisa Leu-Rodriguez and Rene Vazquez
# Winter 2021 - MATAH381 - Matthew M. Conroy
#
# Python program to simulate the Bellman's lost in a forest problem
# with various strategies, forest shapes, and forest sizes.
# The Bellman's lost in a forest problem asks, "A hiker is lost in a forest 
# whose shape and dimensions are precisely known to him - however he does not know
# his starting point or the direction he is facing. 
# What is the best path for him to follow to escape from the forest?"
#
# Note: Coordinate system used in this program has the origin as the bottom left corner - with
# x increasing positively to the right and y increasing positively upwards.
#
# Read README.md for instructions on program usage.
#

import random
import numpy as np
import math
import argparse

# TODO: large scale random walk. take big steps and then if we don't get out - do it in another step. we know width/height.
# pick random direction for zig zag, turn 90 degrees go. (have bigger step size). for zigzag and spiral we can change parameters.
# pick random point, random direction, calculate line to escape forest. we know line path is on - top of square is.
STRATEGIES = ['RANDOM', 'ZIGZAG', 'SPIRAL']  # Strategies to simulate.
SHAPES = ['RECTANGLE', 'CIRCLE', 'L-SHAPED']  # Different shapes of forests to simulate.
step_size = 0.01  # Hiker's step size is 1 unit of length.

def main(shape, strategy, height, width, radius, n):
    # Call appropiate method based on passed in shape of forest to simulate.
    i = 0  # Do 1,000 n-simulations for central limit theorem.
    if (shape == 'RECTANGLE'):
        while (i < 1000):
            rectangle(strategy, height, width, n)
            i += 1
    elif (shape == 'CIRCLE'):
        while (i < 1000):
            circle(strategy, radius, n)
            i += 1
    elif (shape == 'L-SHAPED'):
        while (i < 1000):
            l_shape(strategy, length, n)
            i += 1

############ Helper functions for to set up different forest shapes ############

# Rectangle-shaped forest.
def rectangle(strategy, height, width, n):
    num_steps_avg = 0  # Keep track of a running average.
    for i in range(n):
        # Pick a random starting position - where every position is equally likely.
        start_pos_x = np.random.uniform(0, width - 1)
        start_pos_y = np.random.uniform(0, height - 1)
        # print("Starting walk at: (%f, %f)" % (start_pos_x, start_pos_y))
        cur_pos_x = start_pos_x
        cur_pos_y = start_pos_y
        positions = [(start_pos_x, start_pos_y)]  # Keep track of coordinates for each step.
        # Use the passed in strategy to escape the forest.
        if (strategy == 'RANDOM'):
            num_steps_avg += move_random('RECTANGLE', None, positions, width, height, 0, 0, 0)
        elif (strategy == 'ZIGZAG'):
            num_steps_avg += move_zig_zag('RECTANGLE', None, positions, width, height, 0, 0, 0)
        elif (strategy == 'SPIRAL'):
            num_steps_avg += move_spiral('RECTANGLE', None, positions, width, height, 0, 0, 0)

    # Print out average number of steps needed.
    print(1.0 * num_steps_avg / n)
    # print ("Average number of steps: ", 1.0 * num_steps_avg / n)

# Circle-shaped forest.
def circle(strategy, radius, n):
    # Circle in our coordinate system is always centered at (radius, radius)
    num_steps_avg = 0
    center_x = radius
    center_y = radius
    for i in range(n):
        # Pick a random starting position - where every position is equally likely.
        alpha = np.pi * np.random.uniform(0, 2)  # in radians
        r = (np.random.uniform(0, radius)) ** 0.5
        start_pos_x = (r * np.cos(alpha)) + center_x
        start_pos_y = (r * np.sin(alpha)) + center_y
        # print("Starting walk at: (%f, %f)" % (start_pos_x, start_pos_y))
        positions = [(start_pos_x, start_pos_y)]  # Keep track of coordinates for each step.
        # Use the passed in strategy to escape the forest.
        if (strategy == 'RANDOM'):
            num_steps_avg += move_random('CIRCLE', None, positions, 0, 0, center_x, center_y, radius)
        elif (strategy == 'ZIGZAG'):
            num_steps_avg += move_zig_zag('CIRCLE', None, positions, 0, 0, center_x, center_y, radius)
        elif (strategy == 'SPIRAL'):
            num_steps_avg += move_spiral('CIRCLE', None, positions, 0, 0, center_x, center_y, radius)
    
    # Print out average number of steps needed.
    print (1.0 * num_steps_avg / n)
    # print ("Average number of steps: ", 1.0 * num_steps_avg / n)

# Circle-shaped forest.
def l_shape(strategy, radius, n):
    # Circle in our coordinate system is always centered at (radius, radius)
    num_steps_avg = 0
    center_x = radius
    center_y = radius
    for i in range(n):
        # Pick a random starting position - where every position is equally likely.
        alpha = np.pi * np.random.uniform(0, 2)  # in radians
        r = (np.random.uniform(0, radius)) ** 0.5
        start_pos_x = (r * np.cos(alpha)) + center_x
        start_pos_y = (r * np.sin(alpha)) + center_y
        # print("Starting walk at: (%f, %f)" % (start_pos_x, start_pos_y))
        positions = [(start_pos_x, start_pos_y)]  # Keep track of coordinates for each step.
        # Use the passed in strategy to escape the forest.
        if (strategy == 'RANDOM'):
            num_steps_avg += move_random('CIRCLE', None, positions, 0, 0, center_x, center_y, radius)
        elif (strategy == 'ZIGZAG'):
            num_steps_avg += move_zig_zag('CIRCLE', None, positions, 0, 0, center_x, center_y, radius)
        elif (strategy == 'SPIRAL'):
            num_steps_avg += move_spiral('CIRCLE', None, positions, 0, 0, center_x, center_y, radius)
    
    # Print out average number of steps needed.
    print (1.0 * num_steps_avg / n)
    # print ("Average number of steps: ", 1.0 * num_steps_avg / n)

l
############ Helper functions to check if point is inside forest based on shape ############

# Helper method used to check if a given (x, y) point is inside of a circle
# of radius rad centered at (circle_x, circle_y).
def is_inside_circle(circle_x, circle_y, rad, x, y): 
    # Compare radius of circle with distance of its center from given point 
    if ((x - circle_x) * (x - circle_x) + (y - circle_y) * (y - circle_y) <= rad * rad):
        return True
    else: 
        return False


############ Helper functions to move based on strategy and shape ############

# Helper method to handle the move right strategy.
def move_random(shape, polygon, positions, width, height, center_x, center_y, radius):
    j = 0
    point = positions[j]
    cur_pos_x = point[0]
    cur_pos_y = point[1]
    num_steps_avg = 0
    alpha = np.pi * np.random.uniform(0, 2)  # in radians
    while (1):
        cur_position = positions[j]  # Look at curent position.
        # print(cur_position)
        # Based on shape - see if the current position is inside or outside of shape.
        outside_of_shape = False
        if (shape == 'RECTANGLE'):
            outside_of_shape = (cur_pos_x > width - 1) or (cur_pos_y > height - 1) or (cur_pos_x < 0) or (cur_pos_y < 0)
        elif (shape == 'CIRCLE'):
            outside_of_shape = not is_inside_circle(center_x, center_y, radius, cur_pos_x, cur_pos_y)
        if (outside_of_shape):
            break
        
        next_pos_x = step_size * math.cos(alpha) + cur_pos_x
        next_pos_y = step_size * math.sin(alpha) + cur_pos_y
        positions.append((next_pos_x, next_pos_y))
        cur_pos_x = next_pos_x
        cur_pos_y = next_pos_y
        num_steps_avg += 1
        j += 1
    # Print out the number of steps needed for this trial.
    # print(len(positions)-1)
    return num_steps_avg

# Helper method to handle the zig-zag strategy.
def move_zig_zag (shape, polygon, positions, width, height, center_x, center_y, radius):
    j = 0
    point = positions[j]
    cur_pos_x = point[0]
    cur_pos_y = point[1]
    num_steps_avg = 0
    alpha = np.pi * np.random.uniform(0, 2)  # in radians
    while (1):
        cur_position = positions[j]  # Look at curent position.
        # print(cur_position)
        # Based on shape - see if the current position is inside or outside of shape.
        outside_of_shape = False
        if (shape == 'RECTANGLE'):
            outside_of_shape = (cur_pos_x > width - 1) or (cur_pos_y > height - 1) or (cur_pos_x < 0) or (cur_pos_y < 0)
        elif (shape == 'CIRCLE'):
            outside_of_shape = not is_inside_circle(center_x, center_y, radius, cur_pos_x, cur_pos_y)
        if (outside_of_shape):
            break
        if (len(positions) % 2 == 1):
            next_pos_y = cur_position[1] + step_size * math.sin(alpha)
            positions.append((cur_position[0], next_pos_y))
            cur_pos_y = next_pos_y
        else:
            next_pos_x = cur_position[0] + step_size * math.cos(alpha)
            positions.append((next_pos_x, cur_position[1]))
            cur_pos_x = next_pos_x
        num_steps_avg += 1
        j += 1
    # Print out the number of steps needed for this trial.
    # print(len(positions)-1)
    return num_steps_avg

# Helper method to handle the spiral strategy.
def move_spiral(shape, polygon, positions, width, height, center_x, center_y, radius):
    j = 0
    cur_spiral_side = 1  # change cur_spiral_side.
    point = positions[j]
    cur_pos_x = point[0]
    cur_pos_y = point[1]
    num_steps_avg = 0
    alpha = np.pi * np.random.uniform(0, 2)  # in radians
    while (1):
        cur_position = positions[j]  # Look at curent position.
        # print(cur_position)
        # Based on shape - see if the current position is inside or outside of shape.
        outside_of_shape = False
        if (shape == 'RECTANGLE'):
            outside_of_shape = (cur_pos_x > width - 1) or (cur_pos_y > height - 1) or (cur_pos_x < 0) or (cur_pos_y < 0)
        elif (shape == 'CIRCLE'):
            outside_of_shape = not is_inside_circle(center_x, center_y, radius, cur_pos_x, cur_pos_y)
        if (outside_of_shape):
            break
        if (cur_spiral_side % 2 == 1):
            next_pos_x = cur_position[0] + (cur_spiral_side * math.cos(alpha))
            next_pos_y = cur_position[1] + (cur_spiral_side * math.sin(alpha))
            positions.append((next_pos_x, next_pos_y))
            cur_pos_x = next_pos_x
            cur_pos_y = next_pos_y
        else:
            next_pos_x = cur_position[0] - (cur_spiral_side * math.cos(alpha))
            next_pos_y = cur_position[1] - (cur_spiral_side * math.sin(alpha))
            positions.append((next_pos_x, next_pos_y))
            cur_pos_x = next_pos_x
            cur_pos_y = next_pos_y 
        num_steps_avg += (2 * cur_spiral_side)
        cur_spiral_side += 1
        j += 1
    # Print out the number of steps needed for this trial.
    # print(len(positions)-1)
    return num_steps_avg


if __name__ == '__main__':
    # Parse user passed in arguments and call appropiate function based on passed in shape.
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("-st", "--strategy", type = str, help = "the strategy to use", default = "RANDOM", choices = STRATEGIES)
    arg_parser.add_argument("-sh", "--shape", type = str, help = "the shape of the forest to use", default = "RECTANGLE", choices = SHAPES)
    arg_parser.add_argument("-r", "--radius", type = int, help = "the radius of the circle to use", default = 3)
    arg_parser.add_argument("-he", "--height", type = int, help = "the height of the rectangle to use", default = 2)
    arg_parser.add_argument("-w", "--width", type = int, help = "the width of the rectangle to use", default = 2)
    arg_parser.add_argument("-n", "--num_trials", type = int, help = "the number of trials to use for simulation", default = 100)

    args = arg_parser.parse_args()
    main(args.shape, args.strategy, args.height, args.width, args.radius, args.num_trials)