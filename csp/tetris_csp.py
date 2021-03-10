from .csp import CSP
from .tetromino_puzzle_constraint import TetrominoPuzzleConstraint
from tetris import TetrominoUtil

class TetrisCSP(CSP):

  def __init__(self, grid):
    super().__init__()
    self.update_grid(grid)
    self.add_constraint(TetrominoPuzzleConstraint(grid))

  def update_grid(self, grid):
    self._grid = grid
    self._rows = len(self._grid)
    self._cols = len(self._grid[0])

  def _build_domain(self, var):
    # Question 1, your build domain implementation goes here.

    # This method simply returns a domain suitable for the given variable where the variable in this case
    # is a TetrominoVariable. Remember the domain for a variable is all possible positions which it
    # could take. Since we are dealing with tetromino pieces don't forget that they can rotate, thus
    # creating more possible options for the variable can take.

    # Return a list of values (a domain) for said variable in the form of ((row, col), rotation) where
    # (row, col) is a possible position on the grid.

    # Helpful Functions:
    # TetrominoUtil.rotation_limit(tetromino) --> returns the maximum amount of rotations which the tetromino
    #                                             can take before resulting in its original position.
    # Tetromino.get_pruned_dimensions() --> Returns row_count, col_count of the tetromino pruned piece.
    
    raise NotImplementedError("Build Domain not defined for TetrisCSP") 
        
