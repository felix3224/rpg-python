import random
from   character import Player, Enemy

class Combat:
    #this dont need of a self. because just rolla dice and no go modify some
    @staticmethod
    def roll_dice(side: int) -> int:
        """Rolls a dice with the given number of sides (e.g., 20)"""
        return random.randint(1,side)
    #Here is the same thing, dont need of none 
    @staticmethod
    def battle(attacker, defender):
        print(f'[{attacker.name}] is attacking [{defender.name}]!!')

        result_dice = Combat.roll_dice(20)
        
        total_damage = 0 

        if result_dice == 20:
            print(f'Dice: {result_dice} - Atack critical!!!\n')
            total_damage = attacker.attack * 2
        
        elif result_dice == 1:
            print(f"Do you know what luck is? It's what you don't have. - Dice: {result_dice}\n")
            total_damage = 0
        
        else:
            print(f'Atack standard! - Dice: {result_dice}\n')
            total_damage = attacker.attack 
        
        if total_damage > 0:
            defender.take_damage(total_damage)
    
    # i think that a weapon is for have a atacker and damage? what you think? because this combat no have weapon.
    # Or add o damge total + weapon. what would the better sistema? would might too the atack of character more atacker of weapon.