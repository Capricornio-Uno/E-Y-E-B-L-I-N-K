''' 

    Room 1

    A text adventure written by Capricornio-Uno (miguelreinoso7@gmail.com)

    August 2019

'''

# ============================== THINGS THAT I'M TESTING ====================================

# This will print the output in a more cinematic way

'''
import sys

BAUD = 1200

def baudout(s):
    for c in s:
        sleep(9. / BAUD)  # 8 bits + 1 stop bit @ the given baud rate
        sys.stdout.write(c)
        sys.stdout.flush()

 baudout(game.output)
'''
 

from player import Player
from time import sleep
	
# ========================================== Functions ========================================
  	     
def three_blank_lines(): # Spaces between paragraphs
	print()
	print()
	print()

def shpause(): # short pause in the narrative
	sleep(3)

def lpause(): # long pause in the narrative
	sleep(7)

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

# ==================================== NARRATIVE ================================================

three_blank_lines()

print("                       _____                         __          ")
print("                      |  __ \                       /_ |         ")
print("                      | |__) |___   ___  _ __ ___    | |         ")
print("                      |  _  // _ \ / _ \| '_ ` _ \   | |         ")
print("                      | | \ \ (_) | (_) | | | | | |  | |         ")
print("                      |_|  \_\___/ \___/|_| |_| |_|  |_|         ")

three_blank_lines()

shpause()

print("""
                                 Synopsis: 

It's the year 2050. After the climate breakdown, life on the surface of the planet
became impossible ... Humans and cyborgs started to live in subterranean megacities where 
everyone struggles to survive. 
""")

lpause()

print("""
In this wicked world, you're a little girl called Valeria. You survive collecting and selling
junk, hacking machines and stealing Qtrits, the cryptocurrency that wealthy people uses in
the underground.  
""")

lpause()

print("""
One night you're coming back to your cabin to get some rest and you find a strange woman
waiting at the door of your block. She asks you for an adress. You try to run without
answering nothing but it's too late. A protocol droid appears from the shadows and grabs
you while the woman forces you to inhale some kind of drug ...
""")

lpause()

print("""
You fall asleep ... 
""")

three_blank_lines()

lpause()

print("Instructions: Play with your keyboard. Enter commands in lower case (n,s,e,w, get lamp ...)")

three_blank_lines()

shpause()

print("""
You awake ... 
After opening your eyes you find yourself in an empty room.
There's only a wall with a strange drawing on it.
There are doors to the east and the west.
There's a plastic curtain to the north.
""")

play()
