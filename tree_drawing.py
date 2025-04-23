import turtle

# Recursive function to draw the tree
def draw_tree(t, branch_length, angle_left, angle_right, depth, reduction_factor):
    if depth == 0:
        return  # Base case: no more branches to draw
    
    # Draw the current branch
    t.forward(branch_length)
    
    # Draw the left branch
    t.left(angle_left)
    draw_tree(t, branch_length * reduction_factor, angle_left, angle_right, depth - 1, reduction_factor)
    
    # Go back to the original position
    t.right(angle_left + angle_right)
    
    # Draw the right branch
    draw_tree(t, branch_length * reduction_factor, angle_left, angle_right, depth - 1, reduction_factor)
    
    # Return to the starting position (after drawing both branches)
    t.left(angle_right)
    t.backward(branch_length)

# Main function to set up the turtle graphics and get user input
def main():
    # Get user inputs
    angle_left = float(input("Enter the left branch angle (degrees): "))
    angle_right = float(input("Enter the right branch angle (degrees): "))
    starting_branch_length = float(input("Enter the starting branch length (pixels): "))
    recursion_depth = int(input("Enter the recursion depth (try a value like 10): "))  # Suggest a smaller depth
    reduction_factor = float(input("Enter the branch length reduction factor (e.g., 0.7): "))
    
    # Set up the screen and turtle
    screen = turtle.Screen()
    screen.bgcolor("white")  # Set background color
    t = turtle.Turtle()
    t.speed(0)  # Set turtle speed to the fastest
    
    # Position the turtle
    t.left(90)  # Start facing upwards
    t.up()
    t.backward(200)  # Move back to give space for the tree
    t.down()
    
    # Call the recursive function to draw the tree
    draw_tree(t, starting_branch_length, angle_left, angle_right, recursion_depth, reduction_factor)
    
    # Keep the window open until clicked
    screen.exitonclick()

if __name__ == "__main__":
    main()
