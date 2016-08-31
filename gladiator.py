import random


class Gladiator:
    """ A gladiator with attributes (health, rage, damage_low, and damage_high)
    that can heal and tells when he is dead. """

    def __init__(self, name, health, rage, damage_low, damage_high):
        """ (str, int, int, int, int) -> NoneType

        Creates a gladiator with health, rage, damage_low, and damage_high.
        """
        self.name = name
        self.health = health
        self.rage = rage
        self.damage_low = damage_low
        self.damage_high = damage_high

    def attack(self, target):
        """ (class, class) -> str

        Attacks a target.
        An attack hits, crits, or misses.
        Hit does damage between damage_low and damage_high.
        A miss does 0 damage.
        A crit does double the damage of a hit.
        A deadly crit does triple damage of the hit plus the amount of rage
        the gladiator has.
        Crits occur '<rage>%' of the time.
        If there is a crit, rage is set to 0. Otherwise, it is increased by 15.
        """
        damage_power = random.randint(self.damage_low, self.damage_high)
        crit_yes_no = random.randint(1, 101)
        miss_yes_no = random.randint(1, 21)
        if miss_yes_no in [1, 5, 10, 20]:
            self.rage = self.rage - 15
            if self.rage < 0:
                self.rage = 0
            return "{0} missed and was discouraged.".format(
                self.name)
        if crit_yes_no in range(1, self.rage):
            if crit_yes_no in range(self.rage // 2):
                damage_power = damage_power * 3
                target.health = target.health - damage_power
                return "{0} got an extreme critical hit on {1} for {2} damage and {1} has {3} health and {4} rage remaining!".format(
                    self.name, target.name, damage_power, target.health, target.rage)
            self.rage -= self.rage
            damage_power = damage_power * 2
            target.health = target.health - damage_power
            return "{0} got a critical hit on {1} for {2} damage and {1} has {3} health and {4} rage remaining!".format(
                self.name, target.name, damage_power, target.health, target.rage)
        self.rage += 15
        if self.rage < 0:
            self.rage = 0
        elif self.rage > 100:
            self.rage = 100
        target.health = target.health - damage_power
        return "{0} was hit for {1} damage and has {2} health and {3} rage remaining.".format(
            target.name, damage_power, target.health, target.rage)

    def heal(self):
        """ (class) -> str

        Increases the gladiators health by 10 and decreases his rage by 10.
        """
        self.health += 10
        self.rage -= 10
        if self.rage < 0:
            self.rage = 0
        return "{0} was healed for 10 points and now has {1} health remaining.".format(self.name, self.health)

    def beg(self):
        """ (class) -> str

        Return the result of begging for your champion's life.
        """
        dice_roll = random.randint(0, 101)
        if dice_roll in range(0, 51):
            return "Your opponent feels no shame and kills you anyway."
        elif dice_roll in range(51, 101):
            return "Your opponent is feeling generous and spares you."

    def isDead(self, target):
        """ (class, class) -> int

        Returns whether or not each gladiator is alive.
        """
        if self.health <= 0:
            return 1
        elif target.health <= 0:
            return 2
