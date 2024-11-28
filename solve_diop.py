def solve_diophantine():
    # Define the range of k and the search space for x, y, z
    k_range = range(0, 101)  # k values from 0 to 100
    search_space = range(-100, 101)  # x, y, z values between -100 and 100
    
    # Precompute cubes for efficiency
    cubes = {i: i**3 for i in search_space}
    
    # Dictionary to store results
    solutions = {}
    
    # Iterate over all values of k
    for k in k_range:
        found = False
        # Check all combinations of x, y, z
        for x in search_space:
            for y in search_space:
                # Calculate z^3 based on the equation
                z_cubed = k - cubes[x] - cubes[y]
                if z_cubed in cubes.values():  # Check if z_cubed is a valid cube
                    z = next(key for key, value in cubes.items() if value == z_cubed)
                    solutions[k] = (x, y, z)
                    found = True
                    break
            if found:
                break
        if not found:
            solutions[k] = None  # No solution found for this k
    
    return solutions

# Solve the equation and print results
if __name__ == "__main__":
    results = solve_diophantine()
    for k, solution in results.items():
        if solution:
            print(f"k={k}: x={solution[0]}, y={solution[1]}, z={solution[2]}")
        else:
            print(f"k={k}: No solution")
