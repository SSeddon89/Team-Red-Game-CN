from time import sleep
import sys


def typewriter(demo):
# This typewriter function makes the text appeard letter by letter.
    for c in demo:
        print(c, end='')
        sys.stdout.flush()
        sleep(0.05)
    print("\n")
typewriter("\nHello from the Red Team!")
    


def hallway():
# This hallway function is one level of the game which include multiple choice question.
    print("\n")
    typewriter("Do you want to (1) go through the door or (2) leave the house?") 
    answer = input (">")
    if answer == "1":
        frontroom()
    elif answer == "2":
        print("\n")
        typewriter("Bye have a nice day!")
        play_again()
    else:
        print("\n")
        print("Incorrect Answer!") 
        typewriter("Go and learn how to type a number")
        hallway()

def frontroom():
# This frontroom function is second level of the game including ascii art and tricky question for the player.
    print("\n")
    print("""\n
    
                             .-.
                       .'   `.
                       :g g   :
                       : o    `.
                      :         ``.
                     :             `.
                    :  :         .   `.
                    :   :          ` . `.
                     `.. :            `. ``;
                        `:;             `:'
                           :              `.
                   updog    `.              `.     .
                              `'`'`'`---..,___`;.-'
 \n """)
    typewriter("A Ghostly apparition manifests in the centre of the room and asks a question:")
    print("\n")
    typewriter("What kind of coat is always wet when you put it on?")
    answer = input (">").lower()
# .lower function ensures that player input is converted to lowercase.
    if "paint" in answer:
        basement()
    elif answer == "":
        print("Incorrect Answer!")
        play_again()
    else:
        print("Incorrect Answer!")
        play_again()


def basement():
# This basement function is third level of the game including ascii art and tricky question for the player.
    print("\n")
    typewriter("""  
  ooo,    .---.
 o`  o   /    |\________________
o`   'oooo()  | ________   _   _)
`oo   o` \    |/        | | | |
  `ooo'   `---'         "-" |_|""")
    typewriter("You descend a cold stone staircase and brush past the cobwebs to reveal a mysterious shiny key with a face")
    typewriter("The key poses the question:")
    typewriter("What belongs to you but other people use it more than you?")
    answer = input(">").lower()
    if "name" in answer:
        kitchen()
    else:
        print("\n")
        print("Incorrect Answer!")
        typewriter("The key disappears and you are trapped in the basement forever.")
        play_again()

def kitchen():
# This kitchen function is fourth level of the game including ascii art and multiple choice question for the player.
    typewriter("\nYou walk into a huge old kitchen that has not been in use for a very long time.")
    typewriter("\nThere is a red potion (1) and a blue potion (2) on the central table. Which potion will you drink? ")
    print("""\n

    --,          ,--,
   )""(          )""(
  /    \        .%nn%.
 /      \      /%%%%%%%
.        .    .%%%%%%%%.
|`-....-'|    |"*%%%%*"|
|        |    |        |
|        |    |        |
|`-....-'|    |8n....n8|
|        |    |%%%%%%%%|
|        |    |%%%%%%%%|
 `-....-' red   "*%%%%*" blue
     \n """)
    answer = input(">").lower()
    if  answer == "red" or answer == "1":
# Player can select a number or a word for each choice. This is to make it easier for the player.
        print("\n")
        typewriter("You feel weak and fall asleep forever.")
        play_again()
    elif answer == "blue" or answer == "2":
        print("\n")
        typewriter("You feel strong and progress to Monster room. ")
        monster()
    else:
        print("\n")
        print("Incorrect Answer!")
        typewriter("Go and learn how to type a number")
        kitchen()


def monster():
# This monster function is fifth and final level of the game including ascii art and tricky question for the player.
    print("\n")
    typewriter("As you enter the bedroom the door slams shut behind you and a giant green monster jumps out of the closet.")
    print("""⢀⡴⠑⡄⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⣤⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠸⡇⠀⠿⡀⠀⠀⠀⣀⡴⢿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠑⢄⣠⠾⠁⣀⣄⡈⠙⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⡀⠁⠀⠀⠈⠙⠛⠂⠈⣿⣿⣿⣿⣿⠿⡿⢿⣆⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⡾⣁⣀⠀⠴⠂⠙⣗⡀⠀⢻⣿⣿⠭⢤⣴⣦⣤⣹⠀⠀⠀⢀⢴⣶⣆
⠀⠀⢀⣾⣿⣿⣿⣷⣮⣽⣾⣿⣥⣴⣿⣿⡿⢂⠔⢚⡿⢿⣿⣦⣴⣾⠁⠸⣼⡿
⠀⢀⡞⠁⠙⠻⠿⠟⠉⠀⠛⢹⣿⣿⣿⣿⣿⣌⢤⣼⣿⣾⣿⡟⠉⠀⠀⠀⠀⠀
⠀⣾⣷⣶⠇⠀⠀⣤⣄⣀⡀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀
⠀⠉⠈⠉⠀⠀⢦⡈⢻⣿⣿⣿⣶⣶⣶⣶⣤⣽⡹⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠉⠲⣽⡻⢿⣿⣿⣿⣿⣿⣿⣷⣜⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣷⣶⣮⣭⣽⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣀⣀⣈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠻⠿⠿⠿⠿⠛⠉""")

    typewriter("The monster poses a question:")
    typewriter("I have branches yet I have no leaves, no trunk and no fruit. What am I?")
    answer = input(">").lower()
    if "bank" in answer:
        typewriter("You use your extra strength to slay the monster.")
        print("""\n            .___.
           /)               ,-^     ^-. 
          //               /           )
 .-------| |--------------/  __     __  \-------------------.__
 |WMWMWMW| |>>>>>>>>>>>>> | />>\   />>\ |>>>>>>>>>>>>>>>>>>>>>>:>
 `-------| |--------------| \__/   \__/ |-------------------'^^
          \\               \    /|\    /
           \)               \   \_/   /
                             |       |
                             |+H+H+H+|
                             \       /
                              ^-----^""")
        print("\n")
        typewriter("The house transforms into a luxury mansion where you live happily ever after.")
        print("""     *                                        !
      _.---._       !                         |>>>
    .'       '.     |>>>   *                  |>>>     *
   /           \    |>>>                      |               !
  |             |   |                   *    /~\              |>>>  
  |             |  /~\        _             /~~~\             |>>>   *
   \           /  /~~~\    /\(")/\         /~~~~~\  *  _   _  |_   _   _
    '.       ,'  /~~~~~\  //\   /\\       /~~~~~~~\   | |_| |_| |_| |_| |
      !'---'`   /~~~~~~~\ `  `m`  `      /~~~~~~~~~\ [___________________]
      |>>>     /~~~~~~~~~\              /~~~~~~~~~~~\ |           _     |
      |>>>  !  U_U_U_U_U_U         __  U _ U U U U U U|         .'|'.   |
 *    |     |>>>\ \| |/ /      _  (OO)_.'/ \ | | / / /|         |oo=|   |
     /~\    |>>> |  _  |       \'._)   .'___________/ |         |_|_|   |
    /~~~\   |    |.'|'.|        '..-'._ `'._   _   |  |   _             |
   /~~~~~\ /~\   ||=OO||    *          '.__.'.'|'. |  | .'|'.           |
  /~~~~~~~\~~~\  ||_|_||                 |   |=+=| |  | |=+=|           |
 (XXXXXXXXX)~~~\ |     |         !       |   |_|_| |  | |_|_|           |
  |   _   |xxxxx)U_U_U_U_U_U_U   |>>>    |         |_ |                 |
  | .'|'. |[]  | \ \  | |  / /   |>>>    |     _   | \|    _________    |
  | |=+=| | _  |_ |         | _  |_   _  |_  .'|'. |  |   [_________]   |
  | |_|_| || |_| ||  .-.    || |_| |_| |_| | |OO=| |  __   |XXXXXXX|    |
  |   _   |       |  | |    |    &     &   | |_|_| |_(oo)  _\/\/\/\|    |
  | .'|'. |       |  |_|    |    |'._.'|   |       |   (_.'/ " " " |    |
  | |=+=|_|   __  |         |    |__|  |   |       |_.'-..'|       |    |
  | |_|_|\'._(oo) | _       |    |'. .'|   |.---.  |  |____|_______|____|
  |   _   `.    (_.'/   .-. |    \  '  /   ||   |  | /~~~~/=========\~~~
~"| .'|'_.'  _.'-..'    | | |     '._.'    ||_  |  |/~~~~/...........\~~
  | |=+'.__.'     |     |_| |          _   ||   |  |~^"^/_____________\~^
  | |_|_| |       |         |     _    )\  ||___|__|
  |       |_______|         |_____))_.'~~'.|    ~"^"
  |       |~^^"^~"|_________|~^~.'~~'.x  x :
  lc______|        "~"^"~~"^~  : x  x :~~_.'
  ~"^"~"^"                      `-~~-'"^"^"^^
                           ~^"~^"~^""")
        playagain()
        
    
    elif answer == "":
        print("\n")
        print("Incorrect Answer!")
        play_again()
    else:
        print("\n")
        print("Incorrect Answer!")
        typewriter("The monster eats you for supper.")
        play_again()
    

def player():
# This player function is asking the player to enter his name.
    print("\n")
    chars = set('01234567890@#?£$%&*()[]"!^:;~.,/\|')
# The above line is showing that name entered is based on charaters excluding numbers and special characters.
    answer = input("Please type your name:     ")
    if answer == "":
# The condition above states if the value entered is empty the player will be prompted to enter a valid value again.
        typewriter("Did you type your name correctly?")
        start()
    elif any((c in chars) for c in answer):
# The condition above check if the character is present in the input which player entered.
        print("Did you type your name correctly?")
        start()    
    else: 
        print("\n")
        typewriter(f"Welcome {answer} to the Haunted House")

def play_again():
# This play_again function is asking the player to play again including ascii art.
    print("""


               ...
             ;::::;
           ;::::; :;
         ;:::::'   :;
        ;:::::;     ;.
       ,:::::'       ;           OOO0
       ::::::;       ;          OOOOO0
       ;:::::;       ;         OOOOOOOO
      ,;::::::;     ;'         / OOOOOOO
    ;:::::::::`. ,,,;.        /  / DOOOOOO
  .';:::::::::::::::::;,     /  /     DOOOO
 ,::::::;::::::;;;;::::;,   /  /        DOOO
;`::::::`'::::::;;;::::: ,#/  /          DOOO
:`:::::::`;::::::;;::: ;::#  /            DOOO
::`:::::::`;:::::::: ;::::# /              DOO
`:`:::::::`;:::::: ;::::::#/               DOO
 :::`:::::::`;; ;:::::::::##                OO
 ::::`:::::::`;::::::::;:::#                OO
 `:::::`::::::::::::;'`:;::#                O
  `:::::`::::::::;' /  / `:#
   ::::::`:::::;'  /  /   `#

  )\.-.      /`-.    )\   )\   )\.---.       .-./(       .-.   )\.---.     /`-. 
 ,' ,-,_)   ,' _  \  (  ',/ /  (   ,-._(    ,'     )  ,'  /  ) (   ,-._(  ,' _  )
(  .   __  (  '-' (   )    (    \  '-,     (  .-, (  (  ) | (   \  '-,   (  '-' (
 ) '._\ _)  )   _  ) (  \(\ \    ) ,-`      ) '._\ )  ) './ /    ) ,-`    ) ,_ .'
(  ,   (   (  ,' ) \  `.) /  )  (  ``-.    (  ,   (  (  ,  (    (  ``-.  (  ' ) )
 )/'._.'    )/    )/      '.(    )..-.(     )/ ._.'   )/..'      )..-.(   )/   )/
                                                                                 """)
    
    typewriter("\nDo you want to play again? (y or n)")
    answer = input(">").lower()
    if "y" in answer:
        start()
    else:
        exit()


def playagain():
# This play_again function is asking the player to play again without ascii art.
  
    typewriter("\nDo you want to play again? (y or n)")
    answer = input(">").lower()
    if "y" in answer:
        start()
    elif "n" in answer:
        print("Thank you for playing we look forward to you playing again")
        exit()
    else:
        exit()

def start():
# This start function is the intro level of the game.
    player()
    print("\n")
    print("""                                              ,           ^'^  _
                                              )               (_) ^'^
         _/\_                    .---------. ((        ^'^
         (('>                    )`'`'`'`'`( ||                 ^'^
    _    /^|                    /`'`'`'`'`'`\||           ^'^
    =>--/__|m---               /`'`'`'`'`'`'`\|
         ^^           ,,,,,,, /`'`'`'`'`'`'`'`\      ,
                     .-------.`|`````````````|`  .   )
                    / .^. .^. \|  ,^^, ,^^,  |  / \ ((
                   /  |_| |_|  \  |__| |__|  | /,-,\||
        _         /_____________\ |")| |  |  |/ |_| \|
       (")         |  __   __  |  '==' '=='  /_______\     _
      (' ')        | /  \ /  \ |   _______   |,^, ,^,|    (")
       \  \        | |--| |--| |  ((--.--))  ||_| |_||   (' ')
     _  ^^^ _      | |__| |("| |  ||  |  ||  |,-, ,-,|   /  /
   ,' ',  ,' ',    |           |  ||  |  ||  ||_| |_||   ^^^
.,,|RIP|,.|RIP|,.,,'==========='==''=='==''=='=======',,|RIP|,.,,|RIP|,.. """)

    typewriter("\nYou are caught in a terrible storm and must seek shelter. \nThe only option is a large old mansion up ahead. \nYou walk up the path and knock on the door. \nThe door slowly opens itself and you enter the chilly hallway.")
    print("\n")

    typewriter("There is a doorway to the front room.")
    print("\n")
    hallway()

 

start()
# This start function is initialising the game to start.