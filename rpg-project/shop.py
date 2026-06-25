# shop.py
from database import WEAPONS, CONSUMABLES


class Merchant:
    @staticmethod
    def open_shop(player):
        """Abre o menu interativo de compras com o Mercador."""

        # Carrega dinamicamente os itens disponíveis no catálogo do database
        catalogo_loja = []
        for item in WEAPONS.values():
            catalogo_loja.append(item)
        for item in CONSUMABLES.values():
            catalogo_loja.append(item)

        while True:
            print("\n" + "=" * 15 + "👳‍♂️ MERCADOR AMBULANTE " + "=" * 15)
            print(f"💰 Seu Ouro Atual: {player.gold} moedas")
            print("=" * 44)
            print("0. ↩️  Sair da Loja e Continuar sua Jornada")

            # Lista as mercadorias com seus respectivos preços
            for idx, item in enumerate(catalogo_loja, start=1):
                print(f"{idx}. {item.name:<18} | Preço: 💰 {item.value} moedas")
            print("=" * 44)

            escolha = input(
                '\n[Mercador]: "Olá viajante! O que vai querer hoje?" (Digite o número): '
            ).strip()

            if escolha == "0":
                print(
                    '\n[Mercador]: "Tenha cuidado herói, ouvi dizer que tem um esqueleto por essas redondezas..."'
                )
                print("Você se despede do mercador e segue seu caminho.\n")
                break

            # Validação de entrada
            if (
                not escolha.isdigit()
                or int(escolha) < 1
                or int(escolha) > len(catalogo_loja)
            ):
                print("❌ Opção inválida! Escolha um número válido da lista.")
                continue

            idx_item = int(escolha) - 1
            item_selecionado = catalogo_loja[idx_item]

            # Submenu para inspecionar o item antes de gastar o dinheiro
            print("\n" + "-" * 15 + " INSPEÇÃO DE ITEM " + "-" * 15)
            print(item_selecionado.get_detailed_info())  # Polimorfismo em ação!
            print("-" * 48)

            confirmar = (
                input(
                    f"Deseja comprar [{item_selecionado.name}] por 💰 {item_selecionado.value} moedas? (S/N): "
                )
                .strip()
                .upper()
            )

            if confirmar == "S":
                # Verificação de Economia: O jogador tem dinheiro suficiente?
                if player.gold >= item_selecionado.value:
                    player.gold -= item_selecionado.value  # Deduz o ouro
                    player.backpack.add_item(
                        item_selecionado
                    )  # Adiciona à mochila por Composição
                    print(
                        f'✅ [Mercador]: "Excelente escolha! Aqui está o seu [{item_selecionado.name}]."'
                    )
                else:
                    print(
                        '\n❌ [Mercador]: "Ei! Você não tem moedas suficientes para pagar por isso. Vá caçar mais alguns monstros!"'
                    )
            else:
                print(
                    '\n[Mercador]: "Sem problemas. Quer dar uma olhada em outra coisa?"'
                )
