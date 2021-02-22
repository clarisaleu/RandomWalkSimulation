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
from shapely.geometry.point import Point
from shapely.geometry.polygon import Polygon
import argparse

STRATEGIES = ['RIGHT', 'UP', 'ZIGZAG', 'SPIRAL']  # Strategies to simulate.
SHAPES = ['RECTANGLE', 'CIRCLE', 'TRIANGLE', 'OCTAGON', 'HEXAGON']  # Different shapes of forests to simulate.
step_size = 1  # Hiker's step size is 1 unit of length.

def main(shape, strategy, height, width, radius, length, n):
    # Call appropiate method based on passed in shape of forest to simulate.
    if (shape == 'RECTANGLE'):
        rectangle(strategy, height, width, n)
    elif (shape == 'CIRCLE'):
        circle(strategy, radius, n)
    elif (shape == 'TRIANGLE'):
        triangle(strategy, length, n)
    elif (shape == 'OCTAGON'):
        octagon(strategy, length, n)
    elif (shape == 'HEXAGON'):
        hexagon(strategy, length, n)

############ Helper functions for to set up different forest shapes ############

# Rectangle-shaped forest.
def rectangle(strategy, height, width, n):
    num_steps_avg = 0  # Keep track of a running average.
    for i in range(n):
        # Pick a random starting position - where every position is equally likely.
        start_pos_x = np.random.uniform(0, width - 1)
        start_pos_y = np.random.uniform(0, height - 1)
        print("Starting walk at: (%d, %d)" % (start_pos_x, start_pos_y))
        cur_pos_x = start_pos_x
        cur_pos_y = start_pos_y
        positions = [(start_pos_x, start_pos_y)]  # Keep track of coordinates for each step.
        # Use the passed in strategy to escape the forest.
        if (strategy == 'RIGHT'):
            num_steps_avg += move_right('RECTANGLE', None, positions)
        elif (strategy == 'UP'):
            num_steps_avg += move_up('RECTANGLE', None, positions)
        elif (strategy == 'ZIGZAG'):
            num_steps_avg += move_zig_zag('RECTANGLE', None, positions)
        elif (strategy == 'SPIRAL'):
            num_steps_avg += move_spiral('RECTANGLE', None, positions)

    # Print out average number of steps needed.
    print ("Average number of steps: ", 1.0 * num_steps_avg / n)

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
        print("Starting walk at: (%f, %f)" % (start_pos_x, start_pos_y))
        positions = [(start_pos_x, start_pos_y)]  # Keep track of coordinates for each step.
        # Use the passed in strategy to escape the forest.
        if (strategy == 'RIGHT'):
            num_steps_avg += move_right('CIRCLE', None, positions)
        elif (strategy == 'UP'):
            num_steps_avg += move_up('CIRCLE', None, positions)
        elif (strategy == 'ZIGZAG'):
            num_steps_avg += move_zig_zag('CIRCLE', None, positions)
        elif (strategy == 'SPIRAL'):
            num_steps_avg += move_spiral('CIRCLE', None, positions)
    
    # Print out average number of steps needed.
    print ("Average number of steps: ", 1.0 * num_steps_avg / n)

# Triangle-shaped forest.
# TODO should we test different types of triangles?
def triangle(strategy, length, n):
    # Triangle in our coordinate system is always formed by the points (0, 0), 
    # (length, length), and (length, 0).
    num_steps_avg = 0
    x1 = 0
    y1 = 0
    x2 = length
    y2 = length
    x3 = length
    y3 = 0
    for i in range(n):
        point = generate_random_point_triangle((x1,y1), (x2, y2), (x3, y3))
        start_pos_x = point[0]
        start_pos_y = point[1]
        print("Starting walk at: (%f, %f)" % (start_pos_x, start_pos_y))
        positions = [(start_pos_x, start_pos_y)]  # Keep track of coordinates for each step.
        # Use the passed in strategy to escape the forest.
        if (strategy == 'RIGHT'):
            num_steps_avg += move_right('TRIANGLE', None, positions)
        elif (strategy == 'UP'):
            num_steps_avg += move_up('TRIANGLE', None, positions)
        elif (strategy == 'ZIGZAG'):
            num_steps_avg += move_zig_zag('TRIANGLE', None, positions)
        elif (strategy == 'SPIRAL'):
            num_steps_avg += move_spiral('TRIANGLE', None, positions)
    
    # Print out average number of steps needed.
    print ("Average number of steps: ", 1.0 * num_steps_avg / n)


# Octagon-shaped forest.
def octagon(strategy, length, n):
    num_steps_avg = 0
    # Octagon is in our coordinate system defined by the 8 points (0,length), (0, 2*length), (length, 0), (2*length, 0),
    # (3*length, length), (3*length, 2*length), (length, 3*length), (2*length, 3*length)
    octagon = Polygon([(0, length), (0, 2*length), (length, 0), (2*length, 0), (3*length, length), (3*length, 2*length), (length, 3*length), (2*length, 3*length)])
    for i in range(n):
        point = generate_random_point_polygon(octagon, 0, 3 * length, 0, 3 * length)
        start_pos_x = point[0]
        start_pos_y = point[1]
        print("Starting walk at: (%f, %f)" % (start_pos_x, start_pos_y))
        positions = [(start_pos_x, start_pos_y)]
        if (strategy == 'RIGHT'):
            num_steps_avg += move_right('OCTAGON', octagon, positions)
        elif (strategy == 'UP'):
            num_steps_avg += move_up('OCTAGON', octagon, positions)
        elif (strategy == 'ZIGZAG'):
            num_steps_avg += move_zig_zag('OCTAGON', octagon, positions)
        elif (strategy == 'SPIRAL'):
            num_steps_avg += move_spiral('OCTAGON', octagon, positions)
    
    # Print out average number of steps needed.
    print ("Average number of steps: ", 1.0 * num_steps_avg / n)

# Hexagon-shaped forest.
def hexagon(strategy, length, n):
    num_steps_avg = 0
    # Hexagon is in our coordinate system defined by the 6 points (0, length), (length, 0), 
    # (3*length, length), (2*length, 0), (2*length, 2*length), (length, 2*length)
    hexagon = Polygon([(0, length), (length, 0), (3*length, length), (2*length, 0), (2*length, 2*length), (length, 2*length)])
    for i in range(n):
        point = generate_random_point_polygon(hexagon, 0, 3 * length, 0, 2 * length)
        start_pos_x = point[0]
        start_pos_y = point[1]
        print("Starting walk at: (%f, %f)" % (start_pos_x, start_pos_y))
        positions = [(start_pos_x, start_pos_y)]
        if (strategy == 'RIGHT'):
            num_steps_avg += move_right('HEXAGON', hexagon, positions)
        elif (strategy == 'UP'):
            num_steps_avg += move_up('HEXAGON', hexagon, positions)
        elif (strategy == 'ZIGZAG'):
            num_steps_avg += move_zig_zag('HEXAGON', hexagon, positions)
        elif (strategy == 'SPIRAL'):
            num_steps_avg += move_spiral('HEXAGON', hexagon, positions)
    
    # Print out average number of steps needed.
    print ("Average number of steps: ", 1.0 * num_steps_avg / n)


############ Helper functions to check if point is inside forest based on shape/generating a random point in shape ############

# Helper method used to check if a given (x, y) point is inside of a circle
# of radius rad centered at (circle_x, circle_y).
def is_inside_circle(circle_x, circle_y, rad, x, y): 
    # Compare radius of circle with distance of its center from given point 
    if ((x - circle_x) * (x - circle_x) + (y - circle_y) * (y - circle_y) <= rad * rad):
        return True
    else: 
        return False

# A helper function to calculate the area of a triangle defined with the vertices: 
# (x1, y1), (x2, y2) and (x3, y3) 
def area_triangle(x1, y1, x2, y2, x3, y3):
    return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0)

# A helper function to check whether point (x, y) lies inside the triangle formed by  
# its vertices (x1, y1), (x2, y2) and (x3, y3)
def is_inside_triangle(x1, y1, x2, y2, x3, y3, x, y): 
    # Calculate area of triangle ABC 
    A = area_triangle(x1, y1, x2, y2, x3, y3) 
    A1 = area_triangle(x, y, x2, y2, x3, y3) 
    A2 = area_triangle(x1, y1, x, y, x3, y3) 
    A3 = area_triangle(x1, y1, x2, y2, x, y)
    if(A == A1 + A2 + A3):
        return True
    else: 
        return False

# Helper function to generate a random, uniformly distributed point in a polygon shape.
def generate_random_point_polygon(polygon, xmin, xmax, ymin, ymax):
    x = np.random.uniform(xmin, xmax)
    y = np.random.uniform(ymin, ymax)
    point = Point(x, y)
    if (polygon.contains(point) and x is not None and y is not None):
        return (x, y)
    else:
        return generate_random_point_polygon(polygon, xmin, xmax, ymin, ymax)

# A helper function to generate a random point inside the triangle formed by its
# Vertices pt1, pt2, pt3
def generate_random_point_triangle(pt1, pt2, pt3):
    s, t = sorted([random.random(), random.random()])
    return (s * pt1[0] + (t-s)*pt2[0] + (1-t)*pt3[0], s * pt1[1] + (t-s)*pt2[1] + (1-t)*pt3[1])


############ Helper functions to move based on strategy and shape ############

# Helper method to handle the move right strategy.
def move_right(shape, polygon, positions):
    j = 0
    point = positions[j]
    cur_pos_x = point[0]
    cur_pos_y = point[1]
    num_steps_avg = 0
    while (1):
        cur_position = positions[j]  # Look at curent position.
        print(cur_position)
        # Based on shape - see if the current position is inside or outside of shape.
        outside_of_shape = False
        if (shape == 'RECTANGLE'):
            outside_of_shape = (cur_pos_x > width - 1) or (cur_pos_y > height - 1) or (cur_pos_x < 0) or (cur_pos_y < 0)
        elif (shape == 'TRIANGLE'):
            outside_of_shape = not is_inside_triangle(x1, y1, x2, y2, x3, y3, cur_pos_x, cur_pos_y)
        elif (shape == 'CIRCLE'):
            outside_of_shape = not is_inside_circle(center_x, center_y, radius, cur_pos_x, cur_pos_y)
        elif (shape == 'OCTAGON' or shape == 'HEXAGON'):
            point = Point(cur_pos_x, cur_pos_y)
            outside_of_shape = not polygon.contains(point)
        if (outside_of_shape):
            break
        next_pos_x = cur_position[0] + step_size  # Just go right.
        positions.append((next_pos_x, cur_position[1]))
        cur_pos_x = next_pos_x
        num_steps_avg += 1
        j += 1
    # Print out the number of steps needed for this trial.
    # print(len(positions)-1)
    return num_steps_avg

# Helper method to handle the move up strategy.
def move_up(shape, polygon, positions):
    j = 0
    point = positions[j]
    cur_pos_x = point[0]
    cur_pos_y = point[1]
    num_steps_avg = 0
    while (1):
        cur_position = positions[j]  # Look at curent position.
        print(cur_position)
        # Based on shape - see if the current position is inside or outside of shape.
        outside_of_shape = False
        if (shape == 'RECTANGLE'):
            outside_of_shape = (cur_pos_x > width - 1) or (cur_pos_y > height - 1) or (cur_pos_x < 0) or (cur_pos_y < 0)
        elif (shape == 'TRIANGLE'):
            outside_of_shape = not is_inside_triangle(x1, y1, x2, y2, x3, y3, cur_pos_x, cur_pos_y)
        elif (shape == 'CIRCLE'):
            outside_of_shape = not is_inside_circle(center_x, center_y, radius, cur_pos_x, cur_pos_y)
        elif (shape == 'OCTAGON' or shape == 'HEXAGON'):
            point = Point(cur_pos_x, cur_pos_y)
            outside_of_shape = not polygon.contains(point)
        if (outside_of_shape):
            break
        next_pos_y = cur_position[1] + step_size  # Just go up.
        positions.append((cur_position[0], next_pos_y))
        cur_pos_y = next_pos_y
        num_steps_avg += 1
        j += 1
    # Print out the number of steps needed for this trial.
    # print(len(positions)-1)
    return num_steps_avg

# Helper method to handle the zig-zag strategy.
def move_zig_zag(shape, polygon, positions):
    j = 0
    point = positions[j]
    cur_pos_x = point[0]
    cur_pos_y = point[1]
    num_steps_avg = 0
    while (1):
        cur_position = positions[j]  # Look at curent position.
        print(cur_position)
        # Based on shape - see if the current position is inside or outside of shape.
        outside_of_shape = False
        if (shape == 'RECTANGLE'):
            outside_of_shape = (cur_pos_x > width - 1) or (cur_pos_y > height - 1) or (cur_pos_x < 0) or (cur_pos_y < 0)
        elif (shape == 'TRIANGLE'):
            outside_of_shape = not is_inside_triangle(x1, y1, x2, y2, x3, y3, cur_pos_x, cur_pos_y)
        elif (shape == 'CIRCLE'):
            outside_of_shape = not is_inside_circle(center_x, center_y, radius, cur_pos_x, cur_pos_y)
        elif (shape == 'OCTAGON' or shape == 'HEXAGON'):
            point = Point(cur_pos_x, cur_pos_y)
            outside_of_shape = not polygon.contains(point)
        if (outside_of_shape):
            break
        # Go up every other turn
        if (len(positions) % 2 == 1):
            next_pos_y = cur_position[1] + step_size
            positions.append((cur_position[0], next_pos_y))
            cur_pos_y = next_pos_y
        # Go right if not going up.
        else:
            next_pos_x = cur_position[0] + step_size
            positions.append((next_pos_x, cur_position[1]))
            cur_pos_x = next_pos_x
        num_steps_avg += 1
        j += 1
    # Print out the number of steps needed for this trial.
    # print(len(positions)-1)
    return num_steps_avg


# Helper method to handle the spiral strategy.
def move_spiral(shape, polygon, positions):
    j = 0
    cur_spiral_side = 1
    point = positions[j]
    cur_pos_x = point[0]
    cur_pos_y = point[1]
    num_steps_avg = 0
    while (1):
        cur_position = positions[j]  # Look at curent position.
        print(cur_position)
        # Based on shape - see if the current position is inside or outside of shape.
        outside_of_shape = False
        if (shape == 'RECTANGLE'):
            outside_of_shape = (cur_pos_x > width - 1) or (cur_pos_y > height - 1) or (cur_pos_x < 0) or (cur_pos_y < 0)
        elif (shape == 'TRIANGLE'):
            outside_of_shape = not is_inside_triangle(x1, y1, x2, y2, x3, y3, cur_pos_x, cur_pos_y)
        elif (shape == 'CIRCLE'):
            outside_of_shape = not is_inside_circle(center_x, center_y, radius, cur_pos_x, cur_pos_y)
        elif (shape == 'OCTAGON' or shape == 'HEXAGON'):
            point = Point(cur_pos_x, cur_pos_y)
            outside_of_shape = not polygon.contains(point)
        if (outside_of_shape):
            break
        # Going up and to the right.
        if (cur_spiral_side % 2 == 1):
            next_pos_x = cur_position[0] + cur_spiral_side
            next_pos_y = cur_position[1] + cur_spiral_side
            positions.append((next_pos_x, next_pos_y))
            cur_pos_x = next_pos_x
            cur_pos_y = next_pos_y
        # Going down and to the left.
        else:
            next_pos_x = cur_position[0] - cur_spiral_side
            next_pos_y = cur_position[1] - cur_spiral_side
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
    arg_parser.add_argument("-st", "--strategy", type = str, help = "the strategy to use", default = "RIGHT", choices = STRATEGIES)
    arg_parser.add_argument("-sh", "--shape", type = str, help = "the shape of the forest to use", default = "RECTANGLE", choices = SHAPES)
    arg_parser.add_argument("-r", "--radius", type = int, help = "the radius of the circle to use", default = 5)
    arg_parser.add_argument("-he", "--height", type = int, help = "the height of the rectangle to use", default = 5)
    arg_parser.add_argument("-w", "--width", type = int, help = "the width of the rectangle to use", default = 5)
    arg_parser.add_argument("-l", "--length", type = int, help = "the length of the side of the triangle/hexagon/octagon to use", default = 5)
    arg_parser.add_argument("-n", "--num_trials", type = int, help = "the number of trials to use for simulation", default = 1)

    args = arg_parser.parse_args()
    main(args.shape, args.strategy, args.height, args.width, args.radius, args.length, args.num_trials)