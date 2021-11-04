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
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first [p 85].

    Your search algorithm needs to return a list of actions that reaches
    the goal.  Make sure to implement a graph search algorithm [Fig. 3.7].

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    node = {'state': problem.getStartState(), 'action': None, 'cost': 0}  # initial node
    if problem.isGoalState(node['state']):
        return []

    frontier = util.Stack()  # FILO
    frontier.push(node)
    explored = set()  # make sure didn't repeat

    while not problem.isGoalState(node['state']):
        node = frontier.pop()
        explored.add(node['state'])
        successors = problem.getSuccessors(node['state'])  # output state, action, cost
        for successor in successors:
            child = {'state': successor[0], 'action': successor[1], 'cost': successor[2], 'parent': node}
            if child['state'] not in explored:
                if problem.isGoalState(child['state']):
                    actions = []
                    node = child
                    while 'parent' in node:  # go back to forward node
                        actions.append(node['action'])
                        node = node['parent']
                    actions.reverse()  # reverse to first-end
                    return actions
                frontier.push(child)
    util.raiseNotDefined()


"""
recursiv impelementation
"""


# def depthFirstSearch(problem):
#     """
#     Search the deepest nodes in the search tree first [p 85].
#
#     Your search algorithm needs to return a list of actions that reaches
#     the goal.  Make sure to implement a graph search algorithm [Fig. 3.7].
#
#     To get started, you might want to try some of these simple commands to
#     understand the search problem that is being passed in:
#
#     print "Start:", problem.getStartState()
#     print "Is the start a goal?", problem.isGoalState(problem.getStartState())
#     print "Start's successors:", problem.getSuccessors(problem.getStartState())
#     """
#     # node = dict()
#     s = problem.getStartState()
#     a = []
#     DFS(problem, s, a, node) # call the DFS function, and let it upload by itself.
#     return node['action']

# def DFS(problem, state, action, node):
#     if problem.isGoalState(state):
#         return True
#
#     successors = problem.getSuccessors(state)
#     for successor in successors:
#         state = successor[0]
#         if not node.has_key(state): # make sure it isn't repeat.
#             node[state] = state
#             action.append(successor[1])
#             if DFS(problem, state, action, node) == True:
#                 return True
#             action.pop()
#
#     return False


def breadthFirstSearch(problem):
    "Search the shallowest nodes in the search tree first. [p 81]"
    node = {'state': problem.getStartState(), 'action': None, 'cost': 0}  # initial node
    if problem.isGoalState(node['state']):
        return []

    frontier = util.Queue()  # FILO
    frontier.push(node)
    explored = set()  # make sure didn't repeat

    while not problem.isGoalState(node['state']):
        node = frontier.pop()
        explored.add(node['state'])
        successors = problem.getSuccessors(node['state'])  # output state, action, cost
        for successor in successors:
            child = {'state': successor[0], 'action': successor[1], 'cost': successor[2], 'parent': node}
            if child['state'] not in explored:
                if problem.isGoalState(child['state']):
                    actions = []
                    node = child
                    while 'parent' in node:  # go back to forward node
                        actions.append(node['action'])
                        node = node['parent']
                    actions.reverse()  # reverse to first-end
                    return actions
                frontier.push(child)

    util.raiseNotDefined()


def uniformCostSearch(problem):
    "Search the node of least total cost first. "
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    "Search the node that has the lowest combined cost and heuristic first."
    "*** YOUR CODE HERE ***"
    # print "Start:", problem.getStartState()
    # print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    # print "Start's successors:", problem.getSuccessors(problem.getStartState())

    fn = 0 + heuristic(problem.getStartState(), problem)  # f(n) = g(n) + h(n)
    node = [problem.getStartState(), []]  # state and action
    explored = set()  # in order not to store same state

    frontier = util.PriorityQueue()
    frontier.push(node, fn)

    while not frontier.isEmpty():
        CurrentState, CurrentAction = frontier.pop()

        if problem.isGoalState(CurrentState):
            return CurrentAction

        if CurrentState not in explored:
            explored.add(CurrentState)

            for xy, action, cost in problem.getSuccessors(CurrentState):  # get the Successors
                fn = problem.getCostOfActions(CurrentAction + [action]) + heuristic(xy, problem)  # calculate the new fn
                frontier.push((xy, CurrentAction + [action]), fn)  # push current successor and the fn

    return []

    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
