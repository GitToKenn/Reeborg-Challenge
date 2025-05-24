# ========== Step 20 ==========
# 🎯 Objective: 
# - Build walls to complete a room with a dynamic, non-square shape.

# 🗺️ Map Notes:
# - Dynamic Maps

# ----- Code -----
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
    
def turn_around():
    turn_left()
    turn_left()
    
def move_n(n):
    for i in range(n):
        move()

def check_and_build_right_wall():
    if right_is_clear():
        move() 
        if wall_on_right():
            turn_around()
            move()
            turn_left()
            build_wall()
            turn_left()
        else:
            turn_around()
            move()      
            turn_left()
            move()      
    elif front_is_clear():
        move()
    else:
        turn_left()

# Main execution
think(50)

#into position
move_n(3)
turn_right()
move()

# loop till all wall build
while not at_goal():
   check_and_build_right_wall()