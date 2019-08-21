''' 

    Room 1

    A text adventure written by Capricornio-Uno (miguelreinoso7@gmail.com)

    August 2019

'''

from player import Player

import time
	
# ========================================== Functions ========================================

def three_blank_lines(): # Spaces between paragraphs
	print()
	print()
	print()

def shpause(): # short pause in the narrative
	time.sleep(3)

def lpause(): # long pause in the narrative
	time.sleep(7)

def get_player_command(): # Player prompt
	print()
	return input("What now? ")

def play(): # Main loop
	player = Player()
	while True:
		action_input = get_player_command()
		if action_input == 'n':
			print("You go north")
		elif action_input == 's':
			print("You go south")
		elif action_input == 'e':
			print("You go east")
		elif action_input == 'w':
			print("You go west")
		elif action_input == 'i':
			player.print_inventory()
		else:
			print("Invalid action")

# ============================================== PROGRAM ============================================

three_blank_lines()

print("               _____                         __          ")
print("              |  __ \                       /_ |         ")
print("              | |__) |___   ___  _ __ ___    | |         ")
print("              |  _  // _ \ / _ \| '_ ` _ \   | |         ")
print("              | | \ \ (_) | (_) | | | | | |  | |         ")
print("              |_|  \_\___/ \___/|_| |_| |_|  |_|         ")

three_blank_lines()

shpause()

print("""
                                 Synopsis: 

It's the year 2050. After the climate breakdown, life on the surface of the planet
became impossible ... Humans and cyborgs started to live in subterranean megacities where 
the ability to survive is a must. 
""")

lpause()

print("""
In this wicked world, you're a female cyborg called Alyssa, a basic pleasure model. 
You play sex with rich women and men in exchange for Qtrits, the cryptocurrency 
that wealthy people uses in the underground.
""")

lpause()

print("""
Your problems start when you meet with a customer called Anastasia, who dates you on a friday
night at the artificial lake on Sector 9. She wanted to enjoy sex in a public space so you
both agreed to walk into a darker zone of the artificial woods ...
""")

lpause()

print("""
She offered you some kind of marijuana joint and after smoking for a while ...
you fell asleep ... 
""")

three_blank_lines()

lpause()

print("Instructions: Play with your keyboard. Enter commands in lower case (n,s,e,w, get lamp ...)")

three_blank_lines()

shpause()

print("""
You awake ... After opening your eyes all you can see is an enormous room ... 
Maybe an hangar or something like that ...
The light is dim but it seems a large location, maybe a military facility, who knows ...
It seems that you're alone and all you can hear is silence ...
Maybe you should start to explore this place and try to find the exit ...
""")

play()

