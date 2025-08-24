class Node:
    def __init__(self, val):
        self.val = val
        self.children = []  # List to hold any number of children

# 2. Queue Class for BFS
class Queue:
    def __init__(self):
        self.arr = [None] * 100
        self.front = -1
        self.rear = -1

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return self.rear == 99

    def enqueue(self, val):
        if self.is_full():
            print("Queue is full")
        
            return
        if self.is_empty():
            self.front = self.rear = 0
            self.arr[self.rear] = val
        else:
            self.rear += 1
        self.arr[self.rear] = val

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        temp = self.arr[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front += 1
        return temp

# 3. Stack Class for DFS
class Stack:
    def __init__(self):
        self.arr = [None] * 100
        self.top = -1

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == 99

    def push(self, val):
        if self.is_full():
            print("Stack is full")
            return
        self.top += 1
        self.arr[self.top] = val

    def pop(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        temp = self.arr[self.top]
        self.top -= 1
        return temp

# 4. BFS Function
def bfs(root):
    if root is None:
        return

    q = Queue()
    q.enqueue(root)

    while not q.is_empty():
        current = q.dequeue()
        print(current.val, end=" ")

        for child in current.children:
            q.enqueue(child)

# 5. DFS Function
def dfs(root):
    if root is None:
        return

    s = Stack()
    s.push(root)

    while not s.is_empty():
        current = s.pop()
        print(current.val, end=" ")

        # Reverse children for correct left-to-right DFS order
        for child in reversed(current.children):
            s.push(child)

# 6. Main Function (Build the same tree as in image)
if __name__ == "__main__":
    # Nodes
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n6 = Node(6)
    n7 = Node(7)
    n8 = Node(8)
    n9 = Node(9)
    n10 = Node(10)
    n11 = Node(11)
    n12 = Node(12)

    # Building the tree (your structure)
    n1.children = [n2, n7, n8]
    n2.children = [n3, n6]
    n3.children = [n4, n5]
    n8.children = [n9, n12]
    n9.children = [n10, n11]

    print("BFS Traversal: ", end="")
    bfs(n1)  # Expected: 1 2 7 8 3 6 9 12 4 5 10 11

    print("\nDFS Traversal: ", end="")
    dfs(n1)  # Example DFS: 1 2 3 4 5 6 7 8 9 10 11 12 