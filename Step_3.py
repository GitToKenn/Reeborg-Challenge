# ========== Step 3 ==========
# 🎯 Objective: 
# - Walk square perimeter and return to start

# 🗺️ Map Notes:
# - Static Maps


# ----- Code -----
# Main execution
#loop 4 move till hit the wall
for i in range(4):
    while front_is_clear():
        move()
    turn_left()