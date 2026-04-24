from abc         import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class Item(ABC):
    name:        str
    description: str
    weight:      float
    value:       int

    @abstractmethod 
    def use(self):
        pass

@dataclass
class Weapon(Item):
    #A Weapon has all the atribut inherit of item more damage
    damage: int

    def use(self):
        print(f'\n 🗡️ You swing the "{self.name}"! Damage: {self.damage}!\n')

@dataclass
class Consumable(Item):
    #A consumable inhert all the stts of Item, plus healing
    heal_amount: int

    def use(self, target):
        # Aplica a cura
        target.hp += self.heal_amount

        # Evita ultrapassar o máximo
        if hasattr(target, "max_hp"):
            target.hp = min(target.hp, target.max_hp)

        print(f'\n 🧃 You drink the "{self.name}"! Recover: {self.heal_amount} HP!\n')
        print(f'{target.name} HP: {target.hp}/{target.max_hp}\n')