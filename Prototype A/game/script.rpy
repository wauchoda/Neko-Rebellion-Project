# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"
image eileen happy = "eileen_happy.png"
image eileen concerned = "eileen_concerned.png"
image eileen vhappy = "eileen_vhappy.png"

image underpass day = "underpass_day.jpg"
image underpass afternoon = "underpass_afternoon.jpg"
image underpass night = "underpass_night.jpg"


# Declare characters used by this game.
define e = Character('Eileen', color="#c8ffc8")


# The game starts here.
label start:
    scene underpass day with Dissolve(1.0)

    show eileen happy
    e "You've created a new Ren'Py game."
    
    scene underpass afternoon with Dissolve(5.0)
    e "Once you add a story, pictures, and music, you can release it to the world!"
    
    scene underpass night with Dissolve(5.0)
    
    return
