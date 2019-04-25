from random import randrange

class Robot():
    max_damage = 5


    def __init__(self, lifes):
        self.lifes = lifes

    def _make_damage(self, target_robot):
        """Generates random damage and forces the
        other robot to defend."""
        damage = randrange(0, self.max_damage)
        target_robot.defend(damage)


    def _take_damage(self, damage):
        """Sets new number of lifes when not already 0."""
        if self.lifes - damage <0:
            self.lifes = 0
        else:
            self.lifes -= damage
    
    def is_alive(self):
        """Returns True if robot has any lifes left."""
        return self.lifes > 0

    def defend(self, damage):
        """Default defend. Simply takes damage."""
        self._take_damage(damage)

    def attack(self, target_robot):
        """Default attack. Simply makes damage."""
        self._make_damage(target_robot)

class Aggressive(Robot):
    max_damage = 7
    def attack(self, target_robot):
        """Makes damage to the other robot twice. Special for aggresive robot."""
        self._make_damage(target_robot)
        self._make_damage(target_robot)
class Defensive(Robot):
    max_damage = 3    
    def defend(self, damage):

        """Special for deffensive robot, takes only half damage."""
        self._take_damage(damage // 2)

aggr = Aggressive(10)
deff = Defensive(50)
while True:
    aggr.attack(deff)
    print('Deff: {}'.format(deff.lifes))
    if not deff.is_alive():
        print('Aggr won')
        break
    
    deff.attack(aggr)
    print('Aggr: {}'.format(aggr.lifes))   
    if not aggr.is_alive():
        print('Deff won')
        break