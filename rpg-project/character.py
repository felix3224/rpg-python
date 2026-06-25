from dataclasses import dataclass, field
from inventory import Inventory
from items import Weapon
from random import randint


@dataclass
class AttackResult:
    dice: int
    total_atk: int
    is_critical: bool
    is_fumble: bool


@dataclass
class Character:
    name: str
    hp: int
    max_hp: int
    atk: int
    defense: int
    equipped_weapon: Weapon | None = None

    def attack_roll_dice(self) -> AttackResult:
        # Um dado de 20 lados
        d20 = randint(1, 20)

        return AttackResult(
            dice=d20,  # resultado do d20
            total_atk=self.atk + d20,  # o ataque inicial do personagem mais o d20
            is_critical=(d20 == 20),  # valor bool
            is_fumble=(d20 == 1),  # valor bool
        )

    # Essa é uma função que centraliza a REGRA de DANO do RP. Assim não cometermos DRY (dont repeat yourself)
    def calculate_damage(self) -> int:
        weapon_dmg = self.equipped_weapon.damage if self.equipped_weapon else 0
        return (self.atk // 2) + weapon_dmg

    def show_status(self):
        arm_name = self.equipped_weapon.name if self.equipped_weapon else "EMPTY HANDS"

        # Correção do bug do total_attack: calcula dinamicamente para o ecrã

        prints = [
            f"[{self.name}]",
            f"❤️ HP:   {self.hp}/{self.max_hp}",
            f"⚔️ ATK:  {self.atk} ",
            f"🛡️ DEF:  {self.defense}",
            f"💥DANO: {self.calculate_damage()}",
        ]

        # Se a class tiver atrubuto mana adicionamos.
        if hasattr(self, "mana"):
            prints.append(f"✨ MP:  {self.mana}/{self.max_mana}")

        # Adcionamos o nome da arma que o personagem está usando.
        prints.append(f"🗡 EQUIP:{arm_name}")

        return "\n".join(prints)

    def take_damage(self, damage_amount: int):
        if damage_amount <= 0:
            return

        self.hp -= damage_amount

        if self.hp < 0:
            self.hp = 0

        print(
            f"{self.name} takes {damage_amount} DAMAGE! HP: {self.hp}/{self.max_hp}\n"
        )

    def get_defender_value(self) -> tuple[int, int]:
        # Defesa ativa: rola um d10 e soma à defesa estática
        d10 = randint(1, 10)
        return d10, (self.defense + d10)


# CLASSES DERIVADAS (PLAYER E ENEMY)
@dataclass
class Player(Character):
    mana: int = 4
    max_mana: int = 4  # Adicionado para evitar erro no show_status
    level: int = 1
    backpack: Inventory = field(default_factory=Inventory)

    # O método equip agora pertence exclusivamente ao Player
    def equip(self, weapon: Weapon):
        if weapon in self.backpack.items:
            self.equipped_weapon = weapon
            print(
                f'🗡️ [{self.name}] equipped the "{weapon.name}"! (+ Damage: {weapon.damage}) \n'
            )
        else:
            print(f'The {self.name} doesn\'t have the "{weapon.name}" in the backpack')

    def unequip(self):
        if self.equipped_weapon:
            print(f'🛡️ [{self.name}] guardou a "{self.equipped_weapon.name}".')
            self.equipped_weapon = None  # Mãos vazias
        else:
            print(f"❌ [{self.name}] já está de mãos vazias!")


@dataclass
class Enemy(Character):
    xp_rewards: int = 10
