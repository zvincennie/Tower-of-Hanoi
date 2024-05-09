# Tower-of-Hanoi
 This Python code solves the Tower of Hanoi problem recursively, printing each move and counting the total number of moves required for a given number of disks.
#Zachary Vincennie U80303351



def tower_of_hanoi(n, source, auxiliary, target):
    if n == 1:
        print(f"Move disk 1 from source {source} to destination {target}")
        return 1  # Return 1 for the single move
    count = 0
    
    # Move n-1 disks from source to auxiliary using target as the auxiliary peg
    count += tower_of_hanoi(n-1, source, target, auxiliary)
    
    # Move the nth disk from source to target
    print(f"Move disk {n} from source {source} to destination {target}")
    count += 1  # Increment the move count
    
    # Move the n-1 disks from auxiliary to target using source as the auxiliary peg
    count += tower_of_hanoi(n-1, auxiliary, source, target)
    
    return count

# Get the number of disks from the user
n = int(input("Input length of the tower: "))

# Function call to solve the Tower of Hanoi problem and get the move count
total_moves = tower_of_hanoi(n, 'A', 'B', 'C')

# Print the total move count
print(f"count = {total_moves}")








