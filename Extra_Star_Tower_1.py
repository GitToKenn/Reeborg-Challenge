# ========== Extra - Star Tower 1 ==========
# 🎯 Objective: 
# - Plant stars in an unknown number of columns, stopping at either an empty column or the final star column.
# - Dynamic layout (varies by number of columns and X-axis endpoint).

# 🗺️ Map Notes:
# - Dynamic Maps

# ----- Code -----
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def move_n(n):
    for i in range(n):
        move()
        
def ver_star_planting(n):
    for i in range(n):
        put("star")
        move()

def transition(n):
    if is_facing_north():
        turn_right()
        if not front_is_clear(): 
            turn_left()
            return False  
        move()            
        turn_right()
        move_n(3)       

        turn_left()
        if not front_is_clear(): 
            return False
        move()
        turn_left()
        return True
    else:
        turn_left()
        if not front_is_clear():
            turn_right()
            return False
        move()
        turn_left()
        return True
    
# Main execution
think(30)

turn_left()
while True:
    ver_star_planting(3)
    if not transition(3):
        break