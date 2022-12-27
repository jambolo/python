# Pathfinding

import heapq
import itertools

uniqueId = itertools.count()


def aStar(graph, start, goal, h, neighborsOf, IMPASSABLE):
    """
    aStar - returns the shortest route in a graph from the start to the goal

    graph       - a list of the nodes in the graph
    start       - the index of the starting node
    goal        - the index of the goal node
    h           - a function that estimates the distance from a node to the goal. The function MUST return a value
                  that is never greater than the actual distance.
    neighborsOf - a function that returns a list of the indexes and costs of the neighboring nodes of a node
    IMPASSABLE  - a value greater than longest possible path
    """
    # The "open" set is implemented as a priority queue in order to efficiently find the lowest cost node in each
    # iteration. Queue elements consist of the estimated cost through the node, a unique id, and finally the node (or
    # a marker indicating that the element has been freplaced). Lowest cost elements have the highest priority. Older
    # elements of equal cost have higher priority due to the id. The id also prevents the node value from being
    # involved in the priority calculation so that the node value can be changed without invalidating the heap.
    openSet = []

    # For node n, predecessors[n] is the node immediately preceding it on the cheapest path from start
    # to n currently known.
    predecessors = [0 for i in range(0, len(graph))]

    # For node n, gScore[n] is the cost of the cheapest path from start to n currently known.
    gScore = [ IMPASSABLE for i in range(0, len(graph)) ]

    # Initially, only the start node is known.
    heapq.heappush(openSet, [h(start), next(uniqueId), start])
    gScore[start] = 0

    while len(openSet) > 0:
        # Get the next node. < 0 indicates a replaced entry
        _, _, n = openSet[0]
        heapq.heappop(openSet) # Remove the current node
        while n < 0:
            _, _, n = openSet[0]
            heapq.heappop(openSet) # Remove the current node

        # If the goal is reached, then return the path by iteratively looking up the goal's predecessors
        if n == goal:
            path = []
            while goal != start:
                path.insert(0, goal)
                goal = predecessors[goal]
            path.insert(0, start)
            return path

        neighbors = neighborsOf(n)
        for neighbor, d in neighbors:
            # distance from start to the neighbor through the current node
            tentative_gScore = gScore[n] + d

            # If this path to neighbor is better than any previous one, then save it (replacing any other instances
            # already in the queue).
            if tentative_gScore < gScore[neighbor]:
                predecessors[neighbor] = n  # Any path to the neighbor should go through n
                gScore[neighbor] = tentative_gScore
                fScore = tentative_gScore + h(neighbor)
                # Invalidate any instances of the neighbor already in the queue
                for i in openSet:
                    if i[2] == neighbor:
                        i[2] = -1
                # Add the new node to the open set
                heapq.heappush(openSet, [fScore, next(uniqueId), neighbor])

    # The open set is empty but goal was never reached. That means that there is no path from start to goal.
    return []
