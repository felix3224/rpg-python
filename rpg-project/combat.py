import random


class Combat:
    @staticmethod
    def roll_dice(side: int) -> int:
        """Rolls a dice with the given number of sides (e.g., 20)"""
        return random.randint(1, side)

    @staticmethod
    def battle(attacker, defender):
        print(f"[{attacker.name}] is attacking [{defender.name}]!!\n")

        # Integração da mecânica da classe Character usando encapsulamento!
        attack_result = attacker.attack_roll_dice()
        dice_atk = attack_result.dice
        total_atk = attack_result.total_atk

        # Aqui vemos a defesa ativa do oponente.
        dice_def, total_def = defender.get_defender_value()

        # Dano total
        total_damage = attacker.calculate_damage()

        print(f" DICE_ATK: ({dice_atk}) | DICE_DEF: ({dice_def})\n")
        print(f"⚔️ ATAQUE: {total_atk} vs 🛡️ DEFESA: {total_def}\n")

        # Sucesso Crítico verificado pela flag do objeto
        if attack_result.is_critical:
            total_damage *= 2
            print("Attack critical!!!\n")
            print(
                f'[{attacker.name}] found an OPENING!!! and dealt DAMAGE!, [{defender.name}] - "AAARGHHH!!!" '
            )
            defender.take_damage(total_damage)

        # Falha Crítica verificada pela flag do objeto
        elif attack_result.is_fumble:
            print("-Do you know what luck is? It's what you don't have. \n")
            print(f"[{attacker.name}] got it right himself!!!\n")
            attacker.take_damage(total_damage)

        # Ataque normal bem-sucedido
        elif total_atk >= total_def:
            print(
                f'[{attacker.name}] found an OPENING!!! and dealt DAMAGE!, [{defender.name}] - "Aaarghh!" '
            )
            defender.take_damage(total_damage)

        # Ataque falhado (Miss)
        else:
            print(f"Attack FAIL!! - [{attacker.name}] didn't cause damage \n")
