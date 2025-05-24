# ========== step 9 ==========
# 🎯 Objective: 
# - Solve the same dynamic from step 8 weed path using `if` conditions for a more adaptive approach.


# 🗺️ Map Notes:
# - Dynamic Maps

# ----- Code -----
def move_n(n):
    for i in range(n):
        move()

def take_obj_on_path(n):
    for i in range(n):
        while object_here():
            take()
        move()

def turn_around():
    turn_left()
    turn_left()

# Main execution
think(30)
move_n(2)
take_obj_on_path(11)

#go to bin and home
turn_around()
move_n(12)
while carries_object():
    put()
move()