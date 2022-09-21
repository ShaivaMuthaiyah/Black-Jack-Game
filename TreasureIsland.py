print('''
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
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

first = input("You are at the dock! Will you go to the forest or take the footpath? Forest or Foot ").lower()

if first == "forest":
	print("You are now at the forest!")
	second = input("You find an abandoned shrine! do you want to explore it? Y or N? ").lower()

	if second == "y":
		print("You found the treasure!!")

	if second == "n":
		print("A zombie attacked you from behind while you were distracted!! You are dead!!")
		

if first == "foot" or first == "footpath":

	print("You are now at an abandoned village!")
	second = input("You see something moving inside a house! Do you want to check it out? Y or N ").lower()

	if second == "y":
		print("A zombie attacked you from inside the house!! Youre dead")

	if second == "n":
		print("You noticed a zombie walking out and decided to run to the forest")
		print("You are now at the forest!")
		
		third = input("You find an abandoned shrine! do you want to explore it? Y or N? ").lower()

		if third == "y":
			
			
			print("You found the treasure!!")

		if third == "n":
		    print("The zombie followed you and attacked you while you were distracted!! You are dead!!!")

	    

		

	
	

        
        
	
		