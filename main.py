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

print("You find yourself on a path that leads to the edge of a large body of water.")
print("You can walk along the shoreline, wait for a boat, or swim.")
first_decision = input("What do you do? Enter (walk, wait, or swim) ").lower()

if first_decision == 'walk':
  print("\nYou begin your walk along the shoreline.")
  print("After about an hour you come across a small skiff that has long since wrecked and aged with time.")
  print("You look inside the skiff and see a skeleton clutching sword and a piece of crumpled paper.")
  print("You can leave the poor soul alone, take the paper, or bury the body.")
  second_decision = input("What do you do? Enter (leave, take, or bury) ").lower()

  if second_decision == 'leave':
    print("\nYou continue your journey along the shore line.")
    print("Darkness falls, and finding no shelter, you lay down next to a large piece of driftwood for the night.")
    print("While sleeping the tide comes in and before you know it you are swept out to sea and drown in the current.")
    print("GAME OVER")
  elif second_decision == 'take':
    print("\nYou bend over and take the crumpled piece of paper from the clutches of the skeleton.")
    print("Suddenly the skeleton comes alive with the ghostly spirit of the pirate he once was!")
    print("He swings his rusted blade and connects! The last thing you see as you slowly bleed is the crumpled piece of paper.")
    print("It is now unfolded and holds a faded drawing of the pirate and his family.")
    print("GAME OVER")
  else:
    print("\nYou carefully remove the skeleton from the skiff, and respectfully bury him nearby above the waterline.")
    print("As you affix a makeshift gravestone to the head of the grave a sense of peace comes over you.")
    print("A ghostly light emenates from a nearby tree, you walk over and find a long forgotten spade near the base of the tree!")
    print("After several moments digging at the base of the tree you hit a solid object with a loud thump!")
    print("You have found the treasure! Buried as the pirates final act before returning to the skiff to look upon the visage of his family one last time before succumbing to his wounds and exposure.")
    print("YOU HAVE WON!")
elif first_decision == 'wait':
  print("\nYou wait for a time by the shoreline.")
  print("Several hours pass and the tide begins to come in.")
  print("After several more hours as it is getting dark you see a small boat carried out to sea from somewhere down the shoreline and watch as it sinks below the surface. ")
  print("With darkness good and set in you get a strange feeling you have missed your chance to find the treasure.")
  print("You sleep away from the shoreline and wait until first light to make your next decision.")
  print("Feeling weary from hunger you feel you only have two choices before you. You can either continue to wait or swim.")

  second_decision = input("What do you do? Enter (wait or swim) ").lower()
  if second_decision == 'wait':
    print("\nYou wait some more and watch the ebb and flow of the sea. ")
    print("You feel your indecision has cost you the chance to find the treasure, and hopelessness sets in.")
    print("You head home, you have failed the mission.")
    print("GAME OVER")
  else:
    print("\nYou begin to swim.")
    print("30 minutes into the swim you see a dot in the distance and come to recognize it as an island.")
    print("You are getting tired though, weak from hunger. You realize after a few more minutes of struggling to swim that you are too tired to fight the current.")
    print("Your last thought as you are pulled down below the briny surface is 'if only you had swam the previous day you would have made it to shore again!'")
    print("You have drowned.")
    print("GAME OVER")
else:
  print("\nYou begin to swim out in a straight line.")
  print("30 minutes into the swim you feel strong still and recognize an island in the distance.")
  print("After another 30 minutes you make it to the island safe and in one piece.")
  print("You are glad you did not waste time being indecisive.")
  print("You begin to explore the island")
  print("You come across a small trail that takes you to a small cave. You can either go in or keep exploring.")

  second_decision = input("What do you do? Enter (cave or explore) \n").lower()
  if second_decision == 'cave':
    print("\nYou walk inside the cave and find it empty.")
    print("In your frustration and still tired from the swim you hit the side of the cave wall.")
    print("This action causes a cave in, where the rocks trap you inside.")
    print("You scream and yell for help and attempt to move the rocks, only to have more rocks fall to block the cave mouth further.")
    print("You die a slow death of starvation.")
    print("GAME OVER")
  else:
    print("\nYou continue your exploration of the island and come across the skeleton of a long dead pirate.")
    print("He is pointing to a small copse of trees nearby and has a spade in his hands!")
    print("This is it! You may have found the treasure!")
    print("You grab the shovel from his long dead hands and rush to the copse of trees!")
    print("You get to the copse and look beyond the first few trees to find a pit already dug.")
    print("The pit is roughly the size of a treasure chest, maybe a bit bigger.")
    print("The treasure has already been removed! As you turn around the last thing you see is the skeleton.")
    print("He swings a bony fist at you and knocks you into the hole.")
    print("You come to just in time to see the sinister pirate burying you alive! BWAHAHA!")
    print("GAME OVER")
