import random
class Character:
    def __init__(self):
        abilities = ["strength", "dexterity", "constitution", "intelligence", "wisdom", "charisma"]
        for abilitie in abilities:
            dice_list = [random.randint(1,6), random.randint(1,6), random.randint(1,6), random.randint(1,6)]
            min_removed = dice_list.remove(min(dice_list))
            setattr(self, abilitie, sum(dice_list))            




def modifier(value):
    pass

personagem = Character()

print(personagem.strength, personagem.charisma)