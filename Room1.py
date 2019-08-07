''' 

    Room 1

    A text adventure written by Capricornio-Uno (miguelreinoso7@gmail.com)

    August 2019


'''

def three_blank_lines():
	print()
	print()
	print()

def get_player_command():
	return input("What now? ")

def play():
	action_input = get_player_command()
	if action_input == 'n':
		print("You go north")
	elif action_input == 's':
		print("You go south")
	elif action_input == 'e':
		print("You go east")
	elif action_input == 'w':
		print("You go west")
	else:
		print("Invalid action")

three_blank_lines()

print("               _____                         __          ")
print("              |  __ \                       /_ |         ")
print("              | |__) |___   ___  _ __ ___    | |         ")
print("              |  _  // _ \ / _ \| '_ ` _ \   | |         ")
print("              | | \ \ (_) | (_) | | | | | |  | |         ")
print("              |_|  \_\___/ \___/|_| |_| |_|  |_|         ")

three_blank_lines()

print("Instructions: Play with your keyboard. Enter commands in lower case (n,s,e,w ...)")

three_blank_lines()

print("You awake ... After opening your eyes all you can see is an enormous room ... ")
print("Maybe an hangar or something like that ...")
print("The light is dim but it seems a large location, maybe a military facility, who knows ...")
print("It seems that you're alone and all you can hear is silence ...")
print("Maybe you should start to explore this place and try to find the exit ...")
print()


play()

