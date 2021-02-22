import random
import numpy as np
import math
from shapely.geometry.point import Point
from shapely.geometry.polygon import Polygon
import argparse

STRATEGIES = ['RIGHT', 'UP', 'ZIGZAG', 'SPIRAL']  # Strategies to test.
SHAPES = ['RECTANGLE', 'CIRCLE', 'TRIANGLE', 'OCTAGON', 'HEXAGON']  # Different shapes of forests to test.
n = 1  # Number of trials.
step_size = 1  # Step size.

def main(strategy, height, width):
    # Rectangle Shape
    # Bottom Left Corner = (0, 0). Upper right corner = (width-1, height-1)
    num_steps_avg = 0
    # Just go right
    for i in range(n):
        j = 0
        start_pos_x = random.randrange(0, width - 1)
        start_pos_y = random.randrange(0, height - 1)
        print("Starting walk at: (%d, %d)" % (start_pos_x, start_pos_y))
        cur_pos_x = start_pos_x
        cur_pos_y = start_pos_y
        positions = [(start_pos_x, start_pos_y)]
        if (strategy == 'RIGHT'):
            while (1):
                if ((cur_pos_x > width-1) or (cur_pos_y > height-1) or (cur_pos_x < 0) or (cur_pos_y < 0)):
                    break
                cur_position = positions[j]
                next_pos_x = cur_position[0] + step_size
                positions.append((next_pos_x, cur_position[1]))
                cur_pos_x = next_pos_x
                num_steps_avg += 1
                j += 1
        elif (strategy == 'UP'):
            while (1):
                if ((cur_pos_x > width-1) or (cur_pos_y > height-1) or (cur_pos_x < 0) or (cur_pos_y < 0)):
                    break
                cur_position = positions[j]
                next_pos_y = cur_position[1] + step_size
                positions.append((cur_position[1], next_pos_y))
                cur_pos_y = next_pos_y
                num_steps_avg += 1
                j += 1
        elif (strategy == 'ZIGZAG'):
            while (1):
                if ((cur_pos_x > width-1) or (cur_pos_y > height-1) or (cur_pos_x < 0) or (cur_pos_y < 0)):
                    break
                cur_position = positions[j]
                print(cur_position)
                # going up
                if (len(positions) % 2 == 1):
                    next_pos_y = cur_position[1] + step_size
                    positions.append((cur_position[0], next_pos_y))
                    cur_pos_y = next_pos_y
                # going right
                else:
                    next_pos_x = cur_position[0] + step_size
                    positions.append((next_pos_x, cur_position[1]))
                    cur_pos_x = next_pos_x
                # increment
                num_steps_avg += 1
                j += 1
        elif (strategy == 'SPIRAL'):
            cur_spiral_side = 1
            while (1):
                if ((cur_pos_x > width-1) or (cur_pos_y > height-1) or (cur_pos_x < 0) or (cur_pos_y < 0)):
                    break
                cur_position = positions[j]
                print(cur_position)
                # going up
                if (cur_spiral_side % 2 == 1):
                    next_pos_x = cur_position[0] + cur_spiral_side
                    next_pos_y = cur_position[1] + cur_spiral_side
                    positions.append((next_pos_x, next_pos_y))
                    cur_pos_x = next_pos_x
                    cur_pos_y = next_pos_y
                # going right
                else:
                    next_pos_x = cur_position[0] - cur_spiral_side
                    next_pos_y = cur_position[1] - cur_spiral_side
                    positions.append((next_pos_x, next_pos_y))
                    cur_pos_x = next_pos_x
                    cur_pos_y = next_pos_y 
                # increment
                num_steps_avg += (2 * cur_spiral_side)
                cur_spiral_side += 1
                j += 1
        # printing number of steps needed 
        print(len(positions)-1)


def circle(strategy, radius):
    # Circle Shape
    def is_inside_circle(circle_x, circle_y, rad, x, y): 
        # Compare radius of circle 
        # with distance of its center 
        # from given point 
        if ((x - circle_x) * (x - circle_x) + (y - circle_y) * (y - circle_y) <= rad * rad):
            return True
        else: 
            return False
    # Circle is always centered at (radius, radius)
    num_steps_avg = 0
    center_x = radius
    center_y = radius

    # Just go right
    for i in range(n):
        j = 0
        # random angle and radius
        alpha = np.pi * np.random.uniform(0, 2)  # in radians
        r = (np.random.uniform(0, radius)) ** 0.5
        print (r)
        # calculating coordinates
        start_pos_x = (r * np.cos(alpha)) + center_x
        start_pos_y = (r * np.sin(alpha)) + center_y
        print("Starting walk at: (%f, %f)" % (start_pos_x, start_pos_y))
        cur_pos_x = start_pos_x
        cur_pos_y = start_pos_y
        positions = [(start_pos_x, start_pos_y)]
        if (strategy == 'RIGHT'):
            while (1):
                print(positions[j])
                if (not is_inside_circle(center_x, center_y, radius, cur_pos_x, cur_pos_y)):
                    break
                cur_position = positions[j]
                next_pos_x = cur_position[0] + step_size
                positions.append((next_pos_x, cur_position[1]))
                cur_pos_x = next_pos_x
                num_steps_avg += 1
                j += 1
        elif (strategy == 'UP'):
            while (1):
                if (not is_inside_circle(center_x, center_y, radius, cur_pos_x, cur_pos_y)):
                    break
                cur_position = positions[j]
                next_pos_y = cur_position[1] + step_size
                positions.append((cur_position[1], next_pos_y))
                cur_pos_y = next_pos_y
                num_steps_avg += 1
                j += 1
        elif (strategy == 'ZIGZAG'):
            while (1):
                if (not is_inside_circle(center_x, center_y, radius, cur_pos_x, cur_pos_y)):
                    break
                cur_position = positions[j]
                print(cur_position)
                # going up
                if (len(positions) % 2 == 1):
                    next_pos_y = cur_position[1] + step_size
                    positions.append((cur_position[0], next_pos_y))
                    cur_pos_y = next_pos_y
                # going right
                else:
                    next_pos_x = cur_position[0] + step_size
                    positions.append((next_pos_x, cur_position[1]))
                    cur_pos_x = next_pos_x
                # increment
                num_steps_avg += 1
                j += 1
        elif (strategy == 'SPIRAL'):
            cur_spiral_side = 1
            while (1):
                if ((cur_pos_x > width-1) or (cur_pos_y > height-1) or (cur_pos_x < 0) or (cur_pos_y < 0)):
                    break
                cur_position = positions[j]
                print(cur_position)
                # going up
                if (cur_spiral_side % 2 == 1):
                    next_pos_x = cur_position[0] + cur_spiral_side
                    next_pos_y = cur_position[1] + cur_spiral_side
                    positions.append((next_pos_x, next_pos_y))
                    cur_pos_x = next_pos_x
                    cur_pos_y = next_pos_y
                # going right
                else:
                    next_pos_x = cur_position[0] - cur_spiral_side
                    next_pos_y = cur_position[1] - cur_spiral_side
                    positions.append((next_pos_x, next_pos_y))
                    cur_pos_x = next_pos_x
                    cur_pos_y = next_pos_y 
                # increment
                num_steps_avg += (2 * cur_spiral_side)
                cur_spiral_side += 1
                j += 1

# Triangle shape - TODO should we test different types of triangles?
def triangle(strategy, length):
    # A utility function to calculate area  
    # of triangle formed by (x1, y1),  
    # (x2, y2) and (x3, y3) 
    def area(x1, y1, x2, y2, x3, y3):
        return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0)
    # A function to check whether point P(x, y) 
    # lies inside the triangle formed by  
    # A(x1, y1), B(x2, y2) and C(x3, y3)
    def is_inside_triangle(x1, y1, x2, y2, x3, y3, x, y): 
        # Calculate area of triangle ABC 
        A = area (x1, y1, x2, y2, x3, y3) 
        # Calculate area of triangle PBC  
        A1 = area (x, y, x2, y2, x3, y3) 
        # Calculate area of triangle PAC  
        A2 = area (x1, y1, x, y, x3, y3) 
        # Calculate area of triangle PAB  
        A3 = area (x1, y1, x2, y2, x, y)
        # Check if sum of A1, A2 and A3  
        # is same as A 
        if(A == A1 + A2 + A3): 
            return True
        else: 
            return False

    def point_on_triangle(pt1, pt2, pt3):
        """
        Random point on the triangle with vertices pt1, pt2 and pt3.
        """
        s, t = sorted([random.random(), random.random()])
        return (s * pt1[0] + (t-s)*pt2[0] + (1-t)*pt3[0],
                s * pt1[1] + (t-s)*pt2[1] + (1-t)*pt3[1])

    # Triangle is formed by the points (0, 0), (length, length), and (length, 0)
    num_steps_avg = 0
    x1 = 0
    y1 = 0
    x2 = length
    y2 = length
    x3 = length
    y3 = 0

    # Just go right
    for i in range(n):
        j = 0
        # calculating coordinates
        point = point_on_triangle((x1,y1), (x2, y2), (x3, y3))
        start_pos_x = point[0]
        start_pos_y = point[1]
        print("Starting walk at: (%f, %f)" % (start_pos_x, start_pos_y))
        cur_pos_x = start_pos_x
        cur_pos_y = start_pos_y
        positions = [(start_pos_x, start_pos_y)]
        if (strategy == 'RIGHT'):
            while (1):
                print(positions[j])
                if (not is_inside_triangle(x1, y1, x2, y2, x3, y3, cur_pos_x, cur_pos_y)):
                    break
                cur_position = positions[j]
                next_pos_x = cur_position[0] + step_size
                positions.append((next_pos_x, cur_position[1]))
                cur_pos_x = next_pos_x
                num_steps_avg += 1
                j += 1
        elif (strategy == 'UP'):
            while (1):
                if (not is_inside_triangle(x1, y1, x2, y2, x3, y3, cur_pos_x, cur_pos_y)):
                    break
                cur_position = positions[j]
                next_pos_y = cur_position[1] + step_size
                positions.append((cur_position[1], next_pos_y))
                cur_pos_y = next_pos_y
                num_steps_avg += 1
                j += 1
        elif (strategy == 'ZIGZAG'):
            while (1):
                if (not is_inside_triangle(x1, y1, x2, y2, x3, y3, cur_pos_x, cur_pos_y)):
                    break
                cur_position = positions[j]
                print(cur_position)
                # going up
                if (len(positions) % 2 == 1):
                    next_pos_y = cur_position[1] + step_size
                    positions.append((cur_position[0], next_pos_y))
                    cur_pos_y = next_pos_y
                # going right
                else:
                    next_pos_x = cur_position[0] + step_size
                    positions.append((next_pos_x, cur_position[1]))
                    cur_pos_x = next_pos_x
                # increment
                num_steps_avg += 1
                j += 1
        elif (strategy == 'SPIRAL'):
            cur_spiral_side = 1
            while (1):
                if ((cur_pos_x > width-1) or (cur_pos_y > height-1) or (cur_pos_x < 0) or (cur_pos_y < 0)):
                    break
                cur_position = positions[j]
                print(cur_position)
                # going up
                if (cur_spiral_side % 2 == 1):
                    next_pos_x = cur_position[0] + cur_spiral_side
                    next_pos_y = cur_position[1] + cur_spiral_side
                    positions.append((next_pos_x, next_pos_y))
                    cur_pos_x = next_pos_x
                    cur_pos_y = next_pos_y
                # going right
                else:
                    next_pos_x = cur_position[0] - cur_spiral_side
                    next_pos_y = cur_position[1] - cur_spiral_side
                    positions.append((next_pos_x, next_pos_y))
                    cur_pos_x = next_pos_x
                    cur_pos_y = next_pos_y 
                # increment
                num_steps_avg += (2 * cur_spiral_side)
                cur_spiral_side += 1
                j += 1


# Helper function to generate a random, uniformly distributed point in polygon
def generate_random_point(polygon, xmin, xmax, ymin, ymax):
    x = np.random.uniform(xmin, xmax)
    y = np.random.uniform(ymin, ymax)
    point = Point(x, y)
    print(polygon.contains(point))
    if (polygon.contains(point)):
        return (x, y)
    else:
        generate_random_point(polygon, xmin, xmax, ymin, ymax)


# Octagon shape
def octagon(strategy, length):
    num_steps_avg = 0
    # Octagon is defined by the 8 points (0,length), (0, 2*length), (length, 0), (2*length, 0),
    # (3*length, length), (3*length, 2*length), (length, 3*length), (2*length, 3*length)
    octagon = Polygon([(0, length), (0, 2*length), (length, 0), (2*length, 0), (3*length, length), (3*length, 2*length), (length, 3*length), (2*length, 3*length)])

     # Just go right
    for i in range(n):
        j = 0
        # calculating coordinates
        point = generate_random_point(octagon, 0, 3*length, 0, 3*length)
        print(point)
        start_pos_x = point[0]
        start_pos_y = point[1]
        print("Starting walk at: (%f, %f)" % (start_pos_x, start_pos_y))
        cur_pos_x = start_pos_x
        cur_pos_y = start_pos_y
        positions = [(start_pos_x, start_pos_y)]
        if (strategy == 'RIGHT'):
            while (1):
                point = Point(cur_pos_x, cur_pos_y)
                print(positions[j])
                if (not octagon.contains(point)):
                    break
                cur_position = positions[j]
                next_pos_x = cur_position[0] + step_size
                positions.append((next_pos_x, cur_position[1]))
                cur_pos_x = next_pos_x
                num_steps_avg += 1
                j += 1
        elif (strategy == 'UP'):
            while (1):
                point = Point(cur_pos_x, cur_pos_y)
                if (not octagon.contains(point)):
                    break
                cur_position = positions[j]
                next_pos_y = cur_position[1] + step_size
                positions.append((cur_position[1], next_pos_y))
                cur_pos_y = next_pos_y
                num_steps_avg += 1
                j += 1
        elif (strategy == 'ZIGZAG'):
            while (1):
                point = Point(cur_pos_x, cur_pos_y)
                if (not octagon.contains(point)):
                    break
                cur_position = positions[j]
                print(cur_position)
                # going up
                if (len(positions) % 2 == 1):
                    next_pos_y = cur_position[1] + step_size
                    positions.append((cur_position[0], next_pos_y))
                    cur_pos_y = next_pos_y
                # going right
                else:
                    next_pos_x = cur_position[0] + step_size
                    positions.append((next_pos_x, cur_position[1]))
                    cur_pos_x = next_pos_x
                # increment
                num_steps_avg += 1
                j += 1
        elif (strategy == 'SPIRAL'):
            cur_spiral_side = 1
            while (1):
                point = Point(cur_pos_x, cur_pos_y)
                if (not octagon.contains(point)):
                    break
                cur_position = positions[j]
                print(cur_position)
                # going up
                if (cur_spiral_side % 2 == 1):
                    next_pos_x = cur_position[0] + cur_spiral_side
                    next_pos_y = cur_position[1] + cur_spiral_side
                    positions.append((next_pos_x, next_pos_y))
                    cur_pos_x = next_pos_x
                    cur_pos_y = next_pos_y
                # going right
                else:
                    next_pos_x = cur_position[0] - cur_spiral_side
                    next_pos_y = cur_position[1] - cur_spiral_side
                    positions.append((next_pos_x, next_pos_y))
                    cur_pos_x = next_pos_x
                    cur_pos_y = next_pos_y 
                # increment
                num_steps_avg += (2 * cur_spiral_side)
                cur_spiral_side += 1
                j += 1

def hexagon(strategy, length):
    # Just go right
    for i in range(n):
        j = 0
        # calculating coordinates
        point = point_on_triangle((x1,y1), (x2, y2), (x3, y3))
        start_pos_x = point[0]
        start_pos_y = point[1]
        print("Starting walk at: (%f, %f)" % (start_pos_x, start_pos_y))
        cur_pos_x = start_pos_x
        cur_pos_y = start_pos_y
        positions = [(start_pos_x, start_pos_y)]
        if (strategy == 'RIGHT'):
            while (1):
                print(positions[j])
                if (not is_inside_triangle(x1, y1, x2, y2, x3, y3, cur_pos_x, cur_pos_y)):
                    break
                cur_position = positions[j]
                next_pos_x = cur_position[0] + step_size
                positions.append((next_pos_x, cur_position[1]))
                cur_pos_x = next_pos_x
                num_steps_avg += 1
                j += 1
        elif (strategy == 'UP'):
            while (1):
                if (not is_inside_triangle(x1, y1, x2, y2, x3, y3, cur_pos_x, cur_pos_y)):
                    break
                cur_position = positions[j]
                next_pos_y = cur_position[1] + step_size
                positions.append((cur_position[1], next_pos_y))
                cur_pos_y = next_pos_y
                num_steps_avg += 1
                j += 1
        elif (strategy == 'ZIGZAG'):
            while (1):
                if (not is_inside_triangle(x1, y1, x2, y2, x3, y3, cur_pos_x, cur_pos_y)):
                    break
                cur_position = positions[j]
                print(cur_position)
                # going up
                if (len(positions) % 2 == 1):
                    next_pos_y = cur_position[1] + step_size
                    positions.append((cur_position[0], next_pos_y))
                    cur_pos_y = next_pos_y
                # going right
                else:
                    next_pos_x = cur_position[0] + step_size
                    positions.append((next_pos_x, cur_position[1]))
                    cur_pos_x = next_pos_x
                # increment
                num_steps_avg += 1
                j += 1
        elif (strategy == 'SPIRAL'):
            cur_spiral_side = 1
            while (1):
                if ((cur_pos_x > width-1) or (cur_pos_y > height-1) or (cur_pos_x < 0) or (cur_pos_y < 0)):
                    break
                cur_position = positions[j]
                print(cur_position)
                # going up
                if (cur_spiral_side % 2 == 1):
                    next_pos_x = cur_position[0] + cur_spiral_side
                    next_pos_y = cur_position[1] + cur_spiral_side
                    positions.append((next_pos_x, next_pos_y))
                    cur_pos_x = next_pos_x
                    cur_pos_y = next_pos_y
                # going right
                else:
                    next_pos_x = cur_position[0] - cur_spiral_side
                    next_pos_y = cur_position[1] - cur_spiral_side
                    positions.append((next_pos_x, next_pos_y))
                    cur_pos_x = next_pos_x
                    cur_pos_y = next_pos_y 
                # increment
                num_steps_avg += (2 * cur_spiral_side)
                cur_spiral_side += 1
                j += 1


if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser()
    # python simulation.py -st OCTAGON -l 5
    arg_parser.add_argument("-st", "--strategy", type = str, help = "the strategy to test", default = "UP", choices = STRATEGIES)
    arg_parser.add_argument("-sh", "--shape", type = str, help = "the shape to test", default = "RECTANGLE", choices = SHAPES)
    arg_parser.add_argument("-r", "--radius", type = int, help = "the radius of the circle to test", default = 5)
    arg_parser.add_argument("-he", "--height", type = int, help = "the height of the rectangle to test", default = 5)
    arg_parser.add_argument("-w", "--width", type = int, help = "the width of the rectangle to test", default = 5)
    arg_parser.add_argument("-l", "--length", type = int, help = "the length of the side of the triangle/hexagon/octagon to test", default = 5)


    args = arg_parser.parse_args()
    if (args.shape == 'CIRCLE'):
        circle(args.strategy, args.radius)
    elif (args.shape == 'RECTANGLE'):
        main(args.strategy, args.height, args.width)
    elif (args.shape == 'TRIANGLE'):
        triangle(args.strategy, args.length)
    elif (args.shape == 'OCTAGON'):
        octagon(args.strategy, args.length)
    elif (args.shape == 'HEXAGON'):
        hexagon(args.strategy, args.length)

