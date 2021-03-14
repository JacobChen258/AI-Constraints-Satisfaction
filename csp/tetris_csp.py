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

        limit = 1
        shape = var.__str__()
        domain = []
        tetromino = TetrominoUtil.copy(var)
        grid = self._grid
        if shape != 'o':
            limit = TetrominoUtil.rotation_limit(var)
        for r in range(self._rows):
            for c in range(self._cols):
                for i in range(limit):
                    rotation = i
                    lst_blocks = []
                    pruned_grid = tetromino.get_pruned_grid()
                    row_count, col_count = tetromino.get_pruned_dimensions()
                    if r <= self._rows-row_count and c <= self._cols-col_count:
                        for rc in range(row_count):
                            for cc in range(col_count):
                                if pruned_grid[rc][cc] != 0:
                                    if not lst_blocks:
                                        lst_blocks.append((rc, cc))
                                    else:
                                        lst_blocks.append((rc - lst_blocks[0][0], cc - lst_blocks[0][1]))
                        lst_blocks[0] = (0, 0)
                        if grid[r][c] == 0:
                            valid = True
                            for block in lst_blocks:
                                row, col = r + block[0], c + block[1]
                                if grid[row][col] != 0:
                                    valid = False
                            if valid:
                                domain.append(((r, c), rotation))
                    tetromino.rotate()
        return domain


