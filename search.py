# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

"""
In search.py, you will implement generic search algorithms which are called
by Pacman agents (in searchAgents.py).
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
        Returns the start state for the search problem
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples,
        (successor, action, stepCost), where 'successor' is a
        successor to the current state, 'action' is the action
        required to get there, and 'stepCost' is the incremental
        cost of expanding to that successor
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.  The sequence must
        be composed of legal moves
        """
        util.raiseNotDefined()

def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other
    maze, the sequence of moves will be incorrect, so only use this for tinyMaze
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s,s,w,s,w,w,s,w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first
    [2nd Edition: p 75, 3rd Edition: p 87]

    Your search algorithm needs to return a list of actions that reaches
    the goal.  Make sure to implement a graph search algorithm
    [2nd Edition: Fig. 3.18, 3rd Edition: Fig 3.7].

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())

    """
    "*** YOUR CODE HERE ***"
    
    fringe = util.Stack()
    
    currentState = [problem.getStartState(), []]
    
    currentNode = None; successors = None; visitedNodes = set()

    "If current state is a goal state, we return current state"
    while(not problem.isGoalState(currentState[0])):
        
        "If current state is not a goal state, do this loop"
        "Note that if initial node is goal state, we skip this"
        (currentPosition, path) = currentState
        successors = problem.getSuccessors(currentPosition)
        for node in successors:
            "update path as we put elements on fringe"
            fringe.push((node[0], path + [node[1]]) )
        while (True):
            "If fringe is empty return failure"
            if (fringe.isEmpty()):
                return None

            "Choose lowest cost node on fringe"
            currentNode = fringe.pop()

            "If current node not in visited nodes, inser it to fringe"
            "Otherwise, repeat with next element of fringe"
            if (currentNode[0] not in visitedNodes):
                break    
        currentState = currentNode
        visitedNodes.add(currentNode[0])
    return currentState[1]


def breadthFirstSearch(problem):
    """
    Search the shallowest nodes in the search tree first.
    [2nd Edition: p 73, 3rd Edition: p 82]
    """
    "*** YOUR CODE HERE ***"
    
    "We overlay the code with the pseudocode from the lecture slides"
    
    "The only difference between this and DFS is the fringe"
    fringe = util.Queue()
    
    currentState = [problem.getStartState(), []]
    
    currentNode = None; successors = None; visitedNodes = set()

    "If current state is a goal state, we return current state"
    while(not problem.isGoalState(currentState[0])):
        
        "If current state is not a goal state, do this loop"
        "Note that if initial node is goal state, we skip this"
        (currentPosition, path) = currentState
        successors = problem.getSuccessors(currentPosition)
        for node in successors:
            "update path as we put elements on fringe"
            fringe.push((node[0], path + [node[1]]) )
        while (True):
            "If fringe is empty return failure"
            if (fringe.isEmpty()):
                return None

            "Choose lowest cost node on fringe"
            currentNode = fringe.pop()

            "If current node not in visited nodes, inser it to fringe"
            "Otherwise, repeat with next element of fringe"
            if (currentNode[0] not in visitedNodes):
                break    
        currentState = currentNode
        visitedNodes.add(currentNode[0])
    return currentState[1]
    
    #util.raiseNotDefined()

def uniformCostSearch(problem):
    "Search the node of least total cost first. "
    "*** YOUR CODE HERE ***"
    "Search the node of least total cost first. "
    "*** YOUR CODE HERE ***"

    "We overlay the code with the pseudocode from the lecture slides"
    
    "The only difference between this and DFS is the fringe and cost"
    fringe = util.PriorityQueue()
    
    currentState = [problem.getStartState(), [], 0]
    
    currentNode = None; successors = None; visitedNodes = set()

    "If current state is a goal state, we return current state"
    while(not problem.isGoalState(currentState[0])):
        
        "If current state is not a goal state, do this loop"
        "Note that if initial node is goal state, we skip this"
        (currentPosition, path, cost) = currentState
        successors = problem.getSuccessors(currentPosition)
        for node in successors:
            "Update path and cost as we put elements on fringe"
            costUpdate = cost + node[2]
            fringe.push((node[0], path + [node[1]], costUpdate), costUpdate )
        while (True):
            "If fringe is empty return failure"
            if (fringe.isEmpty()):
                return None

            "Choose lowest cost node on fringe"
            currentNode = fringe.pop()

            "If current node not in visited nodes, inser it to fringe"
            "Otherwise, repeat with next element of fringe"
            if (currentNode[0] not in visitedNodes):
                break    
        currentState = currentNode
        visitedNodes.add(currentNode[0])
    "return path to goal state"
    return currentState[1]
    
    
    #util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    "Search the node that has the lowest combined cost and heuristic first."
    "*** YOUR CODE HERE ***"
    from game import Directions
    from util import PriorityQueueWithFunction
    from game import Agent
    currentState = [problem.getStartState(), [], 0]
    fringe = util.PriorityQueueWithFunction(lambda x: x[2] + heuristic(x[0],problem))

    
    currentNode = None; successors = None; visitedNodes = set()

    "If current state is a goal state, we return current state"
    while(not problem.isGoalState(currentState[0])):
        
        "If current state is not a goal state, do this loop"
        "Note that if initial node is goal state, we skip this"
        (currentPosition, path, cost) = currentState
        successors = problem.getSuccessors(currentPosition)
        for node in successors:
            "Update path and score as we put elements on fringe"
            costUpdate = cost + node[2]
            fringe.push((node[0], path + [node[1]], costUpdate))
        while (True):
            "If fringe is empty return failure"
            if (fringe.isEmpty()):
                return None

            "Choose lowest cost node on fringe"
            currentNode = fringe.pop()

            "If current node not in visited nodes, inser it to fringe"
            "Otherwise, repeat with next element of fringe"
            if (currentNode[0] not in visitedNodes):
                break    
        currentState = currentNode
        visitedNodes.add(currentNode[0])
    "return path to goal state"
    return currentState[1]

    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
