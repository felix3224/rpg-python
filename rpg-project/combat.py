import random

class Combat:
    #this dont need of a self. because just rolla dice and no go modify some
    @staticmethod
    def roll_dice(side: int) -> int:
        """Rolls a dice with the given number of sides (e.g., 20)"""
        return random.randint(1,side)
    
    #Here is the same thing, dont need of none 
    @staticmethod
    def battle(attacker, defender):
        print(f'[{attacker.name}] is attacking [{defender.name}]!!\n')

        #Aqui vamos ver o ataque do atacante 
        dice_atk = Combat.roll_dice(20)
        total_atk = dice_atk + attacker.atk

        #Aqui vamos ver a defesa do oponente.
        dice_def,total_def = defender.get_defender_value()

        #Para o ataque de maõs vazias do personagem e tambem para auxiliar no dano. assim da um balancemanto
        dmg_standard = attacker.atk // 2

        # Pega o dano da arma OU 0 se estiver desarmado
        weapon_dmg = attacker.equipped_weapon.damage if attacker.equipped_weapon else 0
        
        #Damage total. weapon_dmg + dmg_standard
        total_damage = weapon_dmg + dmg_standard

        print(f' DICE_ATK: ({dice_atk}) | DICE_DEF: ({dice_def})\n')
        print(f"⚔️ ATAQUE: {total_atk} vs 🛡️ DEFESA: {total_def}\n")
        
        #The Damage 2x when is 20 in dice_atk
        if dice_atk == 20:
            
            total_damage *= 2 #When the dice_atk is equal 20, damage 2x

            print('Atack critical!!!\n')
            print(f'[{attacker.name}] found an OPENING!!! and dealt DAMAGE!, [{defender.name}] - "AAARGHHH!!!" ')        
            defender.take_damage(total_damage)

        #My grandmather make to better that it
        elif dice_atk == 1:
            
            print("-Do you know what luck is? It's what you don't have. \n")
            print(f'[{attacker.name}] got it right himself!!!"\ n')
            
            attacker.take_damage(dmg_standard) 

        #Ataque normal
        elif total_atk >= total_def:
            
            print(f'[{attacker.name}] found an OPENING!!! and dealt DAMAGE!, [{defender.name}] - "Aaarghh!" ')                           
            defender.take_damage(total_damage)

        #Miss Normal
        else:
            print(f'Atack FAILL!! - [{attacker.name}] dont cause damge  \n')
                