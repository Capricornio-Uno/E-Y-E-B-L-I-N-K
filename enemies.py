# E Y E B L I N K

# ======================================== ENEMIES =================================================

class Enemy:
    def __init__(self):
        raise NotImplementedError("Do not create raw enemy objects.")

    def __str__(self):
        return self.name

    def is_alive(self):
        return self.hp > 0


class GlassSpider(Enemy): # weak enemy
    def __init__(self):
        self.name = "Glass Spider"
        self.hp = 10
        self.damage = 2

class Guardian(Enemy): # strong enemy
    def __init__(self):
        self.name = "Guardian"
        self.hp = 25
        self.damage = 8


