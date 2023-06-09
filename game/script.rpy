# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Character("Bob")
define li = Character("Lisa")

default wcolor = "#fff"
default bcolor = "#000"

# The game starts here.

label start:
    call variables   
    
    jump GAME

    
