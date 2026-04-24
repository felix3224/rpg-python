from dataclasses import dataclass, field
from inventory   import Inventory
from items       import Weapon 
from random      import randint

@dataclass
class AttackResult:
    dice: int
    total_atk:int
    is_critical: bool
    is_fumble:   bool


#because don need of class (ABC) because i want to very npc. for say the true, i m with doubt
@dataclass
class Character:
    name:    str
    hp:      int
    max_hp:  int
    atk:     int
    defense: int
    #All the personagens begin of hand empty (None)
    #No começo pareceu estranho, mas depois que voce pede pra IA explicar cada parte, fica claro
    equipped_weapon: Weapon | None = None

    # composicao usando uma classe que usa outra classe, isso e dificil de entender 
    # mas vai simplifica o arquivo em combat.py em 60%
    def attack_roll_dice(self) -> AttackResult:
        
        #A dice of 20 sides
        d20 = randint(1,20)
        
        return AttackResult(
            dice        = d20,              # resultado do d20
            total_atk   = self.atk + d20,   # o ataque inicial do personagem mais o d20
            is_critical = (d20 == 20),      # valor bool
            is_fumble   = (d20 == 1)        # valor bool
        )
    #This gonna equip weapon in personagen
    def equip(self, weapon: Weapon):
        if weapon in self.backpack.items:
            self.equipped_weapon = weapon   
            print(f'🗡️ [{self.name}] equipped the "{weapon.name}"! (+ Damage: {weapon.damage}) \n')
        else:
            print(f'The {self.name} dont have the "{weapon.name}" is in backpack')
            
    def show_status(self):
        arm_name = self.equipped_weapon.name if self.equipped_weapon else "EMPTY HANDS"

        prints = [
            f"[{self.name}]",
            f"❤️ HP:  {self.hp}/{self.max_hp}",
            f"⚔️ ATK: {self.total_attack} ( BASE: {self.atk} + {arm_name})",
            f"🛡️ DEF: {self.defense}"

        ]
        # SE PERSONAGEM TIVER O ATRIBUTUS ELE VAI PRINTAR TBM. "hasattr" = "has attribut?" 
        if hasattr(self, 'mana'):
            prints.append(f"✨ MP: {self.mana}/{self.max_mana}")

        #O "\n" antes do .join diz ao Python: 
        #"Pegue cada s da lista e coloque uma quebra de linha entre eles".
        return "\n".join(prints)
    
    def take_damage(self, damage_amount:int):
        
        #verificar se o dano é maior que zero
        if damage_amount <= 0:
            return
        
        self.hp -= damage_amount
        
        #verificar se o personagem vai ficar com hp negativo, 
        if self.hp < 0: 
            self.hp = 0

        print(f'{self.name} takes {damage_amount} DAMAGE! HP: {self.hp}/{self.max_hp}\n')
   
    def get_defender_value(self) -> tuple[int,int]:
        
        # E o seguinte eu tava achando a defesa muita estatica então decidir deixasr
        # ela ativa, o que quer dizer isso? o defensor vai girar um d10 e somar com a
        # defesa dele.

        # Dado de 10 lados
        d10 = randint(1,10)
                    # Defesa mais um d10 isso é igual a defesa total, assim fica algo dinamico diferente de deixar uma defesa                                
        return d10,(self.defense + d10)
    
#CREATE PLAYER AND ENYMEN
@dataclass
class Player(Character):
    mana:     int = 4
    level:    int = 1
    backpack: Inventory = field(default_factory = Inventory)
@dataclass
class Enemy(Character):
    xp_rewards: int = 10 # hom much XP the player gets for killing this enemys

