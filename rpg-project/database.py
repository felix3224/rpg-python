# database.py completo e atualizado para a campanha
from items import Weapon, Consumable
from character import Enemy

# Equipamentos (Armas e Armaduras no futuro)
WEAPONS = {
    "iron_sword": Weapon(
        name="Iron Sword",
        description="Uma espada de ferro simples.",
        weight=10.0,
        value=20,  # Preço de compra/venda no mercador
        damage=8,
    ),
    "steel_axe": Weapon(
        name="Steel Axe",
        description="Um machado pesado de aço, causa cortes profundos.",
        weight=14.0,
        value=50,
        damage=14,
    ),
    "excalibur": Weapon(
        name="Excalibur",
        description="A lendária espada que brilha com poder sagrado.",
        weight=8.5,
        value=200,
        damage=25,
    ),
}

# Consumíveis
CONSUMABLES = {
    "health_potion": Consumable(
        name="Health Potion",
        description="Recupera 20 de HP.",
        weight=1.0,
        value=15,
        heal_amount=20,
    ),
    "mega_potion": Consumable(
        name="Mega Potion",
        description="Recupera 50 de HP. Gosto amargo.",
        weight=1.5,
        value=40,
        heal_amount=50,
    ),
}

# 📑 NOVO: Catálogo de Inimigos para a sua jornada!
ENEMIES = {
    "goblin": Enemy(
        name="Goblin Saqueador",
        hp=45,
        max_hp=45,
        atk=8,
        defense=5,
        xp_rewards=50,
        gold_reward=50,  # Dropa 20 moedas
    ),
    "skeleton": Enemy(
        name="Esqueleto Guardião 💀",
        hp=60,
        max_hp=60,
        atk=12,
        defense=10,
        xp_rewards=100,
        gold_reward=70,
    ),
    "giant_rat": Enemy(
        name="Rato Gigante Gordo 🐀",
        hp=85,
        max_hp=85,
        atk=16,
        defense=12,
        xp_rewards=200,
        gold_reward=0,  # É o boss final, o jogo acaba aqui!
    ),
}
