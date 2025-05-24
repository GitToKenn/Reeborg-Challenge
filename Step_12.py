# ========== Step 12 ==========
# 🎯 Objective: 
# - Collect apples with varying quantities, drop them in the bin, and return home.

# 🗺️ Map Notes:
# - Dynamic Maps

# ----- Code -----
def move_until_wall():
    while front_is_clear():
        move()
        
def move_n(n):
    for i in range(n):
        move()
        
def turn_around():
    turn_left()
    turn_left()
    
def turn_right():
    turn_left()
    turn_left()
    turn_left()

# Main execution
think(30)
#take apples
move_until_wall()
turn_left()
move_until_wall()
while object_here():
    take()
    
#go to bin
turn_around()
move_n(3)
turn_left()
move_n(4)
turn_left()
move_n(4)

#put the apples
while carries_object():
    put()

#go back home
turn_around()
move_n(4)
turn_right()
move_n(5)
turn_left()
move_n(2)
