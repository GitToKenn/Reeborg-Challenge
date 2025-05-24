# ========== Step 17 ==========
# 🎯 Objective: 
# - Find goals in a fixed maze with random goal locations and starting position.

# 🗺️ Map Notes:
# - Static Maps

# ----- Code -----
def turn_right():
    turn_left()
    turn_left()
    turn_left()

# Main execution
think(30)
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()