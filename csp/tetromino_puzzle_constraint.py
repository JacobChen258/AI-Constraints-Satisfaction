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
        for var in variables:
            if not assignments.get(var):
                return False
            row, col = assignments[var][0][0], assignments[var][0][1]
            rotate_count = assignments[var][1]
            tetromino = TetrominoUtil.copy(var)
            tetromino.rotate(rotate_count)
            pruned = tetromino.get_pruned_grid()
            for r in range(len(pruned)):
                for c in range(len(pruned[r])):
                    if pruned[r][c] != 0 and \
                      not MatrixUtil.valid_position(self._grid, r+row, c+col):
                        return False
        return True

    def has_future(self, csp, var, val):
        # Question 5, your has future implementation goes here.

        # Recall this method will return True iff the given variable : value combination exists within
        # a possible satisfying assignment. This means you will have to check all possible assignments
        # which have this variable : value combination to see if any such assignments satisfy the
        # Tetromino Puzzle constraint.
        unassigned_vars = csp.unassigned_variables()
        tetromino = TetrominoUtil.copy(var)
        tetromino.rotate(val[1])
        blocks = []
        tetromino_grid = tetromino.get_pruned_grid()
        dimension = tetromino.get_pruned_dimensions()
        for r in range(dimension[0]):
            for c in range(dimension[1]):
                if tetromino_grid[r][c] != 0:
                    blocks.append((val[0][0]+r, val[0][1]+c))
        for v in unassigned_vars:
            if v != var:
                cur_domain = v.active_domain()[:]
                cur_len = len(cur_domain)
                for pos, n in cur_domain:
                    temp_v = TetrominoUtil.copy(v)
                    temp_v.rotate(n)
                    temp_grid = temp_v.get_pruned_grid()
                    temp_dim = temp_v.get_pruned_dimensions()
                    for r in range(temp_dim[0]):
                        for c in range(temp_dim[1]):
                            if temp_grid[r][c] != 0 and (pos[0]+r, pos[1]+c) in blocks:
                                cur_len -= 1
                if cur_len == 0:
                    return False
        return True
