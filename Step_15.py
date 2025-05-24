# ========== Step 15 ==========
# 🎯 Objective: 
# - Build missing wall segments in a dynamic square room surrounded by impassable water.

# 🗺️ Map Notes:
# - Dynamic Maps

# ----- Code -----
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def check_wall_and_built():
    while front_is_clear():
        if not wall_on_right():
            turn_right()
            build_wall()
        else:
            move()

# Main execution
think(30)
#into position
move()
turn_right()
move()

#looping the 4 walls
while not at_goal():
    check_wall_and_built()
    turn_left()