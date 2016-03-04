# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"
image eileen happy = "eileen_happy.png"
image eileen concerned = "eileen_concerned.png"
image eileen vhappy = "eileen_vhappy.png"

image underpass_day = "underpass_day.jpg"


#begin atl_with
image bg underpass daytoafternoon:
    "underpass_day" with Dissolve(5.0)
    "underpass_afternoon" with Dissolve(5.0)
    pause .5
#end atl_with

#begin atl_with
image bg underpass afternoontonight:
    "underpass_afternoon" with Dissolve(5.0)
    "underpass_night" with Dissolve(5.0)
#end atl_with

# Declare characters used by this game.
define e = Character('Eileen', color="#c8ffc8")



# The game starts here.
label start:
    scene underpass_day
    
    
    show bg underpass daytoafternoon
    #order matters, if you call bg underpass after eileen it will display over her
    show eileen happy
    e "5 Second transition to afternoon afternoon."
    e "Text here"
    
    e "We transition to night after this line"
    #order doesn't matter here because it is replacing the previous image (or so I think)
    show bg underpass afternoontonight
    
    e "1"
    e "2"
    e "Game ends after this line"
    
    
    return
