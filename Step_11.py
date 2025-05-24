# ========== Step 11 ==========
# 🎯 Objective: 
# - Collect flowers from all four corners on a dynamically sized map.

# 🗺️ Map Notes:
# - Dynamic Maps

# ----- Code -----
def move_until_wall():
    while front_is_clear():
        move()

# Main execution
think(30)
for i in range(3):
    move_until_wall()
    take()
    turn_left()
move_until_wall()