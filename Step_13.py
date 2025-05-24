# ========== Step 13 ==========
# 🎯 Objective: 
# - Go home while avoiding randomly placed walls using dynamic roundabout logic.

# 🗺️ Map Notes:
# - Dynamic Maps

# ----- Code -----
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def roundabout():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
def roundabout2():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

# Main execution
think(30)
while not at_goal():
    if wall_in_front():
        roundabout2()
    else:
        move()