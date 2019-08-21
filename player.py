# Room 1

# ========================================== PLAYER ===============================================

import items

class Player:
	def __init__(self):
		self.inventory = [items.Handbag(),
						  items.Videophone(),
						  items.ShockStick()]

	def print_inventory(self):
	        print("Inventory:")
	        for item in self.inventory:
	            print('*' + str(item))

