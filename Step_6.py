# ========== Step 6 ==========
# 🎯 Objective: 
# - Retrieve the star from outside the enclosure, return to the starting area, and place it in the bin.

# 🗺️ Map Notes:
# - Static Maps

# ----- Code -----
# Main execution
think(100)
#take stars
move_until_wall()
turn_right()
move_n(2)
turn_left()
move_n(2)
turn_left()
move_n(2)
take()

#bring back the stars
turn_around()
move_n(2)
turn_right()
move_n(2)
turn_right()
move_n(2)
turn_left()
move()
put()