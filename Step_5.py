# ========== Step 3 ==========
# 🎯 Objective: 
# - Collect all berries and deliver them to their designated bins before reaching the goal.

# 🗺️ Map Notes:
# - Static Maps

# ----- Code -----
def move_n(n):
    for i in range(n):
        move()   
        
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def turn_around():
    turn_left()
    turn_left()

def right_picking():
    move()
    turn_right()
    for i in range(2):
        move()
        take()
    turn_around()
    move_n(2)
    while carries_object():
        put()
    turn_right()

    
def left_picking():
    move()
    turn_left()
    for i in range(2):
        move()
        take()
    turn_around()
    move_n(2)
    while carries_object():
        put()
    turn_left()
    
# Main execution
think(30)
left_picking()
right_picking()
left_picking()
right_picking()
move_n(2)