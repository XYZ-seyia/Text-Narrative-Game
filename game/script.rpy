# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define c = Character("Classmate")
define sound1 = "audio/sound_changescene.mp3"


# The game starts here.

label start:
    play music "audio/bgmusic_hedwaytheme.mp3"
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene begin_hogwartscatsle_boat

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show s2b
    with dissolve

    # These display lines of dialogue.

    c "You've created a new Ren'Py game."

    c "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
