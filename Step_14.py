# ========== Step 14 ==========
# 🎯 Objective: 
# - Walk around the pool and return to the starting point on a dynamically sized map.

# 🗺️ Map Notes:
# - Dynamic Maps

# ----- Code -----
def move_until_wall():
    while front_is_clear():
        move()

# Main execution
think(30)
for i in range(4):
    move_until_wall()
    turn_left()