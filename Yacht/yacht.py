from random import randint

# Score categories.
# Change the values as you see fit.

class YACHT:    

    def score(self, dice, category):

        counts = [dice.count(x) for x in set(dice)]
        categories ={
            "YACHT": 50 if len(set(dice)) == 1 else 0,
            "ONES": 1 * dice.count(1),
            "TWOS": 2 * dice.count(2),
            "THREES": 3 * dice.count(3),
            "FOURS": 4 * dice.count(4),
            "FIVES": 5 * dice.count(5),
            "SIXES": 6 * dice.count(6),
            "FULL_HOUSE": sum(dice) if sorted([dice.count(x) for x in set(dice)]) == [2, 3] else 0,
            "FOUR_OF_A_KIND": sum([x for x in dice if dice.count(x) >= 4][:4]),
            "LITTLE_STRAIGHT": 30 if sorted(dice) == [1, 2, 3, 4, 5] else 0,
            "BIG_STRAIGHT": 30 if sorted(dice) == [2, 3, 4, 5, 6] else 0,
            "CHOICE": sum(dice)

        }
        return categories.get(category, 0)
    
jogador = YACHT()
        
print(jogador.score([5, 5, 5, 5, 5],"FOUR_OF_A_KIND"))

