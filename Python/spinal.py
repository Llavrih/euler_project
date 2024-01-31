def create_spiral_matrix(n):
    # Create an n x n matrix filled with 0s
    matrix = [[0] * n for _ in range(n)]

    # Starting values
    x, y = 0, 0
    dx, dy = 0, 1  # Initially moving right

    # Fill the matrix
    for i in range(n**2, 0, -1):
        matrix[x][y] = i
        # Check for the next step: within the bounds and not filled
        if not (0 <= x + dx < n and 0 <= y + dy < n and matrix[x + dx][y + dy] == 0):
            # Change direction: turn right
            dx, dy = dy, -dx
        # Move to the next cell
        x += dx
        y += dy

    return matrix


def diagonal_sum(matrix):
    suma = 0
    for i in range(0, len(matrix)):
        suma += matrix[i][i] + matrix[len(matrix) - 1 - i][i]
    return suma


# Create a 5x5 spiral matrix
spiral_matrix = create_spiral_matrix(1001)
print(diagonal_sum(spiral_matrix) - 1)
