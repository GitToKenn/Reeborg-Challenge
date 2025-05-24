# ========== Step 7 ==========
# 🎯 Objective:
# - Plant daisies in their designated spots to match the outlined pattern.

# 🗺️ Map Notes:
# - Static Maps

# ----- Code -----
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
    
def vertical_daisy():
    for i in range(4):
        put("daisy")
        move()
    put("daisy")
    
        
def horizontal_daisy():
    turn_left()
    move()
    put("daisy")
    move()
    turn_left()
    
def transition():
    turn_right()
    move_n(2)
    turn_right()
    
def transition2():
    turn_left()
    move_n(4)
    turn_right()
    
def transition3():
    turn_around()
    move_n(4)
    turn_right()
    move_n(2)
    turn_right()

# Main execution
think(30)
#into position
move()
turn_left()
move()

#1st 1
vertical_daisy()

#transition
transition()

#1st 0
vertical_daisy()
horizontal_daisy()
vertical_daisy()
horizontal_daisy()

#transition
transition2()

#2nd 0
vertical_daisy()
horizontal_daisy()
vertical_daisy()
horizontal_daisy()


#transition
transition2()

#2nd 1
vertical_daisy()

#transition
transition3()

#3rd 0
vertical_daisy()
horizontal_daisy()
vertical_daisy()
horizontal_daisy()

#transition
transition2()

#go back home
move_n(5)