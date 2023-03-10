# Test pathfinding.py

import os
import sys

this_dir = os.path.dirname(__file__)
local_src_dir = os.path.join(this_dir, '..', 'src')
sys.path.append(local_src_dir)
import pathfinding


def test_aStar():
    graph = [
        [[8, 1]], [[0, 1], [9, 1]], [[1, 1], [10, 1]], [[2, 1], [4, 1], [11, 1]], [[3, 1], [5, 1]], [[4, 1], [6, 1]], [[5, 1], [7, 1]], [[6, 1], [15, 1]],
        [[0, 1], [9, 1], [16, 1]], [[1, 1], [8, 1], [17, 1]], [[2, 1], [9, 1], [18, 1]], [[3, 1], [10, 1], [19, 1]], [[4, 1], [11, 1], [13, 1], [20, 1]], [[5, 1], [12, 1], [14, 1]], [[6, 1], [13, 1], [15, 1], [22, 1]], [[7, 1], [23, 1]],
        [[8, 1], [24, 1]], [[9, 1], [16, 1], [18, 1]], [[10, 1], [17, 1], [26, 1]], [[11, 1], [18, 1], [27, 1]], [[12, 1], [19, 1], [21, 1], [28, 1]], [[13, 1], [20, 1], [22, 1], [29, 1]], [[14, 1], [23, 1], [30, 1]], [[15, 1], [31, 1]],
        [[16, 1], [32, 1]], [[17, 1], [24, 1], [26, 1], [33, 1]], [[18, 1], [34, 1]], [[19, 1], [26, 1], [28, 1], [35, 1]], [[27, 1], [29, 1], [36, 1]], [[28, 1], [30, 1], [37, 1]], [[22, 1], [29, 1], [31, 1], [38, 1]], [[23, 1], [39, 1]],
        [[24, 1], [33, 1]], [[32, 1]], [[26, 1], [33, 1], [35, 1]], [[34, 1], [36, 1]], [[35, 1], [37, 1]], [[36, 1], [38, 1]], [[37, 1], [39, 1]], [[31, 1], [38, 1]]
    ]
    expected = [0, 8, 9, 17, 18, 26, 34, 35, 36, 37, 38, 39, 31, 23, 15, 7, 6, 5, 4, 3, 11, 19, 27, 28, 29, 30, 22, 14, 13, 12, 20, 21]

    WIDTH = 8
    HEIGHT = 5
    START = 0
    END = 21
    IMPASSABLE = 2 * WIDTH * HEIGHT + 1

    def h(s):
        sx = s % WIDTH
        sy = s // WIDTH
        ex = END % WIDTH
        ey = END // WIDTH
        return abs(ex - sx) + abs(ey - sy)

    def neighborsOf(s):
        return graph[s]

    result = pathfinding.aStar(graph, START, END, h, neighborsOf, IMPASSABLE)
    assert result == expected


def test_dynamicAStar():

    START_INDEX = 0
    GOAL_INDEX = 25
    WIDTH = 6
    HEIGHT = 4
    graphs = [
        [[(0, 1), (1, 1)], [((7, 1), (1, 1)), ((0, 1), (1, 1))], [(3, 1)], [(3, 1), (9, 1)], [(3, 1), (10, 1)], [], [], [(7, 1)], [(7, 1), (9, 1)], [(9, 1), (3, 1), (10, 1), (15, 1)], [(10, 1), (9, 1)], [(10, 1)], [], [(7, 1)], [(15, 1)], [(15, 1), (9, 1)], [(10, 1), (15, 1)], [], [], [], [], [(15, 1)], [], [], [(25, 1)], [(25, 1)]],
        [[(0, 1), (1, 1)], [(1, 1), (0, 1)], [(1, 1), (8, 1)], [(4, 1), (9, 1)], [(4, 1)], [(4, 1), (6, 1)], [(6, 1), (12, 1)], [(1, 1), (8, 1)], [(8, 1), (9, 1)], [(9, 1), (8, 1), (15, 1)], [(4, 1), (9, 1)], [(12, 1)], [(12, 1), (6, 1), (18, 1)], [], [(8, 1), (15, 1)], [(15, 1), (9, 1), (21, 1)], [(15, 1), (22, 1)], [(18, 1)], [(18, 1), (12, 1)], [], [(21, 1)], [(21, 1), (15, 1), (22, 1)], [(22, 1), (21, 1)], [(22, 1)], [(18, 1), (25, 1)], [(25, 1)]],
        [[(0, 1), (1, 1)], [(1, 1), (7, 1), (0, 1)], [(1, 1)], [], [(5, 1)], [(5, 1), (6, 1)], [(6, 1), (5, 1)], [(7, 1), (1, 1), (13, 1)], [(7, 1)], [], [(16, 1)], [(5, 1)], [(6, 1)], [(13, 1), (7, 1), (19, 1)], [(13, 1)], [(16, 1), (21, 1)], [(16, 1), (22, 1)], [(16, 1)], [(24, 1)], [(19, 1), (13, 1)], [(19, 1), (21, 1)], [(21, 1), (22, 1)], [(22, 1), (16, 1), (21, 1)], [(22, 1), (24, 1)], [(24, 1), (25, 1)], [(25, 1), (24, 1)]],
        [[(0, 1)], [(7, 1), (0, 1)], [], [], [(10, 1)], [(6, 1)], [(6, 1), (12, 1)], [(7, 1)], [(7, 1)], [(10, 1)], [(10, 1)], [(10, 1), (12, 1), (17, 1)], [(12, 1), (6, 1), (18, 1)], [(7, 1), (19, 1)], [(20, 1)], [], [(10, 1), (17, 1)], [(17, 1), (18, 1), (23, 1)], [(18, 1), (12, 1), (17, 1), (24, 1)], [(19, 1), (20, 1)], [(20, 1), (19, 1)], [(20, 1)], [(23, 1)], [(23, 1), (17, 1), (24, 1)], [(24, 1), (18, 1), (23, 1), (25, 1)], [(25, 1), (24, 1)]],
        [[(0, 1), (1, 1)], [(1, 1), (0, 1)], [(1, 1), (3, 1)], [(3, 1), (4, 1), (9, 1)], [(4, 1), (3, 1)], [(4, 1), (11, 1)], [(12, 1)], [(1, 1)], [(9, 1)], [(9, 1), (3, 1), (15, 1)], [(4, 1), (9, 1), (11, 1)], [(11, 1), (12, 1)], [(12, 1), (11, 1), (18, 1)], [(19, 1)], [(15, 1)], [(15, 1), (9, 1)], [(15, 1)], [(11, 1), (18, 1)], [(18, 1), (12, 1), (24, 1)], [(19, 1)], [(19, 1)], [(15, 1)], [], [(24, 1)], [(24, 1), (18, 1), (25, 1)], [(25, 1), (24, 1)]],
        [[(0, 1)], [(2, 1), (0, 1)], [(2, 1), (8, 1)], [(2, 1), (4, 1)], [(4, 1), (10, 1)], [(4, 1), (11, 1)], [], [(8, 1), (13, 1)], [(8, 1), (2, 1)], [(8, 1), (10, 1)], [(10, 1), (4, 1), (11, 1)], [(11, 1), (10, 1)], [(11, 1)], [(13, 1), (19, 1)], [(8, 1), (13, 1)], [(21, 1)], [(10, 1), (22, 1)], [(11, 1)], [(24, 1)], [(19, 1), (13, 1)], [(19, 1), (21, 1)], [(21, 1), (22, 1)], [(22, 1), (21, 1)], [(22, 1), (24, 1)], [(24, 1), (25, 1)], [(25, 1), (24, 1)]],
        [[(0, 1)], [(7, 1), (0, 1)], [(3, 1)], [(3, 1)], [(3, 1), (5, 1)], [(5, 1)], [(5, 1)], [(7, 1)], [(7, 1), (14, 1)], [(3, 1), (15, 1)], [], [(5, 1)], [], [(7, 1), (14, 1)], [(14, 1), (15, 1), (20, 1)], [(15, 1), (14, 1), (21, 1)], [(15, 1), (22, 1)], [(23, 1)], [], [(20, 1)], [(20, 1), (14, 1), (21, 1)], [(21, 1), (15, 1), (20, 1), (22, 1)], [(22, 1), (21, 1), (23, 1)], [(23, 1), (22, 1)], [(23, 1), (25, 1)], [(25, 1)]],
        [[(0, 1), (1, 1)], [(1, 1), (0, 1)], [(1, 1)], [(9, 1)], [], [(6, 1)], [(6, 1), (12, 1)], [(1, 1)], [(9, 1)], [(9, 1)], [(9, 1)], [(12, 1)], [(12, 1), (6, 1), (18, 1)], [], [(20, 1)], [(9, 1), (21, 1)], [(22, 1)], [(18, 1), (23, 1)], [(18, 1), (12, 1)], [(20, 1)], [(20, 1), (21, 1)], [(21, 1), (20, 1), (22, 1)], [(22, 1), (21, 1), (23, 1)], [(23, 1), (22, 1)], [(18, 1), (23, 1), (25, 1)], [(25, 1)]],
        [[(0, 1), (1, 1)], [(1, 1), (7, 1), (0, 1)], [(1, 1), (8, 1)], [], [], [(6, 1), (11, 1)], [(6, 1)], [(7, 1), (1, 1), (8, 1), (13, 1)], [(8, 1), (7, 1)], [(8, 1)], [(11, 1), (16, 1)], [(11, 1), (17, 1)], [(6, 1), (11, 1)], [(13, 1), (7, 1), (19, 1)], [(8, 1), (13, 1)], [(16, 1)], [(16, 1), (17, 1)], [(17, 1), (11, 1), (16, 1)], [(17, 1), (24, 1)], [(19, 1), (13, 1)], [(19, 1)], [], [(16, 1)], [(17, 1), (24, 1)], [(24, 1), (25, 1)], [(25, 1), (24, 1)]],
        [[(0, 1)], [(2, 1), (7, 1), (0, 1)], [(2, 1)], [(2, 1)], [(10, 1)], [(6, 1)], [(6, 1), (12, 1)], [(7, 1)], [(2, 1), (7, 1)], [(10, 1)], [(10, 1)], [(10, 1), (12, 1)], [(12, 1), (6, 1), (18, 1)], [(7, 1), (19, 1)], [], [], [(10, 1)], [(18, 1)], [(18, 1), (12, 1), (24, 1)], [(19, 1)], [(19, 1)], [], [], [(24, 1)], [(24, 1), (18, 1), (25, 1)], [(25, 1), (24, 1)]],
        [[(0, 1), (1, 1)], [(1, 1), (0, 1)], [(1, 1), (3, 1)], [(3, 1), (4, 1)], [(4, 1), (3, 1)], [(4, 1)], [(12, 1)], [(1, 1)], [], [(3, 1), (15, 1)], [(4, 1)], [(12, 1)], [(12, 1), (18, 1)], [(19, 1)], [(15, 1), (20, 1)], [(15, 1)], [(15, 1)], [(18, 1), (23, 1)], [(18, 1), (12, 1), (24, 1)], [(19, 1), (20, 1)], [(20, 1), (19, 1)], [(15, 1), (20, 1)], [(23, 1)], [(23, 1), (24, 1)], [(24, 1), (18, 1), (23, 1), (25, 1)], [(25, 1), (24, 1)]],
        [[(0, 1)], [(0, 1)], [(3, 1)], [(3, 1)], [(3, 1), (10, 1)], [], [], [(13, 1)], [(14, 1)], [(3, 1), (10, 1)], [(10, 1), (16, 1)], [(10, 1)], [], [(13, 1), (14, 1), (19, 1)], [(14, 1), (13, 1)], [(14, 1), (16, 1), (21, 1)], [(16, 1), (10, 1), (22, 1)], [(16, 1)], [(24, 1)], [(19, 1), (13, 1)], [(14, 1), (19, 1), (21, 1)], [(21, 1), (22, 1)], [(22, 1), (16, 1), (21, 1)], [(22, 1), (24, 1)], [(24, 1), (25, 1)], [(25, 1), (24, 1)]],
        [[(0, 1)], [(7, 1), (0, 1)], [(3, 1)], [(3, 1), (9, 1)], [(3, 1), (10, 1)], [], [], [(7, 1)], [(7, 1), (9, 1)], [(9, 1), (3, 1), (10, 1), (15, 1)], [(10, 1), (9, 1)], [(10, 1)], [], [(7, 1)], [(15, 1)], [(15, 1), (9, 1)], [(10, 1), (15, 1)], [], [], [], [], [(15, 1)], [], [], [(25, 1)], [(25, 1)]],
        [[(0, 1), (1, 1)], [(1, 1), (0, 1)], [(1, 1), (8, 1)], [(4, 1), (9, 1)], [(4, 1)], [(4, 1), (6, 1)], [(6, 1), (12, 1)], [(1, 1), (8, 1)], [(8, 1), (9, 1)], [(9, 1), (8, 1), (15, 1)], [(4, 1), (9, 1)], [(12, 1)], [(12, 1), (6, 1), (18, 1)], [], [(8, 1), (15, 1)], [(15, 1), (9, 1), (21, 1)], [(15, 1), (22, 1)], [(18, 1)], [(18, 1), (12, 1)], [], [(21, 1)], [(21, 1), (15, 1), (22, 1)], [(22, 1), (21, 1)], [(22, 1)], [(18, 1), (25, 1)], [(25, 1)]],
        [[(0, 1), (1, 1)], [(1, 1), (7, 1), (0, 1)], [(1, 1)], [], [(5, 1)], [(5, 1), (6, 1)], [(6, 1), (5, 1)], [(7, 1), (1, 1), (13, 1)], [(7, 1)], [], [(16, 1)], [(5, 1)], [(6, 1)], [(13, 1), (7, 1), (19, 1)], [(13, 1)], [(16, 1), (21, 1)], [(16, 1), (22, 1)], [(16, 1)], [(24, 1)], [(19, 1), (13, 1)], [(19, 1), (21, 1)], [(21, 1), (22, 1)], [(22, 1), (16, 1), (21, 1)], [(22, 1), (24, 1)], [(24, 1), (25, 1)], [(25, 1), (24, 1)]],
        [[(0, 1)], [(7, 1), (0, 1)], [], [], [(10, 1)], [(6, 1)], [(6, 1), (12, 1)], [(7, 1)], [(7, 1)], [(10, 1)], [(10, 1)], [(10, 1), (12, 1), (17, 1)], [(12, 1), (6, 1), (18, 1)], [(7, 1), (19, 1)], [(20, 1)], [], [(10, 1), (17, 1)], [(17, 1), (18, 1), (23, 1)], [(18, 1), (12, 1), (17, 1), (24, 1)], [(19, 1), (20, 1)], [(20, 1), (19, 1)], [(20, 1)], [(23, 1)], [(23, 1), (17, 1), (24, 1)], [(24, 1), (18, 1), (23, 1), (25, 1)], [(25, 1), (24, 1)]],
        [[(0, 1), (1, 1)], [(1, 1), (0, 1)], [(1, 1), (3, 1)], [(3, 1), (4, 1), (9, 1)], [(4, 1), (3, 1)], [(4, 1), (11, 1)], [(12, 1)], [(1, 1)], [(9, 1)], [(9, 1), (3, 1), (15, 1)], [(4, 1), (9, 1), (11, 1)], [(11, 1), (12, 1)], [(12, 1), (11, 1), (18, 1)], [(19, 1)], [(15, 1)], [(15, 1), (9, 1)], [(15, 1)], [(11, 1), (18, 1)], [(18, 1), (12, 1), (24, 1)], [(19, 1)], [(19, 1)], [(15, 1)], [], [(24, 1)], [(24, 1), (18, 1), (25, 1)], [(25, 1), (24, 1)]],
        [[(0, 1)], [(2, 1), (0, 1)], [(2, 1), (8, 1)], [(2, 1), (4, 1)], [(4, 1), (10, 1)], [(4, 1), (11, 1)], [], [(8, 1), (13, 1)], [(8, 1), (2, 1)], [(8, 1), (10, 1)], [(10, 1), (4, 1), (11, 1)], [(11, 1), (10, 1)], [(11, 1)], [(13, 1), (19, 1)], [(8, 1), (13, 1)], [(21, 1)], [(10, 1), (22, 1)], [(11, 1)], [(24, 1)], [(19, 1), (13, 1)], [(19, 1), (21, 1)], [(21, 1), (22, 1)], [(22, 1), (21, 1)], [(22, 1), (24, 1)], [(24, 1), (25, 1)], [(25, 1), (24, 1)]],
        [[(0, 1)], [(7, 1), (0, 1)], [(3, 1)], [(3, 1)], [(3, 1), (5, 1)], [(5, 1)], [(5, 1)], [(7, 1)], [(7, 1), (14, 1)], [(3, 1), (15, 1)], [], [(5, 1)], [], [(7, 1), (14, 1)], [(14, 1), (15, 1), (20, 1)], [(15, 1), (14, 1), (21, 1)], [(15, 1), (22, 1)], [(23, 1)], [], [(20, 1)], [(20, 1), (14, 1), (21, 1)], [(21, 1), (15, 1), (20, 1), (22, 1)], [(22, 1), (21, 1), (23, 1)], [(23, 1), (22, 1)], [(23, 1), (25, 1)], [(25, 1)]],
        [[(0, 1), (1, 1)], [(1, 1), (0, 1)], [(1, 1)], [(9, 1)], [], [(6, 1)], [(6, 1), (12, 1)], [(1, 1)], [(9, 1)], [(9, 1)], [(9, 1)], [(12, 1)], [(12, 1), (6, 1), (18, 1)], [], [(20, 1)], [(9, 1), (21, 1)], [(22, 1)], [(18, 1), (23, 1)], [(18, 1), (12, 1)], [(20, 1)], [(20, 1), (21, 1)], [(21, 1), (20, 1), (22, 1)], [(22, 1), (21, 1), (23, 1)], [(23, 1), (22, 1)], [(18, 1), (23, 1), (25, 1)], [(25, 1)]]
    ]

    expected = [0, 1, 7, 7, 1, 2, 3, 9, 8, 2, 3, 3, 9, 15, 16, 17, 18, 24, 25]

    def h(t, i):
        if i == START_INDEX:
            cost = WIDTH + HEIGHT
        elif i == GOAL_INDEX:
            cost = 0
        else:
            r = i // WIDTH
            c = i % WIDTH
            cost = (WIDTH - 1 - c) + (HEIGHT - 1 - r) + 1
        return cost

    def neighborsOf(t, i):
        return graphs[t][i]

    path = pathfinding.dynamicAStar(START_INDEX, GOAL_INDEX, h, neighborsOf)
    assert path == expected
