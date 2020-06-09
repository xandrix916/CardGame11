class Card(object):

    def __init__(self, name, health, armor, damage, coef, aoa):
        self.name = name
        self.health = health
        self.armor = armor
        self.damage = damage
        self.coef = coef
        self.fortune = 0.01
        self.aoa = aoa
        self.aoa_max = aoa
        self.alive = True
        self.x = 0
        self.y = 0

    def setCoord(self, x, y):
        self.x = x
        self.y = y

    def get_damage(self, list):
        for i in range(len(list)):
            self.health -= list[i]*(1-self.armor[i])
        if self.health <= 0:
            self.alive = False

    def give_damage(self, card):
        card.get_damage(self.damage)

    def reset(self):
        self.aoa = self.aoamax

    def move(self, x1, y1):
        self.aoa -= 1
        self.x += x1
        self.y += y1

    def wait(self):
        self.aoa = 0


class Player(object):

    def __init__(self, name, card):
        self.name = name
        self.card = card

