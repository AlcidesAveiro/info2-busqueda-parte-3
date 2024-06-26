# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:
    """
    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print( "Start's successors:", problem.getSuccessors(problem.getStartState()))
    

    # Driver Code
    print("Following is the Depth-First Search")
    "*** YOUR CODE HERE ***"
    visited = set() # Set to keep track of visited nodes of graph.
    
    from game import Directions
    w = Directions.NORTH
    a = Directions.WEST
    s = Directions.SOUTH
    d = Directions.EAST

    
    def dfs(visited, problem, node, stack, movement):  # Function for DFS
        if problem.isGoalState(node):  # Check if the node is the goal state
            return True  # Indicate that the goal state is found

        visited.add(node)

        for successor in problem.getSuccessors(node):
            next_state, action, isOpen = successor
            if next_state not in visited:
                if action == 'South' and isOpen == 1:
                    stack.push(s)
                elif action == 'North' and isOpen == 1:
                    stack.push(w)
                elif action == 'West' and isOpen == 1:
                    stack.push(a)
                elif action == 'East' and isOpen == 1:
                    stack.push(d)

                if dfs(visited, problem, next_state, stack, movement):  # Recursively explore the next state
                    return True  # If the goal state is found, stop searching
                if not stack.isEmpty():
                    stack.pop()  # Backtrack by removing the last action from the path
        return False  # Indicate that the goal state is not found in this branch

    visited = set()
    stack = util.Stack()
    movement = []

    dfs(visited, problem, problem.getStartState(), stack, movement)
    while not stack.isEmpty():
        movement.insert(0,stack.pop())

    print(movement)
    return movement

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    visited = set()  # Set to keep track of visited nodes of graph.
    from game import Directions
    w = Directions.NORTH
    a = Directions.WEST
    s = Directions.SOUTH
    d = Directions.EAST

    movement=[]

    def bfs(visited, problem, node):  # Function for BFS
        queue = util.Queue()  # Create a queue for BFS
        queue.push((node, []))  # Initialize the queue with the starting node and an empty path
        
        while not queue.isEmpty():
            current_node, current_path = queue.pop()  # Get the current node and its corresponding path
            
            if problem.isGoalState(current_node):  # Check if the current node is the goal state
                return current_path  # Return the path to the goal state
            
            visited.add(current_node)
            
            for successor in problem.getSuccessors(current_node):
                next_state, action, isOpen = successor
                if next_state not in visited:
                    if action=='South' and isOpen==1:
                        queue.push((next_state, current_path + [s]))  
                    if action=='North' and isOpen==1:
                        queue.push((next_state, current_path + [w])) 
                    if action=='West' and isOpen==1:
                        queue.push((next_state, current_path + [a])) 
                    if action=='East' and isOpen==1:
                        queue.push((next_state, current_path + [d]))
        
        return []  # If goal state not found, return an empty list

    movement = bfs(visited, problem, problem.getStartState())
    print(movement)
    return movement
    
def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    visited = set()  # Set to keep track of visited nodes of the graph.

    movement = []

    def uniform_cost_search(visited, problem, node):  # Function for Uniform Cost Search
        queue = util.PriorityQueue()  # Create a priority queue for UCS
        queue.push((node, [], 0), 0)  # Initialize the queue with the starting node, an empty path, and cost 0
        
        while not queue.isEmpty():
            current_node, current_path, current_cost = queue.pop()  # Get the current node, its corresponding path, and cost
            
            if problem.isGoalState(current_node):  # Check if the current node is the goal state
                return current_path  # Return the path to the goal state
            
            visited.add(current_node)
            
            for successor in problem.getSuccessors(current_node):
                next_state, action, cost = successor
                if next_state not in visited:
                    total_cost = current_cost + cost  # Calculate the total cost to reach the next state
                    queue.push((next_state, current_path + [action], total_cost), total_cost)  # Add the next state to the queue with its path and cost
        
        return []  # If goal state not found, return an empty list

    movement = uniform_cost_search(visited, problem, problem.getStartState())
    print(len(movement))
    return movement

    

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    visited = set()  # Set to keep track of visited nodes of the graph.

    movement = []

    def a_star_search(visited, problem, node):  # Function for A* Search
        queue = util.PriorityQueue()  # Create a priority queue for A*
        queue.push((node, [], 0), 0)  # Initialize the queue with the starting node, an empty path, and cost 0
        
        while not queue.isEmpty():
            current_node, current_path, current_cost = queue.pop()  # Get the current node, its corresponding path, and cost
            
            if problem.isGoalState(current_node):  # Check if the current node is the goal state
                return current_path  # Return the path to the goal state
            
            visited.add(current_node)
            current_h=heuristic(current_node,problem)
            for successor in problem.getSuccessors(current_node):
                next_state, action, cost = successor
                if next_state not in visited:
                    g_cost = current_cost + cost  # Calculate the g_cost to reach the next state
                    h_cost = heuristic(next_state, problem)  # Calculate the heuristic cost from the next state to the goal
                    f_cost = g_cost + h_cost  # Calculate the f_cost (total cost)
                    # Check for inconsistency

                    if current_h > cost + h_cost:
                        print("Inconsistent heuristic at state:", next_state)



                    queue.push((next_state, current_path + [action], g_cost), f_cost)  # Add the next state to the queue with its path and cost
        
        return []  # If goal state not found, return an empty list

    movement = a_star_search(visited, problem, problem.getStartState())
    print(len(movement))
    return movement




# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch