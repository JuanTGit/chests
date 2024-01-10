import random

class Chest:
    keys = {
        'elite': random.randint(0, 100),
        'master': random.randint(0, 100),
        'insane': random.randint(0, 100),
        'ultimate': random.randint(0, 100)
    }
    key_multi = {
        'elite': random.uniform(.1, 5),
        'master': random.uniform(1.5, 10),
        'insane': random.uniform(2.5, 20),
        'ultimate': random.uniform(10, 40)
    }

    def __init__(self, key):
        self.key = key

    def open(self):
        isOpen = False
        if self.key == 'elite':
            if self.keys['elite'] > 45:
                print(self.keys['elite'])
                isOpen = True
            return isOpen
        elif self.key == 'master':
            if self.keys['master'] > 70:
                print(self.keys['master'])
                isOpen = True
            return isOpen
        elif self.key == 'insane':
            if self.keys['insane'] > 85:
                print(self.keys['insane'])
                isOpen = True
            return isOpen
        elif self.key == 'ultimate':
            if self.keys['ultimate'] > 95:
                print(self.keys['ultimate'])
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
            print(f'Worth {int(self.value * self.key_multi[self.key])}')
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
            print(f'Worth {int(self.value * self.key_multi[self.key])}')
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
            print(f'Worth {int(self.value * self.key_multi[self.key])}')
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
            print(f'Worth {int(self.value * self.key_multi[self.key])}')
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
            print(f'Worth {int(self.value * self.key_multi[self.key])}')
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
            print(f'Worth {int(self.value * self.key_multi[self.key])}')
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
            print(f'Worth {int(self.value * self.key_multi[self.key])}')
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
            print(f'Worth {int(self.value * self.key_multi[self.key])}')
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
            print(f'Worth {int(self.value * self.key_multi[self.key])}')
            return int(self.value * self.key_multi[self.key])
        else:
            print(f'{self.key.title()} 3rd Age Chest')
            print('Your key gets stuck in the ancient lock and crumbles to dust.')
            return 0



    

def run():
    player_gold = 1_000_000_000
    while player_gold > 300_000:
        key = input(f'You have {player_gold}! Pick a chest elite/master/insane/ultimate: ')
        chest = input(f'Pick a chest! m/g/s/c/ec/bs/l/b/3a: ')
        if chest == 'm':
            player_gold -= Muddy(key).value
            player_gold += Muddy(key).multiplier()
            print(f'Gold: {player_gold}')
            return
        elif chest == 'g':
            player_gold -= Grubby(key).value
            player_gold += Grubby(key).multiplier()
            print(f'Gold: {player_gold}')
            return
        elif chest == 's':
            player_gold -= Sinister(key).value
            player_gold += Sinister(key).multiplier()
            print(f'Gold: {player_gold}')
            return
        elif chest == 'c':
            player_gold -= Crystal(key).value
            player_gold += Crystal(key).multiplier()
            print(f'Gold: {player_gold}')
            return
        elif chest == 'ec':
            player_gold -= EnhancedCrystal(key).value
            player_gold += EnhancedCrystal(key).multiplier()
            print(f'Gold: {player_gold}')
            return
        elif chest == 'bs':
            player_gold -= Brimstone(key).value
            player_gold += Brimstone(key).multiplier()
            print(f'Gold: {player_gold}')
            return
        elif chest == 'l':
            player_gold -= Larrans(key).value
            player_gold += Larrans(key).multiplier()
            print(f'Gold: {player_gold}')
            return
        elif chest == 'b':
            player_gold -= Barrows(key).value
            player_gold += Barrows(key).multiplier()
            print(f'Gold: {player_gold}')
            return
        elif chest == '3a':
            player_gold -= ThirdAge(key).value
            player_gold += ThirdAge(key).multiplier()
            print(f'Gold: {player_gold}')
            return
        else:
            print('Input Invalid! Please try again.')

run()