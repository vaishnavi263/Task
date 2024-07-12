def hexagon_grid(rows, cols):
    hexagon = [
        "  __ ",
        " /  \\",
        "/    \\",
        "\\    /",
        " \\__/ "
    ]

    for row in range(rows):
        for line in range(5):
            for col in range(cols):
                if line in [0, 3, 4] and col == 0:
                    print(" " * 2 * row, end="")
                if line in [1, 2] and col == 0:
                    print(" " * (2 * row + 1), end="")
                print(hexagon[line], end=" ")
            print()

# Inputs for the first and second grid
inputs_1 = (4, 7)
inputs_2 = (3, 5)

# Printing the first grid
print(f"Inputs: {inputs_1}")
hexagon_grid(*inputs_1)
print()

# Printing the second grid
print(f"Inputs: {inputs_2}")
hexagon_grid(*inputs_2)
print()
