def optimalRoute(start, end, passengers, roads):
    """
        Function description: This function uses a Graph to store the vertices that represent the location points. Each location point is represented by a Vertex, and an Edge indicates 
        whether the driver is alone in the car or has passengers. Using Dijkstra's algorithm to determines the shortest path from beginning to end. The implementation of Dijkstra's algorithm 
        is inspired by the Malaysia FIT2004 lecture slide.
        
        Approach description: Graphs are an easy approach for illustrating collections of items and representing the connections between them. Moreover, graph can show the relationships 
        between object pairs at the most fundamental level. In this instance, a vertex represents a location point, and an edge represents the time taken to travel between two vertex points. 
        Additionally, I utilise the MinHeap to store the edges once they are discovered, since it takes O(log n) to insert and retrieve the edge in the MinHeap, where n is the total number of
        edges in the MinHeap. According to the weighted structure of the graph and it requires to be a directed graph with non-negative weights and find the shortest path between a single 
        source vertex and single target vertex, I utilise the Dijkstra approach for implementing the function on finding the route that optimises driving time.
        
        :Input:
            argv1: start (int): the location of departing
            argv2: end (int): the location of destination
            argv3: passengers (List[int]): a list of locations where there are potential passengers
            argv4: roads (List[Tuple[int, int, int, int]]): a list of roads with the corresponding travel times
        
        :Output, return or postcondition:
            return: List[int]: the list of vertices which are the optimal route to travel from start to end
        
        :Time complexity:
            O(|R| log |L|), where R is the number of roads and L is the number of vertices
        
        :Space complexity:
            Input: O(|L| + |R|), where R is the number of roads and L is the number of vertices
            Aux: O(|L| + |R|), where R is the number of roads and L is the number of vertices
    """
    maximum_vertex = 0
    for road in roads:
        maximum_vertex = max(maximum_vertex, road[0], road[1])
    
    # Create a normal_lanes_graph carpool_lanes_graph to indicate the time taken between vertices. Addtionally initialize the necessary 
    # variables.
    normal_lanes_graph = Graph(maximum_vertex + 1)
    normal_lanes_graph.add_edges(roads)
    
    for passenger in passengers:
        normal_lanes_graph.vertices[passenger].has_passenger = True
        
    carpool_lanes_graph = Graph(maximum_vertex + 1)
    carpool_lanes_graph.add_edges(roads, True)
    
    backtracking_vertex = None
    
    normal_lanes_graph.vertices[start].time = 0
    normal_lanes_graph.vertices[start].discover_node()
    
    enter_carpool_lane = False
    
    discovered = MinHeap(len(roads))
    discovered.insert((normal_lanes_graph.vertices[start].time, normal_lanes_graph.vertices[start]))

    # Perform Dijkstra's algorithm to find the shortes time from start to end.
    while len(discovered) > 0:
        a = discovered.serve()[1]
        a.visit_node()
        
        if a.id == end:
            backtracking_vertex = a
            break
        
        # To indicate the vertice has passenger. if yes, switch to carpool_lanes_graph, else continue.
        if a.has_passenger:
            carpool_lane_vertex = carpool_lanes_graph.vertices[a.id]

            # To connect the vertex in normal_lane_graph with the vertex in carpool_lane_graph.
            if not enter_carpool_lane:
                a.add_edge(Edge(a, carpool_lane_vertex, 0, 0))
                enter_carpool_lane = True
                    
            carpool_lane_vertex.previous = a.previous
            carpool_lane_vertex.time += a.time
            carpool_lane_vertex.discover_node()
                    
            discovered.insert((carpool_lane_vertex.time, carpool_lane_vertex))
            
        # Perform edge relaxation on all adjacent vertices.
        for edge in a.edges:
            b = edge.b

            # To indicate the vertice is not discovered yet. If yes, discover it, add time taken and insert to MinHeap, else continue.
            if b.discovered == False:
                b.discover_node()
                b.time = a.time + edge.c
                b.previous = a
                discovered.insert((b.time, b))
                
                # To indicate the vertex has passenger. If yes, discover it, add lesser time taken and insert to MinHeap, else continue.
                if b.using_carpool_lane:
                    b.discover_node()
                    b.time = a.time + edge.d
                    b.previous = a
                    discovered.insert((b.time, b))
            
            # To indicate the vertice is discovered but not finalise yet. If yes, compare time taken, it time taken lesser update the time, 
            # else continue.
            elif b.visited == False:
                if b.time > a.time + edge.c:
                    b.time = a.time + edge.c
                    b.previous = a
                    discovered.insert((b.time, b))
                    
                if b.using_carpool_lane and b.time > a.time + edge.d:
                    b.time = a.time + edge.d
                    b.previous = a
                    discovered.insert((b.time, b))
    
    # Use to back track the vertex to indicate which path taken lesser time to reach the destination
    backtracking_array = []
    while backtracking_vertex != None:
        backtracking_array.append(backtracking_vertex.id)
        backtracking_vertex = backtracking_vertex.previous

    backtracking_array.reverse()
    
    return backtracking_array