# main.py
import os
from npc import NpcAI
from character import Player, Enemy
from combat import Combat
from database import WEAPONS, CONSUMABLES, ENEMIES  # Importando ENEMIES do database
from shop import Merchant  # Importando nosso Mercador ambulante


def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


def executar_combate(player: Player, enemy: Enemy) -> bool:
    """
    Gerencia o loop de combate em turnos contra um inimigo específico.
    Retorna True se o player vencer, False se morrer ou fugir.
    """
    round_count = 1
    print(f"\n⚔️  O COMBATE COMEÇOU! {player.name} VS {enemy.name} ⚔️\n")

    while enemy.hp > 0 and player.hp > 0:
        print(f"\n--- ⏳ ROUND {round_count} ---")
        print(
            f"❤️  Seu HP: {player.hp}/{player.max_hp} | ❤️  HP do Inimigo: {enemy.hp}/{enemy.max_hp}"
        )
        print("-" * 40)
        print("1. ⚔️  Atacar")
        print("2. 🎒 Abrir Mochila")
        print("3. 📊 Ver Status")
        print("4. 🏃 Fugir")
        print("-" * 40)

        escolha = input("Escolha sua ação: ").strip()

        # ---- OPÇÃO 1: ATACAR ----
        if escolha == "1":
            limpar_tela()
            # Turno do Player
            Combat.battle(player, enemy)

            # Se o inimigo ainda estiver vivo, ele contra-ataca
            if enemy.hp > 0:
                print(f"⚡ REAÇÃO: O [{enemy.name}] se recupera e avança contra você!")
                Combat.battle(enemy, player)

            round_count += 1

        # ---- OPÇÃO 2: ABRIR MOCHILA ----
        elif escolha == "2":
            limpar_tela()
            while True:
                print("\n" + "=" * 15 + " 🎒 SUA MOCHILA " + "=" * 15)
                if not player.backpack.items:
                    print("Sua mochila está completamente vazia!")
                    print("=" * 46)
                    input("\nPressione Enter para voltar...")
                    break

                # Lista os itens
                for idx, item in enumerate(player.backpack.items, start=1):
                    print(f"{idx}. {item.name}")
                print("0. Voltar ao menu de combate ↩️")
                print("=" * 46)

                opc = input(
                    "Escolha um item para inspecionar/usar (ou 0 para voltar): "
                ).strip()
                if opc == "0":
                    break

                if (
                    not opc.isdigit()
                    or int(opc) < 1
                    or int(opc) > len(player.backpack.items)
                ):
                    print("❌ Opção inválida!")
                    continue

                item_selecionado = player.backpack.items[int(opc) - 1]

                print("\n" + "-" * 15 + " DETALHES DO ITEM " + "-" * 15)
                print(item_selecionado.get_detailed_info())
                print("-" * 48)
                print("1. 👍 Usar/Equipar ")
                print("2. 🗑️  Descartar Item")
                print("0. ↩️  Voltar")

                acao = input("O que deseja fazer? ").strip()

                if acao == "0":
                    continue
                elif acao == "1":
                    if hasattr(item_selecionado, "damage"):  # É uma arma
                        player.equip(item_selecionado)
                    elif hasattr(item_selecionado, "heal_amount"):  # É uma poção
                        item_selecionado.use(player)
                        player.backpack.rmv_item(item_selecionado)

                        # Beber poção gasta turno: inimigo ataca!
                        print(
                            f"\n⚡ OPORTUNIDADE: Enquanto você se curava, o [{enemy.name}] atacou!"
                        )
                        Combat.battle(enemy, player)
                    break
                elif acao == "2":
                    if player.equipped_weapon == item_selecionado:
                        player.equipped_weapon = None  # Desequipa se for a arma atual
                    player.backpack.rmv_item(item_selecionado)
                    print(f'🗑️ Você descartou "{item_selecionado.name}".')
                    break

            if player.hp <= 0:
                return False

        # ---- OPÇÃO 3: VER STATUS ----
        elif escolha == "3":
            limpar_tela()
            print("--- SEU STATUS ---")
            print(player.show_status())
            print("\n--- STATUS DO INIMIGO ---")
            print(enemy.show_status())

        # ---- OPÇÃO 4: FUGIR ----
        elif escolha == "4":
            print(
                f"\n🏃 [{player.name}] largou as armas e fugiu correndo da batalha chorando!"
            )
            return False
        else:
            print("❌ Opção inválida!")

    # Fim do While: Alguém morreu
    if player.hp <= 0:
        print(f"\n💀 GAME OVER! Você foi derrotado por [{enemy.name}]...")
        return False
    elif enemy.hp <= 0:
        print(f"\n🎉 VITÓRIA! Você derrotou [{enemy.name}]!")
        # Recompensa em Ouro!
        player.gold += enemy.gold_reward
        print(
            f"🪙 Você saqueou o corpo do monstro e encontrou 💰 {enemy.gold_reward} moedas de ouro!"
        )
        return True


# ==============================================================================
# 2. FLUXO PRINCIPAL DA JORNADA DO HERÓI
# ==============================================================================
if __name__ == "__main__":
    limpar_tela()
    print("\n ---- ⚔️ A JORNADA DO HERÓI COMEÇOU ⚔️ ----\n")

    # Setup Inicial do Player
    player1 = Player(
        name="Witalo",
        hp=100,
        max_hp=100,
        atk=12,
        defense=8,
        mana=6,
        max_mana=6,
        gold=10,  # Começa com 10 moedas de reserva
    )

    # Itens Iniciais
    player1.backpack.add_item(WEAPONS["iron_sword"])
    player1.backpack.add_item(CONSUMABLES["health_potion"])
    player1.equip(WEAPONS["iron_sword"])

    input("\nPressione Enter para iniciar a história...")
    limpar_tela()

    # --------------------------------------------------------------------------
    # FASE 1: NPC Camponês & O Goblin
    # --------------------------------------------------------------------------
    print("=" * 50)
    print("[👨‍🌾 NPC Camponês]: Um Goblin Saqueador invadiu as")
    print('nossas plantações🌾 e está roubando nossas colheitas!!! "')
    print("=" * 50)

    NpcAI.conversar_com_campones(player_name=player1.name)
    # O "Gancho" inteligente que você desenhou:
    while True:
        print("\nE então, jovem herói, você vai caçar o terrível Goblin?")
        print("1 - Sim, eu vou!")
        print("2 - Não, ainda não estou pronto (Ver Status)")

        gancho = input("Sua resposta: ").strip()

        if gancho == "1":
            print('\n[NPC Camponês]: "Muito obrigado! Que os deuses te guiem!"')
            break
        elif gancho == "2":
            limpar_tela()
            print("\nVocê respira fundo, se concentra e checa suas condições:")
            print("-" * 30)
            print(player1.show_status())
            print("-" * 30)
        else:
            print("❌ Escolha apenas 1 ou 2.")

    # Inicia a luta contra o Goblin cadastrado no database
    goblin = ENEMIES["goblin"]
    venceu = executar_combate(player1, goblin)

    if not venceu:
        print("\nA sua jornada terminou antes mesmo de começar...")
        exit()  # Fecha o jogo se morrer ou fugir

    input("\nPressione Enter para continuar viagem...")
    limpar_tela()

    # --------------------------------------------------------------------------
    # FASE 2: O Mercador Ambulante
    # --------------------------------------------------------------------------
    # Abre a loja passando o jogador por parâmetro
    Merchant.open_shop(player1)

    input("Pressione Enter para seguir viagem pela estrada escura...")
    limpar_tela()

    # --------------------------------------------------------------------------
    # FASE 3: O Esqueleto
    # --------------------------------------------------------------------------
    print("=" * 50)
    print(
        "O vento sopra frio. Entre as lápides de um velho cemitério na beira da estrada,"
    )
    print(
        "um som de ossos batendo ecoa. Um Esqueleto Guardião se levanta com uma espada enferrujada!"
    )
    print("=" * 50)
    input("\n[Prepare-se para lutar!] Pressione Enter...")

    esqueleto = ENEMIES["skeleton"]
    venceu = executar_combate(player1, esqueleto)

    if not venceu:
        print("\nOs seus ossos agora farão companhia ao esqueleto na estrada...")
        exit()

    input("\nPressione Enter para continuar...")
    limpar_tela()

    # --------------------------------------------------------------------------
    # FASE 4: NPC em Perigo & O Boss Final (Rato Gigante)
    # --------------------------------------------------------------------------
    print("=" * 50)
    print("De repente, você ouve passos rápidos e descontraídos na sua direção.")
    print("Uma jovem camponesa passa correndo desesperada e grita:")
    print(
        '\n[👩 NPC em Perigo]: "ALGUÉM ME SALVE! TEM UM RATO GORDO NOJENTO ATRÁS DE MIM!!!"'
    )
    print("=" * 50)
    print(
        "\nAtrás dela, surge uma criatura imensa, do tamanho de um urso, babando e com dentes afiados."
    )
    input(
        "\n[É a batalha final!] Pressione Enter para enfrentar o Rato Gigante Gordo..."
    )

    rato = ENEMIES["giant_rat"]
    venceu = executar_combate(player1, rato)

    if not venceu:
        print("\nVocê virou comida de rato de esgoto... Que fim trágico.")
        exit()

    # --------------------------------------------------------------------------
    # FIM DE JOGO: Vitória Total
    # --------------------------------------------------------------------------
    limpar_tela()
    print("=" * 60)
    print(f" ✨ PARABÉNS, {player1.name.upper()}!!! ✨")
    print("=" * 60)
    print("Você derrotou as 3 criaturas mais temíveis da região!")
    print("Os camponeses fazem uma festa em sua homenagem e o seu nome")
    print("será lembrado para sempre como o do Verdadeiro Herói dessas terras.")
    print("\n Obrigado por jogar o RPG-Python! FIM! 🎉")
    print("=" * 60)
