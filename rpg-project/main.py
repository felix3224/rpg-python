from items     import Weapon,Consumable
from character import Player, Enemy
from combat    import Combat
#from inventory import Inventory

#create items (swod and potion) 
weapon1 = Weapon('Iron Sword', 'A Sword forjed with iron, very carry, because it cut ',10.4, 20, 8)
potion1  = Consumable('Health Potion','Recover your HP, this tastes like grapes.',1.0,10,20)

#create a player
print("\n--- PLAYER INFO ---")
player1 = Player('Hiury',100,100,12,18,4,)
print(player1)# dont can print the player 

#create a enemy
print("\n--- ENEMY INFO ---")
enemy1 = Enemy('Goblin',58,58,10,8,3)
print(enemy1)

#player put items in backpack
player1.backpack.add_item(weapon1)
player1.backpack.add_item(potion1)
player1.backpack.show_inventory()
player1.backpack.rmv_item(weapon1)
player1.backpack.show_inventory()

#System of combat
Combat.battle(player1,enemy1)  # player 1 is attacking
Combat.battle(enemy1,player1)  # player 1 is defensor

