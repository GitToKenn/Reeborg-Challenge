# ========== Step 18 ==========
# 🎯 Objective: 
# - Pick all carrots across a randomly sized map with carrots placed in random positions and amounts.

# 🗺️ Map Notes:
# - Dynamic Maps

# ----- Code -----
def turn_around():
    turn_left()
    turn_left()

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def move_until_wall():
    while front_is_clear():
        move()
def wall_on_left():
    turn_left()
    result = not front_is_clear()
    turn_right()
    return result
    
def go_to_start_corner():
    while not is_facing_north():
        turn_left()
    turn_around()
    while front_is_clear():
        move()
    turn_left()
    while front_is_clear():
        move()
    turn_around()

def ver_harvest():
    if object_here():
        while object_here():
            take()
    if front_is_clear():
        move()


def snake_harvest():
    count = 1
    while True:
        while object_here():
            take()    
        if wall_in_front() and wall_on_right() and wall_on_left():
            break
        elif wall_in_front() and wall_on_right():
            break
        elif wall_in_front():
            if count %2 == 1:
                turn_right()
                if not front_is_clear():
                    break
                move()
                turn_right()
            else:
                turn_left()
                if not front_is_clear():
                    break
                move()
                turn_left()
                
            count += 1
        else:
            move()

# Main execution
think(30)

go_to_start_corner()
snake_harvest()

# go to bin
go_to_start_corner()
turn_right()
move_until_wall()
while carries_object():
    put()
go_to_start_corner()
while not at_goal():
    move()