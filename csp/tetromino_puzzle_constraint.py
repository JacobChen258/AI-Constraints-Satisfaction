from .constraint import Constraint
from utils import MatrixUtil
from tetris.tetrominos import TetrominoUtil

class TetrominoPuzzleConstraint(Constraint):
  
  def __init__(self, grid):
    super().__init__()
    self._grid = MatrixUtil.copy(grid)

    # Helpful Functions:
    # MatrixUtil.copy(matrix) --> returns a copy of the matrix
    # MatrixUtil.valid_position(matrix, row, col) --> returns True iff (row, col) is a valid position within the matrix
    # TetrominoUtil.copy(tetromino) --> returns a copy of the tetromino
    # Tetromino.get_pruned_grid() --> returns a condensed version of the block grid representing a tetromino piece.
    #                                 Use this over Tetromino.get_original_grid()!
    # Tetromino.get_pruned_dimensions() --> returns row_count, col_count of the tetromino piece
    # Tetromino.rotate(rotation_amount) --> rotates the tetromino piece rotation_amount times
    
  def check(self, variables, assignments):
    # Question 2, your check solution goes here.

    # This method returns True iff the given variables and their assignments satisfy the Tetromino Puzzle
    # Constraint. Recall this constraint is that all tetromino pieces are placed onto the grid without
    # colliding with any present pieces on the grid or any other pieces to be placed.

    # As you will be manipulating Tetromino pieces here you should be manipulating _copies_ of the pieces
    # instead of the original. Same goes with the grid being worked with (self._grid).

    raise NotImplementedError("Check method for TetrominoPuzzleConstraint is not implemented")

  def has_future(self, csp, var, val):
    # Question 5, your has future implementation goes here.

    # Recall this method will return True iff the given variable : value combination exists within
    # a possible satisfying assignment. This means you will have to check all possible assignments
    # which have this variable : value combination to see if any such assignments satisfy the
    # Tetromino Puzzle constraint.
    
    raise NotImplementedError("Has Future method for TetrominoPuzzleConstraint is not implemented")
