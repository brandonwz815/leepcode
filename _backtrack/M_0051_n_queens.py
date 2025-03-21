# https://leetcode.com/problems/n-queens/description/
# https://grok.com/chat/d94fc76b-3122-4bdc-aff2-1b1f5dea84bc


def solveNQueens(n: int) -> list[list[str]]:
    # Initialize the board with empty cells
    board = [["." for _ in range(n)] for _ in range(n)]
    # Store the result
    result = []

    # Sets to track attacked columns and diagonals
    cols = set()
    pos_diag = set()  # (row + col)
    neg_diag = set()  # (row - col)

    def backtrack(row: int):
        # Base case: if all queens are placed
        if row == n:
            # Convert board to required string format
            result.append(["".join(row) for row in board])
            return

        # Try placing queen in each column of current row
        for col in range(n):
            # Check if this position is safe
            if (
                col not in cols
                and (row + col) not in pos_diag
                and (row - col) not in neg_diag
            ):

                # Place queen
                board[row][col] = "Q"
                cols.add(col)
                pos_diag.add(row + col)
                neg_diag.add(row - col)

                # Recurse for next row
                backtrack(row + 1)

                # Backtrack: remove queen and clear sets
                board[row][col] = "."
                cols.remove(col)
                pos_diag.remove(row + col)
                neg_diag.remove(row - col)

    # Start with first row
    backtrack(0)
    return result


# Example usage:
def test():
    # Test case for n = 4
    n = 4
    solutions = solveNQueens(n)
    for solution in solutions:
        for row in solution:
            print(row)
        print()


# Run test
test()
