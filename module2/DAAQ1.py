def tower_of_hanoi(n):
    """
    Returns the number of moves required to solve Tower of Hanoi for n disks.
    Formula: 2^n - 1
    """
    return 2 ** n - 1

# List of disk values
disk_counts = [3, 5, 10, 20]

# Print results
for n in disk_counts:
    total_moves = tower_of_hanoi(n)
    print(f"Tower of hanoi with {n} disks")
    print(f"Total number of moves required {total_moves}")
