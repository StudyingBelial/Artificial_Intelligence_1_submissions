
from approvedimports import *

class DepthFirstSearch(SingleMemberSearch):
    """your implementation of depth first search to extend
    the superclass SingleMemberSearch search.
    Adds  a __str__method
    Over-rides the method select_and_move_from_openlist
    to implement the algorithm
    """

    def __str__(self):
        return "depth-first"

    def select_and_move_from_openlist(self) -> CandidateSolution:
        """void in superclass
        In sub-classes should implement different algorithms
        depending on what item it picks from self.open_list
        and what it then does to the openlist

        Returns
        -------
        next working candidate (solution) taken from openlist
        """

        # create a candidate solution variable to hold the next solution
        next_soln = CandidateSolution()

        # ====> insert your pseudo-code and code below here
        if self.open_list:
            return self.open_list.pop()
        else:
            return None
        # <==== insert your pseudo-code and code above here
        return next_soln

class BreadthFirstSearch(SingleMemberSearch):
    """your implementation of depth first search to extend
    the superclass SingleMemberSearch search.
    Adds  a __str__method
    Over-rides the method select_and_move_from_openlist
    to implement the algorithm
    """

    def __str__(self):
        return "breadth-first"

    def select_and_move_from_openlist(self) -> CandidateSolution:
        """Implements the breadth-first search algorithm

        Returns
        -------
        next working candidate (solution) taken from openlist
        """
        # create a candidate solution variable to hold the next solution
        next_soln = CandidateSolution()

        # ====> insert your pseudo-code and code below here
        if self.open_list:
            return self.open_list.pop(0)
        else:
            return None
        # <==== insert your pseudo-code and code above here
        return next_soln

class BestFirstSearch(SingleMemberSearch):
    """Implementation of Best-First search."""

    def __str__(self):
        return "best-first"

    def select_and_move_from_openlist(self) -> CandidateSolution:
        """Implements Best First by finding, popping and returning member from openlist
        with best quality.

        Returns
        -------
        next working candidate (solution) taken from openlist
        """

        # create a candidate solution variable to hold the next solution
        next_soln = CandidateSolution()

        # ====> insert your pseudo-code and code below here
        if self.open_list:
            self.open_list.sort(key = lambda instance : instance.quality)
            return self.open_list.pop(0)
        else:
            return None
        # <==== insert your pseudo-code and code above here
        return next_soln

class AStarSearch(SingleMemberSearch):
    """Implementation of A-Star  search."""

    def __str__(self):
        return "A Star"

    def select_and_move_from_openlist(self) -> CandidateSolution:
        """Implements A-Star by finding, popping and returning member from openlist
        with lowest combined length+quality.

        Returns
        -------
        next working candidate (solution) taken from openlist
        """

        # create a candidate solution variable to hold the next solution
        next_soln = CandidateSolution()

        # ====> insert your pseudo-code and code below here
        if self.open_list:
            self.open_list.sort( key = lambda instance : instance.quality +  + len(instance.variable_values))
            return self.open_list.pop(0)
        else:
            return None
        # <==== insert your pseudo-code and code above here
        return next_soln
wall_colour= 0.0
hole_colour = 1.0

def create_maze_breaks_depthfirst():
    # ====> insert your code below here
    #remember to comment out any mention of show_maze() before you submit your work
    maze = Maze(mazefile="maze.txt")
    maze.contents[2][5] = wall_colour
    maze.contents[2][11] = hole_colour
    maze.contents[7][14] = hole_colour
    maze.contents[8][13] = hole_colour
    maze.contents[19][18] = hole_colour
    maze.contents[19][12] = hole_colour
    maze.save_to_txt("maze-breaks-depth.txt")
    #maze.show_maze()
    # <==== insert your code above here

#create_maze_breaks_depthfirst()

def create_maze_depth_better():
    # ====> insert your code below here
    #remember to comment out any mention of show_maze() before you submit your work
    maze = Maze(mazefile="maze.txt")
    maze.contents[8][13] = hole_colour
    maze.contents[6][17] = wall_colour
    maze.contents[10][13] = wall_colour
    maze.contents[9][14] = hole_colour
    maze.save_to_txt("maze-depth-better.txt")
    #maze.show_maze()
    # <==== insert your code above here

#create_maze_depth_better()

def create_maze_depth_better():
    # ====> insert your code below here
    #remember to comment out any mention of show_maze() before you submit your work
    maze = Maze(mazefile="maze.txt")
    maze.contents[8][13] = hole_colour
    maze.contents[6][17] = wall_colour
    maze.contents[10][13] = wall_colour
    #maze.contents[9][14] = hole_colour
    maze.save_to_txt("maze-depth-better.txt")
    #maze.show_maze()
    # <==== insert your code above here

#create_maze_depth_better()
