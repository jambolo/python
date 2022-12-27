# Pathfinding

import heapq
import itertools

uniqueId = itertools.count()


def aStar(graph, start, goal, h, neighborsOf, IMPASSABLE):
    """
    aStar   - returns the lowest cost path in a graph from the start to the goal. If the returned path is empty, then
              there is no path.

    graph                               - a list of the nodes in the graph
    start                               - the index of the starting node in the graph
    goal                                - the index of the goal node in the graph
    h(n) -> cost                        - a function that estimates the cost from node n to the goal. The function MUST
                                          return a value that is never greater than the actual cost.
    neighborsOf(n) -> [(n, cost), ...]  - a function that returns a list of the indexes and costs of the neighboring
                                          nodes of node n
    IMPASSABLE                          - a value greater than longest possible path
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
    gScore = [IMPASSABLE for i in range(0, len(graph))]

    # Initially, only the start node is known.
    heapq.heappush(openSet, [h(start), next(uniqueId), start])
    gScore[start] = 0

    while len(openSet) > 0:
        # Get the next node. < 0 indicates a replaced entry
        _, _, n = openSet[0]
        heapq.heappop(openSet)      # Remove the current node
        while n < 0:
            _, _, n = openSet[0]
            heapq.heappop(openSet)  # Remove the current node

        # If the goal is reached, then return the path by iteratively looking up the goal's predecessors
        if n == goal:
            path = []
            while goal != start:
                path.insert(0, goal)
                goal = predecessors[goal]
            path.insert(0, start)
            return path

        neighbors = neighborsOf(n)
        for neighbor, cost in neighbors:
            # cost from start to the neighbor through the current node
            tentative_gScore = gScore[n] + cost

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


def dynamicAStar(start, goal, h, neighborsOf):
    """
    dynamicAStar    - returns the lowest cost path in a graph from the start to the goal. If the returned path is
                      empty, then there no path.

    start                                   - a non-negative number representing the starting node
    goal                                    - a non-negative number representing the goal node
    h(t, n) -> cost                         - a function that estimates the cost from node n to the goal at time t. The
                                              function MUST return a value that is never greater than the actual cost.
    neighborsOf(t, n) -> [(n, cost), ...]   - a function that returns a list of the indexes and costs of the
                                              neighboring nodes of node n at time t

    This function finds a path from the start node to the goal node in a graph that is changing over time. Changes to
    the graph must be synchronized and occur at integer points in time.
    """
    # The "open" set is implemented as a priority queue in order to efficiently find the lowest cost node in each
    # iteration. Queue elements consist of the estimated cost through the node, a unique id, and finally the node (or
    # a marker indicating that the element has been freplaced). Lowest cost elements have the highest priority. Older
    # elements of equal cost have higher priority due to the id. The id also prevents the node value from being
    # involved in the priority calculation so that the node value can be changed without invalidating the heap.
    openSet = []

    # For node n, predecessors[n] is the node immediately preceding it on the cheapest path from start
    # to n currently known.
    predecessors = {}

    # For node n, gScore[n] is the cost of the cheapest path from start to n currently known.
    gScore = {}

    # Initially, only the start node is known.
    heapq.heappush(openSet, [h(0, start), 0, next(uniqueId), start])
    gScore[(0, start)] = 0

    while len(openSet) > 0:
        # Get the next node. < 0 indicates a replaced entry
        _, t0, _, n = openSet[0]
        heapq.heappop(openSet)  # Remove the current node
        while n < 0:
            _, t0, _, n = openSet[0]
            heapq.heappop(openSet)  # Remove the current node

        # If the goal is reached, then return the path by iteratively looking up the goal's predecessors
        if n == goal:
            path = []
            end = goal
            t = t0
            while t > 0:
                path.insert(0, end)
                t, end = predecessors[(t, end)]
            path.insert(0, start)
            return path

        t1 = t0 + 1
        neighbors = neighborsOf(t1, n)
        for neighbor, d in neighbors:
            # distance from start to the neighbor through the current node
            tentative_gScore = gScore[(t0, n)] + d
            # If this path to neighbor is better than any previous one, then save it (replacing any other instances
            # already in the queue).
            if (t1, neighbor) not in gScore or tentative_gScore < gScore[(t1, neighbor)]:
                predecessors[(t1, neighbor)] = (t0, n)        # Any path to the neighbor should go through n
                gScore[(t1, neighbor)] = tentative_gScore
                fScore = tentative_gScore + h(t1, neighbor)
                # Invalidate any instances of the neighbor already in the queue
                for i in openSet:
                    if i[1] == t1 and i[3] == neighbor:
                        i[3] = -1
                # Add the new node to the open set
                heapq.heappush(openSet, [fScore, t1, next(uniqueId), neighbor])

    # The open set is empty but goal was never reached. That means that there is no path from start to goal.
    return []
