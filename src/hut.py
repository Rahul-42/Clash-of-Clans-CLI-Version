class Hut:
    def __init__(self, x, y, health):
        self.x = x
        self.y = y
        self.health = health


class Th(Hut):
    def __init__(self, x, y, health):
        super().__init__(x, y, health)


class Can(Hut):
    def __init__(self, x, y, health, damage):
        super().__init__(x, y, health)
        self.damage = damage


class Wizard(Hut):
    def __init__(self, x, y, health, damage):
        super().__init__(x, y, health)
        self.damage = damage


class Walls(Hut):
    def __init__(self, x, y, health):
        super().__init__(x, y, health)
