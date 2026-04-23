from items     import Weapon,Consumable
from character import Player, Enemy
from combat    import Combat
#from inventory import Inventory

#create items (swod and potion) 
weapon1  = Weapon('Iron Sword', 'A Sword forjed with iron, very carry, because it cut ',10.0, 20, 8)
potion1  = Consumable('Health Potion','Recover your HP, this tastes like grapes.',1.0,10,20)

#create a player
print("\n--- PLAYER INFO ---")
player1 = Player(
    name    ='witalo',
    hp      =100,
    max_hp  =100,
    atk     =12,
    defense =18,
    mana    =6
)
print(player1)# dont can print the player 

#create a enemy
print("\n--- ENEMY INFO ---")
# No enemy1
enemy1 = Enemy(
    name="Goblin", 
    hp        =58, 
    max_hp    =58, 
    atk       =10, 
    defense   =8, 
    xp_rewards=100
)
print(enemy1)

#player put items in backpack
player1.backpack.add_item(weapon1)
player1.backpack.add_item(potion1)
player1.backpack.show_inventory()

#remove a item of backpack
player1.backpack.rmv_item(weapon1)
player1.backpack.show_inventory()

#System of combat, without weapon equipped.
print(f'{"="*15}Round 1{"="*15}\n')

Combat.battle(player1,enemy1)  # player 1 is attacking
Combat.battle(enemy1,player1)  # player 1 is defensor

#Test of new funtion total_attack (atk_standard more weapon) 22/04/2026
#The player taked arm
player1.backpack.add_item(weapon1)
player1.equip(weapon1)              #for equipped arm have that before is in backpack

#Fight 2 round, with modification in system of combat and use arm
print(f'{"="*15}Round 2{"="*15}\n')

Combat.battle(player1,enemy1) #Turn of player1
Combat.battle(enemy1,player1) #Turn of enemy1 




