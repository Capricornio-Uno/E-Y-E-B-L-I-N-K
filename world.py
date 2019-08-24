# Room 1

# ====================================== WORLD ================================================

class MapTile:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def intro_text(self):
		raise NotImplementedError("Create a subclass instead!")

class ThreeCyborgsTile(MapTile):
	def intro_text(self):
		return """
		There are lots of shelves full of parts, dirt and junk. 
		You can see a stand with three cyborgs on it. 
		They look asleep and abandoned for some reason.
		"""

class StartTile(MapTile):
	def intro_text(self):
		return """
		This is the place where you woke up. 
		There's only a wall with a strange drawing on it.
		There are doors to the east and the west.
		There's a plastic curtain to the north.
		"""

class CrystalMachineTile(MapTile):
	def intro_text(self):
		return """
		Some sort of machinery is inside a crystal container with a built-in electromagnetic door.
		The door seems operated from a panel on the right.
		You look carefully at the panel and see a red button, a keypad and a holographic display.
		"""

class CenterTile(MapTile):
	def intro_text(self):
		return """
		You walk through a plastic curtain and find yourself in another chamber.
		There are doors on your left and right.
		In the center there's a drawing, it seems a labyrinth ...
		To the north there's a long and dark corridor.
		"""

class ExitTile(MapTile):
	def intro_text(self):
		return """
		After walking for a while you arrive to a large room.
		Poweful lights and pure white walls are so bright that you can barely open your eyes.
		The only thing here is an artifact like a ring. It's void within.
		It has flashing lights on it.
		"""

room1_map = [
	[None,ExitTile(1,0),None]
	[None,CenterTile(1,1),None]
	[ThreeCyborgsTile(0,2),StartTile(1,2),CrystalMachineTile(2,2)]
]

def tile_at(x,y): # locates the tile at a coordinate
	if x < 0 or y > 0: 
		return None
	try:
		return room1_map[y][x]
	except IndexError:
		return None 