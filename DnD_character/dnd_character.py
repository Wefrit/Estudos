import random
class Character:
    def __init__(self):
        abilities = ["strength", "dexterity", "constitution", "intelligence", "wisdom", "charisma"]
        for ability in abilities:
            dice_list = [random.randint(1,6), random.randint(1,6), random.randint(1,6), random.randint(1,6)]
            min_removed = dice_list.remove(min(dice_list))
            setattr(self, ability, sum(dice_list))   
        self.hitpoints = 10 + modifier(self.constitution)
    def ability (self):
        return random.choice([self.strength,
                             self.dexterity,
                             self.constitution,
                             self.intelligence,
                             self.wisdom,
                             self.charisma])
def modifier(value):
    return (value - 10) // 2 
