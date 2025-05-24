# ========== Step 10 ==========
# 🎯 Objective: 
# - Navigate home by looping around static walls using a roundabout path.

# 🗺️ Map Notes:
# - Static Maps

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

# Main execution
think(30)
for i in range(6):
    roundabout()