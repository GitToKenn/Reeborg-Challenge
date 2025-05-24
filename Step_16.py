# ========== Step 16 ==========
# 🎯 Objective: 
# - Harvest all carrots with random positions and quantities on fixed white tiles.

# 🗺️ Map Notes:
# - Dynamic Maps

# ----- Code -----
def move_n(n):
    for i in range(n):
        move()
        
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def ver_pick(n):
    for i in range(n):
        while object_here():
            take()
        move()

def into_next_col_R():
    turn_right()
    move()
    turn_right()

def into_next_col_L():
    turn_left()
    move()
    turn_left()

def turn_around():
    turn_left()
    turn_left()

# Main execution
think(50)

#into position
move_n(2)
turn_left()
move()

#3 R L loop col picking
for i in range(3):
    ver_pick(7)
    into_next_col_R()
    ver_pick(7)
    into_next_col_L()
    
#go to bin
turn_around()
move()
while carries_object():
    put()