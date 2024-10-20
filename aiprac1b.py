# Code: Implement the Iterative Depth First Search Algorithm to solve the same problem.
import queue as Q 
from RMP import dict_gn 
start = "Arad" 
goal = "Bucharest" 
result = "" 
 
def DLS(city,visitedstack,startlimit,endlimit): 
    global result 
    found = 0 
    result = result + city + " " 
    visitedstack.append(city) 
    if city == goal: 
        return 1 
    if startlimit == endlimit: 
         return 0 
    for eachcity in dict_gn[city].keys(): 
        if eachcity not in visitedstack: 
              found = DLS(eachcity,visitedstack,startlimit+1,endlimit) 
        if found: 
              return found 
 
def IDDFS(city,visitedstack,endlimit): 
    global result 
    for i in range(0,endlimit): 
        print("Seaching at Limit:", i) 
        found = DLS(city,visitedstack, 0 , i) 
        if found: 
            print("Found") 
            break 
        else: 
            print("Not Found!") 
            print(result) 
            print("______") 
            result="" 
            visitedstack = []
def main(): 
    visitedstack = [] 
    IDDFS(start,visitedstack,9) 
    print("IDDFS Traversal from ", start, " to ",goal," is:")
    print(result) 
main()


#What is DFS ?
# DFS is a graph traversal algorithm that explores as far down a branch as possible before backtracking. It uses a stack (either explicitly or through recursion) to explore the graph.
# Key Steps:
# DFS starts at a selected node.
# It visits the node and marks it as visited.
# It recursively visits one of the unvisited neighbors, going deeper until there are no unvisited nodes left.
# After reaching the end of a branch, DFS backtracks to explore other unvisited branches.
# This continues until all nodes have been visited.
# Time Complexity: O(V + E), where V is the number of vertices and E is the number of edges.
# Use Case: DFS is useful for tasks like detecting cycles, pathfinding in mazes, topological sorting, and solving puzzles like the Sudoku.