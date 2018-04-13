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

def extractCoordinates(successorStates):
    listOfCoordinates = []
    index = 0
    print "# of possibilities", index+1
    while(index < len(successorStates)):
        listOfCoordinates.append(successorStates[index][0])
        index += 1
    return listOfCoordinates

def extractCoordinatesSingle(successorStates):
    listOfCoordinates = []
    index = 0
    print "# of possibilities", index+1
    return successorStates[0]


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    from game import Directions

    #list of possible actions
    actions = []
    index = 0
    e = Directions.EAST
    n = Directions.NORTH
    s = Directions.SOUTH
    w = Directions.WEST
    #we want a list of all the nodes that we have visited already
    visitedNodes = []
    endPath = []
    flag = False
    #direction states
    # currentdirection = ""
    # nextdirection = ""
    #x and y states
    px,py = 0,0
    x,y = 0,0
    dx,dy = 0,0
    #length of successors
    successorlength = 0
    successorCoordinates = []
    #create stack for usage and our current path
    currentPath = util.Stack()
    #get our start state
    x,y = problem.getStartState()
    if(problem.isGoalState((x,y))):
        return []
    nextstates = problem.getSuccessors((x,y))
    currentstate = problem.getSuccessors((x, y))
    # print nextstates[0][1]
    visitedNodes.append(tuple((x, y)))
    # print "visted nodes", visitedNodes
    successorCoordinates = extractCoordinates(nextstates)
    print "succesors", successorCoordinates
    '''
    we call getSuccessors and get all possibilities, if the first successor is already in the visited nodes list, then we iterate to the next
    if we get to the end of the successors, then we have hit a dead end or attempted to go into a loop
    we have to backtrack in this case, which uses the stack, but the visitedNodes still retains the same values
    '''
    while(problem.isGoalState((x,y)) == False):
        # first we get the first successor coordinates
        while(index < len(successorCoordinates)):
            #check if we have already visited the node
            if(successorCoordinates[index] in visitedNodes):
                #if the node is visited, then move to next node
                index = index + 1
                # this is backtracking
                if(index == len(successorCoordinates)):
                    index = 0
                    currentstate = currentPath.pop()
                    successorCoordinates = extractCoordinatesSingle(list(currentstate))
                    x = successorCoordinates[0]
                    y = successorCoordinates[1]
                    nextstates = problem.getSuccessors((x,y))
                    successorCoordinates = extractCoordinates(nextstates)
                    index = len(successorCoordinates)-1
                    while(index>= 0):
                        if(successorCoordinates[index] in visitedNodes):
                            index -= 1
                            flag = True
                        else:
                            flag = False
                            break
                    if(flag == False):
                        currentPath.push(currentstate)
                    index = 0
            else:
                #go down next node in the path
                x = successorCoordinates[index][0]
                y = successorCoordinates[index][1]
                visitedNodes.append(tuple((x,y)))
                currentPath.push(nextstates[index])
                nextstates = problem.getSuccessors((x,y))
                successorCoordinates = extractCoordinates(nextstates)
                index = 0
                break
        #we need to backtrack
        print "X, Y", x,y
    #by the time we break out of both loops we should have a end state in the stack
    #so we just extract the directions
    while(currentPath.isEmpty() == False):
        nextstates = currentPath.pop()
        if(nextstates[1] == "North"):
            endPath.insert(0,n)
        elif(nextstates[1] == "East"):
            endPath.insert(0,e)
        elif(nextstates[1] == "South"):
            endPath.insert(0,s)
        elif(nextstates[1] == "West"):
            endPath.insert(0,w)
    return endPath
    util.raiseNotDefined()





def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    queue = util.Queue()

    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
