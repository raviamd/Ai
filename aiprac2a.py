# A* Search

import queue as Q
from RMP import dict_gn
from RMP import dict_hn

start = 'Arad'
goal = 'Bucharest'
result = ' '

def get_fn(citystr):
    cities = citystr.split(",")
    gn = 0
    for ctr in range(0, len(cities) - 1):
        gn += dict_gn[cities[ctr]][cities[ctr + 1]]
    hn = dict_hn[cities[-1]]
    return hn + gn

def expand(cityq):
    global result
    tot, citystr, thiscity = cityq.get() 
    if thiscity == goal: 
        result = citystr + "::" + str(tot) 
        return 
    for cty in dict_gn[thiscity]: 
        cityq.put((get_fn(citystr + "," + cty), citystr + "," + cty, cty)) 
    expand(cityq)
    
def main(): 
    cityq = Q.PriorityQueue() 
    thiscity = start 
    cityq.put((get_fn(start), start, thiscity)) 
    expand(cityq) 
    print("The A* path with the total is: ") 
    print(result)
main()

# A Search Algorithm - Short Answer:*
# A* is a pathfinding and graph traversal algorithm that is used to find the shortest path from a start node to a goal node. It combines features of both Dijkstra’s Algorithm and Greedy Best-First Search by using a heuristic function to guide the search.
# Key Formula:
# A* uses the evaluation function:
# f(n) = g(n) + h(n)
# where:
# g(n) = cost from the start node to node n.
# h(n) = heuristic estimate of the cost from node n to the goal.
# Steps:
# Start with the initial node, and calculate f(n) for its neighbors.
# Expand the node with the lowest f(n).
# Continue expanding nodes with the lowest f(n) until the goal is reached.
# Use Case: A* is commonly used in pathfinding problems, such as in navigation systems, robotics, and games.
