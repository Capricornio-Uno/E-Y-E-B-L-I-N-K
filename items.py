# Room 1

# ====================================== ITEMS ============================================


class Object:
    def __init__(self):
        raise NotImplementedError("Do not create raw objects.")

    def __str__(self):
        return self.name


class GrapheneBag(Object):
    def __init__(self):
        self.name = "Graphene bag"
        self.description = "It's a composite graphene bag. You can store things on it."
        self.damage = 2
    
class Videophone(Object):
    def __init__(self):
        self.name = "Videophone"
        self.description = "It's an old COM terminal."
        self.damage = 3

class ShockStick(Object):
    def __init__(self):
        self.name = "ShockStick"
        self.description = "It's a self defense weapon. Pressing a switch releases an energy blast."
        self.damage = 8


class Consumable:
    def __init__(self):
        raise NotImplementedError("Do not create raw Consumable objects.")

    def __str__(self):
        return "{} (+{} HP)".format(self.name, self.healing_value)


class RecoveryPill(Consumable):
    def __init__(self):
        self.name = "Recovery pill"
        self.healing_value = 10


