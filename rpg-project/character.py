from dataclasses import dataclass, field
from inventory   import Inventory

#because don need of class (ABC)?
@dataclass
class Character:
    name:  str
    hp:     int
    max_hp: int
    attack: int
    defense:int

    def __str__(self):
        return f'\n[{self.name}] \nHP:   {self.hp}/{self.max_hp} \n⚔️ATK: {self.attack} \n🛡️ DEF:{self.defense} \n'
    
    def take_damage(self, damage_amount:int):
        #Same the defense begin more than atk, still go take 1 of life
        actual_damage = max(1, damage_amount - self.defense)
        self.hp -= actual_damage

        print(f'{self.name} takes {actual_damage} DAMAGE! HP: {self.hp}/{self.max_hp}\n')

#CREATE PLAYER AND ENYMEN
@dataclass
class Player(Character):
    mana:     int
    level:    int = 1
    backpack: Inventory = field(default_factory = Inventory)
@dataclass
class Enemy(Character):
    xp_rewards: int # hom much XP the player gets for killing this enemys

