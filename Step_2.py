# ========== Step 2 ==========
# 🎯 Objective: 
# - Pick the flower, drop it in the bin (gray flower icon), then return to the starting position.

# 🗺️ Map Notes:
# - Static Maps

# ----- Code -----
# Main execution
#harvest
move()
for _ in range(3):
    if object_here():
        take()
    move()

# drop
while carries_object():
    put()
move()