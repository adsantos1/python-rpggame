# Imports
from random import shuffle
from time import sleep


# Variables with paragraphs/text
game_intro = """After Boris Johnson admission tier 3 lockdown, you decide to fly your private plane and head down to the deep jungle of India for an adventure.
After wandering the jungle for 3 days, you stumble upon an old abandoned temple.
"""

room_1_intro = """You take a step inside. A few candles flicker but you see no signs of life. 'Hello!?' you cry, but the only reply you hear is your own echo.
To either side of you are two unremarkable doors; neither one calls out to you, yet you have an urge to go deeper into the temple.
"""

room_1_options = """- go left
- go right"""

room_1_death = """'Wrong!' you hear. You feel an ancient energy take a hold of you and squeeze with immeasurable force.
Light fades.
"""

room_1_riddle = """In Harry Potter this animal Represents the house of Slytherin. In The Jungle Book there’s one called Kaa.
They have a forked tongue and shed their skin. What animal is it?
"""

room_1_mystery = """Who said float like a butterfly, sting like a bee?
"""

room_2_intro = """This room doesn't seem to have much light, but the sunlight from a hole in the temple is shining on a golden door to the left.
There's also a vase and a door to the right.
"""

room_3_intro = """A foul stench fills the air. You walk past the door and notice
a spooky figure staring back at you with beady eyes. A wrinkly, aged face, disheveled gray hair, and a crooked back...
'Goodness!.. Oh its just me'
Only a rusty mirror leaning suspicously on the wall.
Do you:"""

room_4_intro = """This room is covered with a golden infrastucture; I wonder what could possibly be in here?
Looking down, there seems to be a golden door. There's also another vase and a cane within reach.
"""

room_5_intro = """In a jovial mood you trot past the entrance and into the dark room...
'WOAHH!'
You almost fall into a bottomless pit. Carelessness results in death!
beyond the pit the path continues.
Do you:"""

room_5_options = """- go forward
- go back"""

room_6_intro = """As you struggle to open the rusty doors, a large looming figure approaches from within.
A giant APE!
'GRRR!'
With a menacing glare, the ape pounds its chest furiously and rushes towards you.
'Not good!'
Do you:"""

room_6_options = """- go back
- fight"""

treasure_room_intro = """Majestic doors covered in mysterious ancient glyphs and...
Banana symbols are ahead. Hmm, what could possibly be waiting for you?
'Gulp!'
As you open the doors, the path lights up as if multiple lanterns were lit.
GOLD! LOTS OF GOLD! TREASURE...
And an oddly large banana lay in an unassuming corner.
Booming footsteps can be heard approaching quickly.
Do you:"""

treasure_room_options = """- collect the gold
- collect the banana
- eat the banana"""

winning_paragraph = """You offer the ape the banana.
The ape is delighted!
As a token of appreciation, he helps you collect the gold.
You're rich!
"""

monkey_defeat = """WASTED - The cane arts have failed you! The frenzied ape has sent you flying with a slap.
"""

banana_eaten = """WASTED - The ape has gone berserk! A flurry of fists hammers you into the floor,
forever decorating the temple grounds.
"""

invalid_choice = """That's not a valid choice.
"""

game_credits = """Credits:

Programmers:
Anaam Abdi
Arnold Santos
Mihnea Clejan
Mohammed Sharah

Special thanks to:
Leona So
Michael Clare
Paula Wilson"""

# ASCII Art
temple_ascii = """
               )\\         O_._._._A_._._._O         /(
                \\`--.___,'=================`.___,--'/
                 \\`--._.__                 __._,--'/
                   \\  ,. l`~~~~~~~~~~~~~~~'l ,.  /
       __            \\||(_)!_!_!_.-._!_!_!(_)||/            __
       \\\\`-.__        ||_|____!!_|;|_!!____|_||        __,-'//
        \\\\    `==---='-----------'='-----------`=---=='    //
        | `--.                                         ,--' |
         \\  ,.`~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~',.  /
           \\||  ____,-------._,-------._,-------.____  ||/
            ||\\|___!`======="!`======="!`======="!___|/||
            || |---||--------||-| | |-!!--------||---| ||
  __O_____O_ll_lO_____O_____O|| |'|'| ||O_____O_____Ol_ll_O_____O__
  o H o o H o o H o o H o o |-----------| o o H o o H o o H o o H o
 ___H_____H_____H_____H____O =========== O____H_____H_____H_____H___
                          /|=============|\\
()______()______()______() '==== +-+ ====' ()______()______()______()
||{_}{_}||{_}{_}||{_}{_}/| ===== |_| ===== |\\{_}{_}||{_}{_}||{_}{_}||
||      ||      ||     / |==== s(   )s ====| \\     ||      ||      ||
======================()  =================  ()======================
----------------------/| ------------------- |\\----------------------
                     / |---------------------| \\
-'--'--'           ()  '---------------------'  ()
                   /| ------------------------- |\\    --'--'--'
       --'--'     / |---------------------------| \\
"""


temple_door_ascii = """
.._|      | `-.  | `.  -_-_ _-_  _-  _- -_ -  .'|   |.'|     |  _..
   `-.._  |    |`!  |`.  -_ -__ -_ _- _-_-  .'  |.;'   |   _.!-'|
      | `-!._  |  `;!  ;. _______________ ,'| .-' |   _!.i'     |
..__  |     |`-!._ | `.| |_______________||."'|  _!.;'   |     _|..
   |``"..__ |    |`";.| i|_|MMMMMMMMMMM|_|'| _!-|   |   _|..-|'
   |      |``--..|_ | `;!|l|MMoMMMMoMMM|1|.'j   |_..!-'|     |
   |      |    |   |`-,!_|_|MMMMP'YMMMM|_||.!-;'  |    |     |
___|______|____!.,.!,.!,!|d|MMMo * loMM|p|,!,.!.,.!..__|_____|_____
      |     |    |  |  | |_|MMMMb,dMMMM|_|| |   |   |    |      |
      |     |    |..!-;'i|r|MPYMoMMMMoM|r| |`-..|   |    |      |
      |    _!.-j'  | _!,"|_|M<>MMMMoMMM|_||!._|  `i-!.._ |      |
     _!.-'|    | _."|  !;|1|MbdMMoMMMMM|l|`.| `-._|    |``-.._  |
..-i'     |  _.''|  !-| !|_|MMMoMMMMoMM|_|.|`-. | ``._ |     |``"..
   |      |.|    |.|  !| |u|MoMMMMoMMMM|n||`. |`!   | `".    |
   |  _.-'  |  .'  |.' |/|_|MMMMoMMMMoM|_|! |`!  `,.|    |-._|
  _!"'|     !.'|  .'| .'|[@]MMMMMMMMMMM[@] \\|  `. | `._  |   `-._
-'    |   .'   |.|  |/| /                 \\|`.  |`!    |.|      |`-
      |_.'|   .' | .' |/                   \\  \\ |  `.  | `._    |
     .'   | .'   |/|  /                     \\ |`!   |`.|    `.  |
  _.'     !'|   .' | /                       \\|  `  |  `.    |`.|
"""


banana_ascii = """
 _
//\\
V  \\
 \\  \\_
  \\,'.`-.
   |\\ `. `.
   ( \\  `. `-.                        _,.-:\\
    \\ \\   `.  `-._             __..--' ,-';/
     \\ `.   `-.   `-..___..---'   _.--' ,'/
      `. `.    `-._        __..--'    ,' /
        `. `-_     ``--..''       _.-' ,'
          `-_ `-.___        __,--'   ,'
             `-.__  `----\"\"\"    __.-'
                  `--..____..--'
"""


snake_ascii = """
   /^\\/^\\
         _|__|  O|
\\/     /~     \\_/ \\
 \\____|__________/  \\
        \\_______      \\
                `\\     \\                 \\
                  |     |                  \\
                 /      /                    \\
                /     /                       \\
              /      /                         \\ \\
             /     /                            \\  \\
           /     /             _----_            \\   \\
          /     /           _-~      ~-_         |   |
         (      (        _-~    _--_    ~-_     _/   |
          \\      ~-____-~    _-~    ~-_    ~-_-~    /
            ~-_           _-~          ~-_       _-~
               ~--______-~                ~-___-~
"""


room_6_ascii = """
           ."`".
       .-./ _=_ \\.-.
      {  (,(oYo),) }}
      {{ |   "   |} }
      { { \\(---)/  }}
      {{  }'-=-'{ } }
      { { }._:_.{  }}
      {{  } -:- { } }
      {_{ }`===`{  _}
     ((((\\)     (/))))
"""


happy_monkey_ascii = """
                _
            ,.-" "-.,
           /   ===   \\
          /  =======  \\
       __|  (o)   (0)  |__
      / _|    .---.    |_ \\
     | /.----/ O O \\----.\\ |
      \\/     |     |     \\/
      |                   |
      |                   |
      |                   |
      _\\   -.,_____,.-   /_
  ,.-"  "-.,_________,.-"  "-.,
 /          |       |          \\
|           l.     .l           |
|            |     |            |
l.           |     |           .l
 |           l.   .l           | \\,
 l.           |   |           .l   \\,
  |           |   |           |      \\,
  l.          |   |          .l        |
   |          |   |          |         |
   |          |---|          |         |
   |          |   |          |         |
   /"-.,__,.-"\\   /"-.,__,.-"\\"-.,_,.-"\\
  |            \\ /            |         |
  |             |             |         |
   \\__|__|__|__/ \\__|__|__|__/ \\_|__|__/
"""


key_ascii = """
  ooo,    .---.
 o`  o   /    |\\________________
o`   'oooo()  | ________   _   _)
`oo   o` \\    |/        | | | |
  `ooo'   `---'         "-" |_|
"""


# Global variables
inventory = []
left = ("left", "go left")
right = ("right", "go right")
forward = ("forward", "go forward")
back = ("back", "go back")


# Useful functions
def cls(newlines=20):
    print("\n" * 100)


def slow_print(text, wait=0.04):
    for c in text:
        print(c, end="")
        if c in ".,!?;:":
            sleep(6 * wait)
        else:
            sleep(wait)
    print()


def roll_credits():
    input("Press enter to continue...")
    cls()
    for line in game_credits.split("\n"):
        print(line)
        sleep(1)
    exit()


# Introduction function
def intro():
    cls()
    print(temple_ascii)
    slow_print(game_intro)
    input("Press enter to continue...")
    room_1()


# Room 1 functions
def solve_riddle():
    slow_print(room_1_riddle)
    options = ["Snake", "Lion", "Gorilla"]
    shuffle(options)
    correct_answer = "snake"
    for option in options:
        print("- " + option)
    while True:
        response = input("> ")
        if response == correct_answer:
            return True
        elif response != "":
            return False


def solve_mystery():
    slow_print(room_1_mystery)
    options = ["Muhammad Ali", "Winston Churchill", "Mike Tyson"]
    shuffle(options)
    correct_answer = "muhammad ali"
    for option in options:
        print("- " + option)
    while True:
        response = input("> ")
        if response == correct_answer:
            return True
        elif response != "":
            return False


def room_1():
    cls()
    slow_print(room_1_intro)
    while True:
        print(room_1_options)
        choice = input("> ")
        if choice in left:
            slow_print("Solve a riddle or die!")
            correct = solve_riddle()
            if correct:
                cls()
                print(snake_ascii)
                slow_print("That's correct; you are a true Swashbuckler! Go on ahead.")
                room_2()
            else:
                slow_print(room_1_death)
                roll_credits()
        elif choice in right:
            slow_print("Solve a mystery or die!")
            correct = solve_mystery()
            if correct:
                cls()
                slow_print("That's right; you are a true Swashbuckler! Go on ahead.")
                room_3()
            else:
                slow_print(room_1_death)
                roll_credits()
        else:
            slow_print(invalid_choice)


# Room 2 function
room_2_options = ["- break vase", "- go left", "- go right", "- go back"]


def room_2():
    slow_print(room_2_intro)
    while True:
        slow_print("what do you want to do?\n")
        for option in room_2_options:
            print(option)
        choice = input("> ").lower()
        if choice == "break vase":
            cls()
            slow_print("you have found a key\n")
            inventory.append("room 2 key")
            room_2_options.pop(0)
        elif choice in left:
            cls()
            slow_print("you have decided to further explore deep down. What awaits you?\n")
            room_5()
        elif choice in right:
            cls()
            slow_print("Entering the golden room\n")
            room_4()
        elif choice in back:
            cls()
            slow_print("You go back to the previous room.")
            return
        else:
            slow_print(invalid_choice)


# Room 3 function
room_3_options = ["- look behind mirror", "- go right", "- go left", "- go back"]


def room_3():
    slow_print(room_3_intro)
    while True:
        for option in room_3_options:
            print(option)
        choice = input("> ").lower()
        if choice in right:
            if "room 3 key" in inventory:
                cls()
                slow_print("You use the key to unlock the door, and proceed.")
                room_6()
            else:
                slow_print("You try the door, but it is locked.")
        elif choice == "look behind mirror":
            if "room 3 key" in inventory:
                slow_print("You've already found the key")
            else:
                inventory.append("room 3 key")
                room_3_options.pop(0)
                slow_print("You have found a Key!")
        elif choice in left:
            if "room 3 key" in inventory:
                cls()
                slow_print("You use the key to unlock the door, and proceed.")
                room_4()
            else:
                slow_print("You try the door, but it is locked.")
        elif choice in back:
            cls()
            slow_print("You go back to the previous room.")
            return
        else:
            slow_print(invalid_choice)


# Room 4 function
room_4_options = ["- break vase", "- grab cane", "- go forward", "- go back"]


def room_4():
    print(temple_door_ascii)
    slow_print(room_4_intro)
    while True:
        slow_print("What do you want to do?:")
        for option in room_4_options:
            print(option)
        choice = input("> ").lower()
        if choice == "break vase":
            if "rope" in inventory:
                slow_print("You've already found the rope...\n")
            else:
                inventory.append("rope")
                slow_print("Yata! You have found a rope!\n")
                room_4_options.pop(room_4_options.index("- break vase"))
        elif choice == "grab cane":
            if "cane" in inventory:
                slow_print("You have already picked up the cane...\n")
            else:
                inventory.append("cane")
                slow_print("Yata! You have found a cane!\n")
                room_4_options.pop(room_4_options.index("- grab cane"))
        elif choice in forward:
            if "room 2 key" in inventory and "room 3 key" in inventory:
                cls()
                slow_print("Well done, you have unlocked the secret passage to the treasure!")
                treasure_room()
            else:
                slow_print("The door is locked! There are two keyways.")
        elif choice in back:
            cls()
            slow_print("You go back to the previous room.")
            return
        else:
            slow_print(invalid_choice)


# Room 5 function
def room_5():
    slow_print(room_5_intro)
    while True:
        print(room_5_options)
        choice = input("> ").lower()
        if choice in back:
            cls()
            slow_print("You go back to the previous room.")
            return
        elif choice in forward:
            if "rope" in inventory:
                cls()
                slow_print("You swing across the pit and proceed!")
                treasure_room()
            else:
                slow_print("WASTED - you have fallen to your death.")
                roll_credits()
        else:
            slow_print(invalid_choice)


# Room 6 function
def room_6():
    print(room_6_ascii)
    slow_print(room_6_intro)
    while True:
        print(room_6_options)
        choice = input("> ").lower()
        if choice in back:
            cls()
            slow_print("You go back to the previous room.")
            return
        elif choice == "fight":
            if "cane" in inventory:
                cls()
                slow_print("The ape cannot fathom your cane arts and is stunned!")
                treasure_room()
            else:
                slow_print("WASTED - The ape has punched you up.")
                roll_credits()
        else:
            slow_print(invalid_choice)


# Treasure room function
def treasure_room():
    slow_print(treasure_room_intro)
    while True:
        print(treasure_room_options)
        choice = input("> ").lower()
        if choice == "collect the gold":
            slow_print(monkey_defeat)
            roll_credits()
        elif choice == "collect the banana":
            print(happy_monkey_ascii)
            slow_print(winning_paragraph)
            roll_credits()
        elif choice == "eat the banana":
            slow_print(banana_eaten)
            roll_credits()
        else:
            slow_print(invalid_choice)


# Start
intro()
