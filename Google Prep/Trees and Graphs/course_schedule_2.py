'''
There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1,
which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, 
return the ordering of courses you should take to finish all courses.

There may be multiple correct orders, you just need to return one of them. 
If it is impossible to finish all courses, return an empty array.
'''

'''
Input: 4, [[1,0],[2,0],[3,1],[3,2]]
Output: [0,1,2,3] or [0,2,1,3]
'''

import collections

WHITE = 1 # For a node that has not been process
GRAY = 2 # For a node in recursion and used for cycle detection
BLACK = 3 # For a node which is finished processing

def courseSchedule(numCourses, prerequisites):

    # Create the adj_list
    adj_list = collections.defaultdict(list)
    for dest, src in prerequisites:
        adj_list[src].append(dest)
    
    # Create global variable for cycle detection
    is_possible = True

    # Create the result or topological sorted array
    top_sorted_array = []

    # Define all nodes to be white, as they have no been traversed yet
    color = {k: WHITE for k in range(numCourses)}

    # recursive dfs function 
    def dfs(node):

        # is_possible is a global variable
        nonlocal is_possible

        # if cycle is detected, automatically return 
        if is_possible is False:
            return 
        
        # We are processing the node so change color to gray
        color[node] = GRAY
        
        # Check is node is in adj_list
        if node in adj_list:

            # Get each neighbor in the adj_list for that node
            for neighbor in adj_list[node]:

                # If the node is WHITE, dfs that node
                if color[neighbor] == WHITE:
                    dfs(neighbor)
                
                # However if the node is GRAY, then cycle is detected
                # change global is_possible variable to False
                elif color[neighbor] == GRAY:
                    is_possible = False
                
                # If node is BLACK, do nothing
        
        # After recursion is completed, change node to black
        # and add the node to our stack
        color[node] = BLACK 
        top_sorted_array.append(node)

    # For each white vertex, perform the dfs on it
    for vertex in range(numCourses):
        if color[vertex] == WHITE:
            dfs(vertex)
    
    # Return the reverse of the top_sorted_array is is_possible is true
    # else return nothing
    return top_sorted_array[::-1] if is_possible else []


def courseSchedule2(numCourses, prerequisites):
       # Prepare the graph
        adj_list = collections.defaultdict(list)
        indegree = {}
        for dest, src in prerequisites:
            adj_list[src].append(dest)
            
            # record each nodes indegree
            indegree[dest] = indegree.get(dest, 0) + 1
        
        # Queue for maintaining list of nodes that have 0 in-degree
        zero_indegree_queue = [k for k in range(numCourses) if k not in indegree]
        
        top_sorted_order = []
        
        while zero_indegree_queue:
            
            vertex = zero_indegree_queue.pop(0)
            
            top_sorted_order.append(vertex)
            
            if vertex in adj_list:
                for neighbor in adj_list[vertex]:
                    indegree[neighbor] -= 1
                    
                    # If the indegree is 0, add this to the queue
                    if indegree[neighbor] == 0:
                        zero_indegree_queue.append(neighbor)
        
        return top_sorted_order if len(top_sorted_order) == numCourses else []

numCourses = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]

print(courseSchedule(numCourses, prerequisites))
print(courseSchedule2(numCourses, prerequisites))