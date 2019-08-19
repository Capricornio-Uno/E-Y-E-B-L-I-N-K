''' 

    Room 1

    A text adventure written by Capricornio-Uno (miguelreinoso7@gmail.com)

    August 2019


'''

import time

# ====================================== Objects ============================================

class Object:
	def __str__(self):
		return self.name

class Handbag(Object):
	def __init__(self):
		self.name = "Handbag"
		self.description = "It's a composite graphene bag. You store your things on it."
		self.damage = 2
	
class Videophone(Object):
	def __init__(self):
		self.name = "Videophone"
		self.description = "It's an old COM terminal."
		self.damage = 3

class ShockStick(Object):
	def __init__(self):
		self.name = "ShockStick"
		self.description = "It's a self defense weapon. You always carry this with you."
		self.damage = 8
	
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
	inventory = [Handbag(),Videophone(),ShockStick()]
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
			print()
			print("Inventory: ")
			for item in inventory:
				print('*' + str(item))
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

print("Synopsis: It's the year 2050. After the climate breakdown, life on the surface of the planet")
print("became impossible ... Humans and cyborgs started to live in subterranean megacities where ")
print("the ability to survive is a must. ")
print()

lpause()

print("In this wicked world, you're a female cyborg called Alyssa, a basic pleasure model. ")
print("You play sex with rich women and men in exchange for Qtrits, the cryptocurrency ")
print("that wealthy people uses in the underground.")
print()

lpause()

print("Your problems start when you meet with a customer called Anastasia, who dates you on a friday")
print("night at the artificial lake on Sector 9. She wanted to enjoy sex in a public space so you")
print("both agreed to walk into a darker zone of the artificial woods ...")
print()

lpause()

print("She offered you some kind of marijuana joint and after smoking for a while ...")
print("you fell asleep ..")

three_blank_lines()

lpause()

print("Instructions: Play with your keyboard. Enter commands in lower case (n,s,e,w, get lamp ...)")

three_blank_lines()

shpause()

print("You awake ... After opening your eyes all you can see is an enormous room ... ")
print("Maybe an hangar or something like that ...")
print("The light is dim but it seems a large location, maybe a military facility, who knows ...")
print("It seems that you're alone and all you can hear is silence ...")
print("Maybe you should start to explore this place and try to find the exit ...")
print()

play()

