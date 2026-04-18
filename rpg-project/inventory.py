from dataclasses import dataclass, field 
from items       import Item

@dataclass
class Inventory:
    # default_factory=list guarantees every inventory gets its own empty list
    bag: list[Item] = field(default_factory=list)

    def add_item(self, item: Item):
        self.bag.append(item)
        print(f'Picked up: {item.name} \n')

    def rmv_item(self, item: Item):
        if item in self.bag:
            self.bag.remove(item)
            print(f'"{item.name}" was remove of backpack!\n')
        else:
            print(f"{item} don't is in the backpack\n")

    def show_inventory(self):
        print(f' {"="*5}bag{"="*5} \n')

        if len(self.bag) == 0:
            print('Your backpack is Empty!\n')

        else:
            for item in self.bag:
                print(f'{item.name}:\n ')
                print(f' Weight: {item.weight} kg\n')
                print(f' Value : {item.value}  gold\n')

        print(f'{"="*15}\n')


        
