# item_pool.py
from items import Weapon, Consumable

# Criamos um dicionário que funciona como o nosso "Catálogo" de armas disponíveis no jogo
WEAPONS = {
    "iron_sword": Weapon(
        name="Iron Sword",
        description="Um a espada de ferro simples.",
        weight=10.0,
        value=20,
        damage=8,
    ),
    "excalibur": Weapon(
        name="Excalibur",
        description="A lendária espada do Rei Arthur. Brilha com poder sagrado.",
        weight=8.5,
        value=500,
        damage=25,
    ),
}

# Criamos um dicionário para o catálogo de consumíveis
CONSUMABLES = {
    "health_potion": Consumable(
        name="Health Potion",
        description="Recupera 20 de HP.",
        weight=1.0,
        value=10,
        heal_amount=20,
    ),
    "mega_potion": Consumable(
        name="Mega Potion",
        description="Recupera 50 de HP. Gosto amargo.",
        weight=1.5,
        value=35,
        heal_amount=50,
    ),
}
