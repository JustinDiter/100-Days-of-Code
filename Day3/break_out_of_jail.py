import time

print(''' ---.----.__..----.----| _|_||___||___||___||___||___||___||_|_ |
    |        |    |    | -.-..---..---..---..---..---..---..-.- |--.-
 ---'--.-----'----'--.-|  | ||   ||   ||   ||   ||   ||   || |  | `|
       |:           (| |  | ||   ||   ||   ||   ||   ||   || |  |--'-
       |:.           | | _|_||___||___||___||___||___||___||_|_ |
 ------'----.-.,----.'-| -.-..---..---..---..---..---..---..-.- |-.--
        ,/) |       |  |  | ||   ||   ||   ||   ||   ||   || |  | |`
 ----.---8--'--.----'--|  | ||   ||   ||   ||   ||   ||   || |  | |
     |   8     |:      | _|_||___||___||___||___||___||___||_|_ |-'--
     | ,)//    |:.     | -.-..---..---..---..---..---..---..-.- |:.
 ----'-`=;'--.-'-.----.|  | ||   ||   ||   ||   ||   ||   || |  |--.-
       //   /_ _( \    |  | ||   ||   ||   ||   ||   ||   || |  | /|
 ---.-//----)/\,'_/----| _|_||___||___||___||___||___||___||_|_ | `|
    |/|     `;=.(      | -.-..---..---..---..---..---..---..-.- |--'-
 (  |`.`.   |`,-/      |,-'-||---||---||---||---||---||---||-'-.|
 -`-'-.`.`-.';'=`.-..--'-.--------.-------------.--.-------.----'--.-
      |  `-./.}{-'\.)    |        )             |   `)     |       \
      |    :`-}{-''||    |:.      |   ,_        |          |:.     |
 ---'`'-.--|`-}{-'||)----'-.------'--'.,`--.----'--------.-'-------'-
        |  :`-`'-'/)|      |               |:.           |
 -.-----'--;`.}{,`.||----,-'--------.------'---.--------,'--.,-------
  |:     ,'/.`..'_(/(    |:         |          |             \
  |:.  ,',' |`--`.('))   |:.        |          |             |:
 -'--,' <.._|__,. >`,----'----------'--------.,'-------------'----SSt
     ``----....(','
            _,'>'
            )/
            `'
''')
print("You are locked in a prison cell. You plan to escape. You check the door.")

# First player choice

first_choice = input("The door is unlocked. Will you go \"left\" or \"right\" ? ")
first_choice = first_choice.lower()

if first_choice == "left" :
    print("You make it to another door.")
elif first_choice == "right" :
    print("You round the corner and you are caught by a guard. Game Over.")
    time.sleep(5)
    exit()
else :
    print("If you can't follow the instructions then you're no fun to play with. Peace out")
    time.sleep(5)
    exit()

# Second player choice 

second_choice = input("Will you open the door, \"yes\" or \"no\" ? ")
second_choice = second_choice.lower()

if second_choice == "yes" :
    print("You open the door and go to the other side.")
elif second_choice == "no" :
    print("A guard rounds the corner and spots you. Game Over.")
    time.sleep(5)
    exit()
else :
    print("If you can't follow the instructions then you're no fun to play with. Peace out.")
    time.sleep(5)
    exit()

# Third choice

third_choice = input("You enter the room and there is a telephone, a window, and another door. Which will you interact with, the \"telephone\", \"window\", or \"door\" ? ")
third_choice = third_choice.lower()

if third_choice == "telephone" :
    print("You take the phone and call your attourney. He does his magic and is able to get you out, scott free. You win !")
    time.sleep(10)
    exit()
elif third_choice == "window" :
    print("I'm not sure why, but upon opening the window you decide to escape out of it without looking below. You fall sixty stories. Game Over.")
    time.sleep(8)
    exit()
elif third_choice == "door" :
    print("Upon opening the door, you realize that you are trapped in an infinite loop of entering the same room, never able to return. After some time you lose your sanity. Game Over.")
    time.sleep(8)
    exit()
else : 
    print("If you can't follow the instructions then you're no fun to play with. Peace out")
    time.sleep(5)
    exit()
