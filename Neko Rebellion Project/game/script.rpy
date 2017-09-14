# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
define e = Character('The big bean', color="#c8ffc8")
define narrator = nvl_narrator

init python:
    menu = nvl_menu

    style.nvl_window.background = "nvl_window.png"
    style.nvl_window.xpadding = .35
    style.nvl_window.ypadding = .40

    config.empty_window = nvl_show_core

    config.window_hide_transition = dissolve
    config.window_show_transition = dissolve


# The game starts here.
label start:

    nvl clear

    "As I reached my goal, my heart was light."
    "The climb had not tired me, in fact my body could feel little but excitement and fear."
    "A strange combination of feelings surely, but this is something I must do."

    nvl clear

    "The view from our favorite place calms me."
    "The fields spread out below me like a bright green carpet on the valley floor."
    "The mountains beyond them rise like solemn guardians, ever present, ever watchful."

    nvl clear
    
    "As I take stock of the scene before me, I breath the warm summer breeze that rushes to meet me."
    "Today is the day."
    "The day that I had always wanted but also dreaded."

    nvl clear

    "I have always considered myself someone who is well put together."
    "Who has little need for risk and could make his way in life cautiously."
    "I suppose that would explain why I couldn’t bring myself to do this earlier."

    nvl clear

    "As I wait for her I fix the buttons on my uniform."
    "More out of habit than anything else."
    "As I gaze upon the scene in front of me once again, I hear soft footsteps on the gravel behind me."

    nvl clear

    "The nervousness in my heart rises."
    "I suppose my moment is finally here."
    "The note I gave her this morning was pretty vague but I suspect she understands."

    nvl clear

    "She has always been the smarter of the two of us."
    "A smile crosses my lips as I take one final deep breath."
    "I turn to..."

    nvl clear
    
    

    

    return
