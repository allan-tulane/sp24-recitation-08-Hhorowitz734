from collections import deque
from heapq import heappush, heappop 

def shortest_shortest_path(graph, source):
    """
    Params: 
      graph.....a graph represented as a dict where each key is a vertex
                and the value is a set of (vertex, weight) tuples (as in the test case)
      source....the source node
      
    Returns:
      a dict where each key is a vertex and the value is a tuple of
      (shortest path weight, shortest path number of edges). See test case for example.
    """
    
    #Initialize memoization dict
    shortestpaths = {
      vertex: (float('inf'), float('inf')) for vertex in graph
    }
    
    shortestpaths[source] = (0, 0)
    
    #We now initialize a queue (q) and use the collections functions to populate it
    q = []
    heappush(q, (0, 0, source))  # (path weight, number of edges, vertex)

    while q: #Continues until q is empty (froniter exhausted)
        
        curr_w, curr_e, curr_v = heappop(q)
        '''
        curr_w -> current weight
        curr_e -> current edges
        curr_v -> current vertex
        '''
        
        #Iterate over the neighbors of current v
        for neigh, w in graph[curr_v]:
            
            #Recalculate distance/edges
            distance = curr_w + w
            edges = curr_e + 1
            
            #Check if path to next v through v results in less weight than is precomputed
            #If it is, we simply replace it
            if (distance < shortestpaths[neigh][0]) or (distance == shortestpaths[neigh][0] and edges < shortestpaths[neigh][1]):
                shortestpaths[neigh] = (distance, edges)
                heappush(q, (distance, edges, neigh))
                
    return shortestpaths


    

    
    
def bfs_path(graph, source):
    """
    Returns:
      a dict where each key is a vertex and the value is the parent of 
      that vertex in the shortest path tree.
    """

    #We use a dictionary and a double ended queue for this function
    pdict = {source: None}
    q = deque([source])

    while q:
        v = q.popleft()

        #Iterates over neighbors (the frontier)
        #This logic works as follows:
        #1) If the neighbor is not already in the parent dict, we add it with value of the vertex
        #2) Then, we add the neighbor to the frontier
        #3) Otherwise, we just leave it as is since we already did that
        for neigh in graph[v]:
            if neigh not in pdict:
                pdict[neigh] = v
                q.append(neigh)
                
    return pdict

def get_sample_graph():
     return {'s': {'a', 'b'},
            'a': {'b'},
            'b': {'c'},
            'c': {'a', 'd'},
            'd': {}
            }


    
def get_path(parents, destination):
    """
    Returns:
      The shortest path from the source node to this destination node 
      (excluding the destination node itself). See test_get_path for an example.
    """
    
    #Initialize path string and current v
    pathstr = ""
    curr = destination

    #Go to source node and move down, prepending parent to path
    while parents[curr] is not None:
        pathstr = parents[curr] + pathstr
        curr = parents[curr]
    
    return pathstr

