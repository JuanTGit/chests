import random
from numerize import numerize


class Chest:

    key_multi = {
        'elite': random.uniform(.1, 5),
        'master': random.uniform(1.5, 10),
        'insane': random.uniform(2.5, 20),
        'ultimate': random.uniform(10, 40)
    }

    def __init__(self, key):
        self.key = key

    def open(self):
        rng = random.randint(0, 100)
        isOpen = False
        if self.key == 'elite':
            if rng > 45:
                print(rng)
                isOpen = True
            return isOpen
        elif self.key == 'master':
            if rng > 70:
                isOpen = True
            return isOpen
        elif self.key == 'insane':
            if rng > 85:
                isOpen = True
            return isOpen
        elif self.key == 'ultimate':
            if rng > 95:
                isOpen = True
            return isOpen
        return isOpen


class Muddy(Chest):
    def __init__(self, key, value = 300000):
        super().__init__(key)
        self.value = value
    
    def multiplier(self):
        if self.open():
            print('Chest Opened! Time to multiply!')
            print(f'Worth {numerize.numerize(int(self.value * self.key_multi[self.key]), 2)}')
            return int(self.value * self.key_multi[self.key])
        else:
            print(f'{self.key.title()} Muddy Chest')
            print('Your key gets stuck in the ancient lock and crumbles to dust.')
            return 0


class Grubby(Chest):
    def __init__(self, key, value = 1_000_000):
        super().__init__(key)
        self.value = value
    
    def multiplier(self):
        if self.open():
            print('Chest Opened! Time to multiply!')
            print(f'Worth {numerize.numerize(int(self.value * self.key_multi[self.key]), 2)}')
            return int(self.value * self.key_multi[self.key])
        else:
            print(f'{self.key.title()} Grubby Chest')
            print('Your key gets stuck in the ancient lock and crumbles to dust.')
            return 0


class Sinister(Chest):
    def __init__(self, key, value = 3_000_000):
        super().__init__(key)
        self.value = value
    
    def multiplier(self):
        if self.open():
            print('Chest Opened! Time to multiply!')
            print(f'Worth {numerize.numerize(int(self.value * self.key_multi[self.key]), 2)}')
            return int(self.value * self.key_multi[self.key])
        else:
            print(f'{self.key.title()} Sinister Chest')
            print('Your key gets stuck in the ancient lock and crumbles to dust.')
            return 0


class Crystal(Chest):
    def __init__(self, key, value = 8_000_000):
        super().__init__(key)
        self.value = value
    
    def multiplier(self):
        if self.open():
            print('Chest Opened! Time to multiply!')
            print(f'Worth {numerize.numerize(int(self.value * self.key_multi[self.key]), 2)}')
            return int(self.value * self.key_multi[self.key])
        else:
            print(f'{self.key.title()} Crystal Chest')
            print('Your key gets stuck in the ancient lock and crumbles to dust.')
            return 0


class EnhancedCrystal(Chest):
    def __init__(self, key, value = 15_000_000):
        super().__init__(key)
        self.value = value
    
    def multiplier(self):
        if self.open():
            print('Chest Opened! Time to multiply!')
            print(f'Worth {numerize.numerize(int(self.value * self.key_multi[self.key]), 2)}')
            return int(self.value * self.key_multi[self.key])
        else:
            print(f'{self.key.title()} Enhanced Crystal Chest')
            print('Your key gets stuck in the ancient lock and crumbles to dust.')
            return 0


class Brimstone(Chest):
    def __init__(self, key, value = 35_000_000):
        super().__init__(key)
        self.value = value
    
    def multiplier(self):
        if self.open():
            print('Chest Opened! Time to multiply!')
            print(f'Worth {numerize.numerize(int(self.value * self.key_multi[self.key]), 2)}')
            return int(self.value * self.key_multi[self.key])
        else:
            print(f'{self.key.title()} Brimstone Chest')
            print('Your key gets stuck in the ancient lock and crumbles to dust.')
            return 0


class Larrans(Chest):
    def __init__(self, key, value = 80_000_000):
        super().__init__(key)
        self.value = value
    
    def multiplier(self):
        if self.open():
            print('Chest Opened! Time to multiply!')
            print(f'Worth {numerize.numerize(int(self.value * self.key_multi[self.key]), 2)}')
            return int(self.value * self.key_multi[self.key])
        else:
            print(f'{self.key.title()} Larrans Chest')
            print('Your key gets stuck in the ancient lock and crumbles to dust.')
            return 0


class Barrows(Chest):
    def __init__(self, key, value = 150_000_000):
        super().__init__(key)
        self.value = value
    
    def multiplier(self):
        if self.open():
            print('Chest Opened! Time to multiply!')
            print(f'Worth {numerize.numerize(int(self.value * self.key_multi[self.key]), 2)}')
            return int(self.value * self.key_multi[self.key])
        else:
            print(f'{self.key.title()} Barrows Chest')
            print('Your key gets stuck in the ancient lock and crumbles to dust.')
            return 0


class ThirdAge(Chest):
    def __init__(self, key, value = 400_000_000):
        super().__init__(key)
        self.value = value
    
    def multiplier(self):
        if self.open():
            print('Chest Opened! Time to multiply!')
            print(f'Worth {numerize.numerize(int(self.value * self.key_multi[self.key]), 2)}')
            return int(self.value * self.key_multi[self.key])
        else:
            print(f'{self.key.title()} 3rd Age Chest')
            print('Your key gets stuck in the ancient lock and crumbles to dust.')
            return 0



    

def run():
    player_gold = 1_000_000_000
    while player_gold > 300_000:
        key = input(f'You have {numerize.numerize(player_gold, 2)}! Pick a key and chest\nelite/master/insane/ultimate\nm/g/s/c/ec/bs/l/b/3a: ').split(' ')

        if key[1] == 'm':
            player_gold -= Muddy(key[0]).value
            player_gold += Muddy(key[0]).multiplier()
            print(f'Gold: {numerize.numerize(player_gold, 2)}')

        elif key[1] == 'g':
            player_gold -= Grubby(key[0]).value
            player_gold += Grubby(key[0]).multiplier()
            print(f'Gold: {numerize.numerize(player_gold, 2)}')

        elif key[1] == 's':
            player_gold -= Sinister(key[0]).value
            player_gold += Sinister(key[0]).multiplier()
            print(f'Gold: {numerize.numerize(player_gold, 2)}')

        elif key[1] == 'c':
            player_gold -= Crystal(key[0]).value
            player_gold += Crystal(key[0]).multiplier()
            print(f'Gold: {numerize.numerize(player_gold, 2)}')

        elif key[1] == 'ec':
            player_gold -= EnhancedCrystal(key[0]).value
            player_gold += EnhancedCrystal(key[0]).multiplier()
            print(f'Gold: {numerize.numerize(player_gold, 2)}')

        elif key[1] == 'bs':
            player_gold -= Brimstone(key[0]).value
            player_gold += Brimstone(key[0]).multiplier()
            print(f'Gold: {numerize.numerize(player_gold, 2)}')

        elif key[1] == 'l':
            player_gold -= Larrans(key[0]).value
            player_gold += Larrans(key[0]).multiplier()
            print(f'Gold: {numerize.numerize(player_gold, 2)}')

        elif key[1] == 'b':
            player_gold -= Barrows(key[0]).value
            player_gold += Barrows(key[0]).multiplier()
            print(f'Gold: {numerize.numerize(player_gold, 2)}')

        elif key[1] == '3a':
            player_gold -= ThirdAge(key[0]).value
            player_gold += ThirdAge(key[0]).multiplier()
            print(f'Gold: {numerize.numerize(player_gold, 2)}')

        else:
            print('Input Invalid! Please try again.')

run()