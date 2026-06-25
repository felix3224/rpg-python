from abc import ABC
from dataclasses import dataclass


@dataclass
class Item(ABC):
    name: str
    description: str
    weight: float
    value: int

    def get_detailed_info(self) -> str:
        """Retorna uma string formatada com os detalhes do item."""
        info = (
            f"📦 Nome: {self.name}\n"
            f"📖 Descrição: {self.description}\n"
            f"⚖️ Peso: {self.weight} kg | 💰 Valor: {self.value} moedas"
        )
        # Se for uma Arma, adicionamos o dano dinamicamente (Polimorfismo!)
        if hasattr(self, "damage"):
            info += f" | 💥 Dano: {self.damage}"
        # Se for um Consumível, adicionamos a cura
        elif hasattr(self, "heal_amount"):
            info += f" | ❤️ Cura: {self.heal_amount} HP"

        return info


@dataclass
class Weapon(Item):
    # A Weapon has all the atribut inherit of item more damage
    damage: int


# Ainda não vou implementar esses equipamentos defesa apenas ou não sei vai depender do tempo
@dataclass
class Armor(Item):
    protection = int


@dataclass
class Consumable(Item):
    # A consumable inhert all the stts of Item, plus healing
    heal_amount: int

    def use(self, target):
        # Aplica a cura
        target.hp += self.heal_amount

        # Evita ultrapassar o máximo
        if hasattr(target, "max_hp"):
            target.hp = min(target.hp, target.max_hp)

        print(f'\n 🧃 You drink the "{self.name}"! Recover: {self.heal_amount} HP!\n')
        print(f"{target.name} HP: {target.hp}/{target.max_hp}\n")
