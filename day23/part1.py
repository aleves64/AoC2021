from heapq import heappush, heappop, heapify
from collections import deque

grid = """#############
#...........#
###B#C#B#D###
  #A#D#C#A#
  #########"""

grid = grid.split("\n")
current_state = []
depth = 1
for line in grid[2:]:
    room = 2
    for c in line:
        if c in "ABCD":
            current_state.append((c, -1, depth, room))
            room += 2
    depth += 1

max_depth = 2
goals = {'A': 2,'B': 4,'C': 6,'D': 8}
costs = {'A': 1,'B': 10,'C': 100,'D': 1000}

def get_neighbors_weights(current_state):
    global goals
    global costs
    hallway = [0]*11
    rooms = [[0]*max_depth for i in range(4)]
    neighbors = []
    weights = []
    for pod in current_state:
        podtype, loc, depth, room = pod
        if loc >= 0:
            hallway[loc] = 1
        else:
            val = 1 if room == goals[podtype] else -1
            rooms[int(room/2 - 1)][depth-1] = val

    for k in range(len(current_state)):
        podtype, loc, depth, room = current_state[k]
        cost = costs[podtype]
        goal = goals[podtype]
        new_states = []
        new_weights = []

        if loc >= 0:
            goal_i = int(goal/2 - 1)
            step = 1
            if loc > goal:
                step = -1
            hallway_clear = True
            for i in range(loc+step, goal, step):
                if hallway[i] != 0:
                    hallway_clear = False
                    break
            room_clear = True
            goal_depth = max_depth
            for i in range(max_depth-1,-1,-1):
                if rooms[goal_i][i] < 0:
                    room_clear = False
                elif rooms[goal_i][i] == 1:
                    goal_depth = i
            path_clear = room_clear and hallway_clear
            if path_clear:
                new_state = (podtype, -1, goal_depth, goal)
                new_weight = cost*abs(goal-loc) + cost*goal_depth
                new_states.append(new_state)
                new_weights.append(new_weight)

        elif room >= 0:
            room_i = int(room/2 - 1)

            if room == goal and (depth == 2 or rooms[room_i][1] == 1):
                continue
            elif depth == 2 and rooms[room_i][0] != 0:
                continue

            for i in range(room, -1, -1):
                if i in goals.values():
                    continue
                elif hallway[i] != 0:
                    break
                new_states.append((podtype, i, -1, -1))
                new_weights.append(cost*(depth + abs(room - i)))

            for i in range(room, 11):
                if i in goals.values():
                    continue
                elif hallway[i] != 0:
                    break
                new_states.append((podtype, i, -1, -1))
                new_weights.append(cost*(depth + abs(room - i)))

        neighbor = list(current_state)
        for state, weight in zip(new_states, new_weights):
            neighbor[k] = state
            neighbors.append(tuple(neighbor))
            weights.append(weight)
    return neighbors, weights

def is_goal_state(current_state):
    all_OK = True
    for pod in current_state:
        podtype, loc, depth, room = pod
        goal = goals[podtype]
        if room != goal:
            all_OK = False
            break
    return all_OK

def get_paths(start):
    dist = {}
    prev = {}
    explored = {}
    queue = []
    dist[start] = 0
    end = None
    heappush(queue, (dist[start], start))

    while queue:
        nodedist, node = heappop(queue)
        explored[node] = True

        if is_goal_state(node):
            end = node
            break

        neighbors, weights = get_neighbors_weights(node)
        for i in range(len(neighbors)):
            if neighbors[i] in explored:
                continue
            alt = nodedist + weights[i]
            if not neighbors[i] in dist:
                dist[neighbors[i]] = alt
                prev[neighbors[i]] = node
                heappush(queue, (dist[neighbors[i]], neighbors[i]))
            elif alt < dist[neighbors[i]]:
                j = queue.index((dist[neighbors[i]], neighbors[i]))
                dist[neighbors[i]] = alt
                prev[neighbors[i]] = node
                queue[j] = (dist[neighbors[i]], neighbors[i])
                heapify(queue)
    return dist, prev, end

current_state = tuple(current_state)
dist, prev, end = get_paths(current_state)