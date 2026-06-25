from character import Player, Enemy
from items import Weapon, Consumable
from combat import Combat
from database import WEAPONS, CONSUMABLES
# ==============================================================================
# 1. CONFIGURAÇÃO INICIAL (SETUP DO JOGO)
# ==============================================================================

# Criamos as instâncias dos itens usando argumentos nomeados (Boa prática de POO)
# para evitar que quebras ocorram se mudarmos a ordem dos atributos no futuro.
weapon1 = WEAPONS["iron_sword"]
potion1 = CONSUMABLES["health_potion"]

# Criamos o Herói (Jogador)
player1 = Player(
    name="Witalo",
    hp=100,
    max_hp=100,
    atk=9,
    defense=7,
    mana=6,
    max_mana=6,  # Sincronizado com a mana inicial
)

# Criamos o Monstro (Inimigo)
enemy1 = Enemy(name="Goblin", hp=58, max_hp=58, atk=10, defense=8, xp_rewards=100)

print("\n ----A jornada do Bravo Guerreio começou!!!----\n")

# Colocamos os itens iniciais na mochila do jogador (Composição em ação!)
player1.backpack.add_item(weapon1)
player1.backpack.add_item(potion1)

# Equipamos a espada logo no início para o herói não lutar de mãos vazias
player1.equip(weapon1)

# ==============================================================================
# 2. LOOP PRINCIPAL DE COMBATE (INTERATIVO)
# ==============================================================================

print("\n" + "⚔️ " * 15)
print(f"    O COMBATE COMEÇOU: {player1.name} VS {enemy1.name}!  ")
print("⚔️ " * 15 + "\n")

round_count = 1

# O loop roda ENQUANTO os dois estiverem vivos (HP maior que zero)
while player1.hp > 0 and enemy1.hp > 0:
    print(f"\n================= RODADA {round_count} =================")
    print("Escolha sua ação:")
    print("1. ⚔️ Atacar com a Arma Equipada")
    print("2. 🧃 Abrir Mochila")
    print("3. 📋 Analisar Status (Seu e do Inimigo)")
    print("4. 🏃 Fugir da Batalha (Garante Derrota)")

    # Captura a digitação do usuário no console
    escolha = input("\nDigite o número da ação desejada: ").strip()
    print("\n" + "-" * 40)

    # ---- OPÇÃO 1: ATACAR ----
    if escolha == "1":
        # Turno do Player: Ataca o inimigo
        Combat.battle(player1, enemy1)

        # Verificação pós-ataque: O inimigo morreu?
        if enemy1.hp <= 0:
            print(f"🎉 VITÓRIA! O [{enemy1.name}] foi brutalmente derrotado!")
            print(f"✨ Você recebeu {enemy1.xp_rewards} de XP como recompensa!")
            break  # Encerra o loop do jogo imediatamente

        # Se o inimigo sobreviveu, é o turno dele contra-atacar! (Regra de Game Design)
        print(f"\n⚡ REAÇÃO: O [{enemy1.name}] avança para o contra-ataque!")
        Combat.battle(enemy1, player1)

        # O jogador morreu com o contra-ataque?
        if player1.hp <= 0:
            print("\n💀 GAME OVER! Você tombou em batalha... O Goblin venceu.")
            break

        # Se ambos continuam vivos, avançamos a rodada do jogo
        round_count += 1

    # ---- OPÇÃO 2: ABRIR MOCHILA (REFATORADO) ----
    elif escolha == "2":
        mochila_aberta = True

        while mochila_aberta:
            print("\n" + "=" * 15 + " 🎒 MOCHILA INTERATIVA " + "=" * 15)
            # Se a mochila estiver vazia, avisa e volta pro menu de combate
            if not player1.backpack.items:
                print("Sua mochila está completamente vazia!")
                print("=" * 44)
                break

            # Lista os itens dinamicamente usando enumerate
            print("0. ↩️  Voltar para o Combate")
            for idx, item in enumerate(player1.backpack.items, start=1):
                # Se o item listado for a arma que está equipada, coloca um indicador visual
                status_equip = (
                    " ⚔️ (Equipado)" if player1.equipped_weapon == item else ""
                )
                print(f"{idx}. {item.name}{status_equip}")
            print("=" * 44)

            sub_escolha = input(
                "\nSelecione o número do item que deseja interagir: "
            ).strip()

            if sub_escolha == "0":
                break  # Sai da mochila e volta para o menu de combate (Ação Livre)

            # Validação para garantir que o input é um número válido da lista
            if (
                not sub_escolha.isdigit()
                or int(sub_escolha) < 1
                or int(sub_escolha) > len(player1.backpack.items)
            ):
                print("❌ Seleção inválida! Escolha um número da lista.")
                continue

            idx_item = int(sub_escolha) - 1
            item_selecionado = player1.backpack.items[idx_item]

            # ---- SUBMENU DO ITEM SELECIONADO ----
            item_menu_aberto = True
            while item_menu_aberto:
                print(f"\n  [{item_selecionado.name}]")
                print("0. ↩️  Voltar para a Mochila")
                print("1. 📖 Ver informações detalhadas (Ação Livre)")

                # Exibe a opção contextual baseada no tipo do objeto (Polimorfismo/isinstance)
                if isinstance(item_selecionado, Weapon):
                    if player1.equipped_weapon == item_selecionado:
                        print("2. 🛡️ Desequipar Arma (Ação Pesada)")
                    else:
                        print("2. 🗡️ Equipar Arma (Ação Pesada)")
                elif isinstance(item_selecionado, Consumable):
                    print("2. 🧃 Consumir / Beber (Ação Pesada)")

                print("3. 🗑️ Jogar item fora / Descartar")

                acao = input("\nEscolha a ação desejada: ").strip()

                if acao == "0":
                    break  # Volta para a lista de itens da mochila

                # ---- AÇÃO LIVRE: VER INFORMAÇÕES ----
                elif acao == "1":
                    print("\n" + "📜 " * 15)
                    print(
                        item_selecionado.get_detailed_info()
                    )  # Método polimórfico criado por você!
                    print("📜 " * 15)
                    # Nota: Não altera item_menu_aberto, permitindo escolher outra ação logo em seguida

                # ---- AÇÕES PESADAS: EQUIPAR / CONSUMIR ----
                elif acao == "2":
                    turno_gasto = False

                    # Contexto de Arma
                    if isinstance(item_selecionado, Weapon):
                        if player1.equipped_weapon == item_selecionado:
                            player1.unequip()
                        else:
                            player1.equip(item_selecionado)
                        turno_gasto = True

                    # Contexto de Consumível
                    elif isinstance(item_selecionado, Consumable):
                        item_selecionado.use(player1)
                        player1.backpack.rmv_item(
                            item_selecionado
                        )  # Remove da composição do inventário
                        turno_gasto = True

                    if turno_gasto:
                        # Se gastou o turno, o inimigo se aproveita da oportunidade para atacar!
                        print(
                            f"\n⚡ OPORTUNIDADE: Enquanto você se distraía com seu item, o [{enemy1.name}] atacou!"
                        )
                        Combat.battle(enemy1, player1)

                        if player1.hp <= 0:
                            print(
                                "\n💀 GAME OVER! Você morreu gerenciando seus itens..."
                            )

                        # Passa a rodada e fecha as janelas da mochila para atualizar o estado do combate
                        round_count += 1
                        item_menu_aberto = False
                        mochila_aberta = False

                # ---- AÇÃO: JOGAR FORA ----
                elif acao == "3":
                    # Se o jogador decidir jogar fora a arma que está equipada, desarmamos ele primeiro
                    if player1.equipped_weapon == item_selecionado:
                        player1.unequip()

                    player1.backpack.rmv_item(item_selecionado)
                    print(
                        f'🗑️ Você descartou "{item_selecionado.name}" no chão da masmorra.'
                    )
                    break  # O item não existe mais, quebra o menu dele e volta para a lista da mochila

                else:
                    print("❌ Opção inválida! Digite números de 0 a 3.")

            # Se o jogador morreu na reação do inimigo, quebra o loop externo da mochila também
            if player1.hp <= 0:
                break

    # ---- OPÇÃO 3: VER STATUS ----
    elif escolha == "3":
        # Usamos o método show_status que refatoramos para inspecionar os objetos
        print("--- SEU STATUS ---")
        print(player1.show_status())
        print("\n--- STATUS DO INIMIGO ---")
        print(enemy1.show_status())
        # Nota: Olhar o status não gasta seu turno, você pode decidir sua ação logo em seguida!

    # ---- OPÇÃO 4: FUGIR ----
    elif escolha == "4":
        print(
            f"🏃 [{player1.name}] largou as armas e fugiu correndo da batalha chorando! Que vergonha..."
        )
        break  # Sai do loop e encerra o programa

    # ---- TRATAMENTO DE ERRO ----
    else:
        print("❌ Opção inválida! Digite apenas números de 1 a 4.")
