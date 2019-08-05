print()
print("Room 1")
print()
print("Instructions: Play with your keyboard. When entering directions use lower case (n,s,e,w)")
print()

action_input = input("Action: ")

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

