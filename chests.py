import random
import time
from numerize import numerize


class Chest:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.key_multi = {
        'elite': random.uniform(.1, 5),
        'master': random.uniform(1.5, 10),
        'insane': random.uniform(2.5, 20),
        'ultimate': random.uniform(10, 40)
        }

    def open(self):
        rng = random.randint(0, 100)
        isOpen = False
        if self.key == 'elite' and rng > 45:
            isOpen = True
        elif self.key == 'master' and rng > 70:
            isOpen = True
        elif self.key == 'insane' and rng > 85:
            isOpen = True
        elif self.key == 'ultimate' and rng > 95:
            isOpen = True
        return isOpen
    
    def multiplier(self):
        print('\n\tOpening...')
        time.sleep(1.5)
        if self.open():
            print('\n\tChest Opened!')
            print('\t==============================')
            print(f'\tChest worth: {numerize.numerize(int(self.value * self.key_multi[self.key]), 2)}')
            print('\t==============================')
            print('\t==============================')
            return int(self.value * self.key_multi[self.key])
        else:
            print(f'\n\t{self.key.title()} {self.__class__.__name__} Chest')
            print('\t==============================')
            print('\tYour key gets stuck in the \n\tancient lock and \n\tcrumbles to dust.')
            print('\t==============================')
            return 0


class Muddy(Chest):
    def __init__(self, key, value = 300000):
        super().__init__(key, value)

class Grubby(Chest):
    def __init__(self, key, value = 1_000_000):
        super().__init__(key, value)

class Sinister(Chest):
    def __init__(self, key, value = 3_000_000):
        super().__init__(key, value)

class Crystal(Chest):
    def __init__(self, key, value = 8_000_000):
        super().__init__(key, value)

class EnhancedCrystal(Chest):
    def __init__(self, key, value = 15_000_000):
        super().__init__(key, value)

class Brimstone(Chest):
    def __init__(self, key, value = 35_000_000):
        super().__init__(key, value)

class Larrans(Chest):
    def __init__(self, key, value = 80_000_000):
        super().__init__(key, value)

class Barrows(Chest):
    def __init__(self, key, value = 150_000_000):
        super().__init__(key, value)

class ThirdAge(Chest):
    def __init__(self, key, value = 400_000_000):
        super().__init__(key, value)


def run():
    player_gold = 1_000_000_000
    while player_gold > 300_000:
        key = input(f'\n\tYou have {numerize.numerize(player_gold, 2)}! Pick a key and chest\n\telite/master/insane/ultimate\n\tm/g/s/c/ec/bs/l/b/3a: ').split(' ')

        chest_types = {'m': Muddy, 'g': Grubby, 's': Sinister, 'c': Crystal, 'ec': EnhancedCrystal,
                       'bs': Brimstone, 'l': Larrans, 'b': Barrows, '3a': ThirdAge}
        
        try:
            amount = int(key[2])
        except:
            amount = 1

        if key[0] == 'q':
            print(f'\n\tRemaining balance: {numerize.numerize(player_gold, 2)}!\n\tThank you for playing!')
            return

        while amount > 0:
            if len(key) >= 2 and key[1] in chest_types:
                chest = chest_types[key[1]](key[0])
                player_gold -= chest.value
                player_gold += chest.multiplier()
                print(f'\tGold: {numerize.numerize(player_gold, 2)}')
                print('\t==============================')
                amount -= 1
            else:
                print('\tInput Invalid! Please try again.')
                break

run()