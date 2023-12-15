# ---------------------------------------------------------------
#           %%%%%      DAY THREE PROJECT      %%%%%
# ---------------------------------------------------------------
print(''''
        *******************************************************************************
                  |                   |                  |                     |
         _________|________________.=""_;=.______________|_____________________|_______
        |                   |  ,-"_,=""     `"=.|                  |
        |___________________|__"=._o`"-._        `"=.______________|___________________
                  |                `"=._o`"=._      _`"=._                     |
         _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
        |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
        |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
                  |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
         _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
        |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
        |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
        ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
        /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
        ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
        /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
        ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
        /______/______/______/______/______/______/______/______/______/______/______/_
        *******************************************************************************
        ''')
print("Welcome to Treasure Island. Your mission is to find the treasure!")
direction = input("You are at a cross road. Where do you want to go? (Type 'left' or 'right') ").lower()

if direction != "left":
    print("You fell into a hole. Game Over.")

else:
    lake_option = input("You come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a "
                        "boat or 'swim' to swim across. ").lower()

    if lake_option != "wait":
        print("You were attacked by a shark-cat. Game Over.")
    else:
        door_color = input("You arrived at the island unharmed. There is a house with 3 doors. One red, one yellow and one "
                      "blue. Which one do you choose? ")
        if door_color == "blue":
            print("You entered a room of beasts and got eaten by them. Game Over")
        elif door_color == "red":
            print("You entered a room on fire and burned to death. Game Over.")
        elif door_color == "yellow":
            print("Congratulations! You found the treasure.")
        else:
            print("That was not an option. You died of wrong decision!")
