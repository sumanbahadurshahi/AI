# Define Priority Queue class
class priorityQueue:
    def __init__(self):
        self.arr = []  # initialize an empty list to store (priority, value) tuples

    def isEmpty(self):
        return len(self.arr) == 0  # returns True if queue is empty

    def enqueue(self, priority, val):
        self.arr.append((priority, val))       # Add (priority, node) to queue
        self.arr.sort()  # Sort by priority (lowest priority first = greedy logic)

    def dequeue(self):
        if self.isEmpty():
            return None
        else:
            return self.arr.pop(0)  # Remove and return the node with lowest heuristic value (best guess)

# Greedy Best First Search Function
def Gfs(start, goal, graph, heuristic):
    visited = set()  # Keep track of visited nodes to avoid revisiting
    pq = priorityQueue()  # Create priority queue
    pq.enqueue(heuristic[start], start)  # Push start node with its heuristic value

    while not pq.isEmpty():  # Loop while queue is not empty
        h, current = pq.dequeue()  # Get node with smallest heuristic value
        print(current, end=" ")    # Visit and print the current node

        if current == goal:        # If goal is found, stop
            return

        visited.add(current)       # Mark current node as visited

        # Visit all neighbors of current node
        for neighbor, cost in graph[current]:  # Here, graph[current] gives list of (neighbor, cost)
            if neighbor not in visited:        # Only if not already visited
                pq.enqueue(heuristic[neighbor], neighbor)  # Enqueue with heuristic as priority

def a_starsearch(start,goal,graph,heuristic):
    visited=set()
    pq=priorityQueue()

    pq.enqueue(heuristic[start],(start,0))#push start node with its f(h),S,f(g)=0,
    while not pq.isEmpty():
        f,(current,g)=pq.dequeue()
        if current==goal:
            print("Path found:",goal)
            return
        visited.add(current)
        for neighbor, cost in graph[current]:
            if neighbor not in visited:
                g_new = g + cost               # g(n): path cost from start to neighbor
                f_new = g_new + heuristic[neighbor]  # f(n) = g(n) + h(n)
                pq.enqueue(f_new, (neighbor, g_new))  # Enqueue with updated f(n) and g(n)
# Main driver code
if __name__ == "__main__":
    # Define the graph as adjacency list with cost
    graph = {
        'S': [('A', 6), ('D', 3)],
        'A': [('B', 5), ('D', 5)],
        'B': [('C', 4), ('E', 6)],
        'C': [],
    
        'D': [('E', 2)],
        'E': [('F', 4)],
        'F': [('G', 3)],
        'G': []
    }

    # Define heuristic values (estimated cost from node to goal)
    heuristic = {
        'S': 12, 'A': 8, 'B': 7, 'C': 5,
        'D': 9, 'E': 4, 'F': 2, 'G': 0
    }

    print("Greedy Best First Search Path: ", end="")
    Gfs('S', 'G', graph, heuristic)
    print("\nA* Search Path: ", end="")
    a_starsearch('S', 'G', graph, heuristic)
