# ========== Step 3 ==========
# 🎯 Objective: 
# - Collect flowers along the path and deliver them to the finish.

# 🗺️ Map Notes:
# - Static Maps


# ----- Code -----
def move_n(n):
    for i in range(n):
        move()

def move_until_wall():
    while front_is_clear():
        move()
        
def turn_left_or_right():
    if wall_in_front() and wall_on_right():
        turn_left()
    elif wall_in_front() and right_is_clear():
        turn_right()

def pick_and_continue():
    move_until_wall()
    turn_left_or_right()
    take()

def drop_and_continue():
    move_until_wall()
    turn_left_or_right()
    put()

# Main execution   
think(30) # to fastend the trial and errors

move_until_wall()
turn_left_or_right()

pick_and_continue()
drop_and_continue()
pick_and_continue()

move_until_wall()
turn_left_or_right()

move_n(3)
put()
move()