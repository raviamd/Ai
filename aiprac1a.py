#Implement Breadth First Search Algorithm
import queue as Q 
from RMP import dict_gn 
start = 'Arad' 
goal = "Bucharest" 
result='' 
def BFS(city,cityq,visitedq): 
    global result 
    if city==start: 
        result = result + "" + city 
    for eachcity in dict_gn[city].keys():
        if eachcity==goal: 
            result = result + " " + eachcity
            return 
        if eachcity not in cityq.queue and eachcity not in visitedq.queue:
            cityq.put(eachcity) 
            result = result + " " + eachcity
    visitedq.put(city) 
    BFS(cityq.get(),cityq,visitedq)
def main(): 
    cityq = Q.Queue() 
    visitedq = Q.Queue() 
    BFS(start,cityq,visitedq) 
    print("BFS Traversal From ", start," to " , goal, "is :")
    print(result) 
main()

#What is BFS ? 

# BFS is a graph traversal algorithm that explores nodes level by level. Starting from a given node, BFS visits all its neighboring nodes first before moving on to the next level of neighbors.

# Key Steps:

# BFS uses a queue to track the nodes to visit.
# It starts at a selected node (root in the case of a tree).
# It enqueues the starting node and marks it as visited.
# Then, it repeatedly dequeues a node, visits its unvisited neighbors, and enqueues them.
# This process continues until all nodes have been visited or the queue is empty.