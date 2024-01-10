import random

class Chest:
    keys = {
        'elite': random.randint(0, 100),
        'master': random.randint(0, 100),
        'insane': random.randint(0, 100),
        'ultimate': random.randint(0, 100)
    }
    key_multi = {
        'elite': random.uniform(.1, 30),
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
        print(f'{self.key} Chest')
        print('Your key gets stuck in the ancient lock and crumbles to dust.')


class Muddy(Chest):
    def __init__(self, key, value = 300000):
        super().__init__(key)
        self.value = value
    
    def multiplier(self):
        if self.open():
            print('Chest Opened! Time to multiply!')
            print(f'Worth {int(self.value * self.key_multi[self.key])}')


class Muddy(Chest):
    def __init__(self, key, value = 300_000):
        super().__init__(key)
        self.value = value
    
    def multiplier(self):
        if self.open():
            print('Chest Opened! Time to multiply!')
            print(f'Worth {int(self.value * self.key_multi[self.key])}')


class Grubby(Chest):
    def __init__(self, key, value = 1_000_000):
        super().__init__(key)
        self.value = value
    
    def multiplier(self):
        if self.open():
            print('Chest Opened! Time to multiply!')
            print(f'Worth {int(self.value * self.key_multi[self.key])}')


class Sinister(Chest):
    def __init__(self, key, value = 3_000_000):
        super().__init__(key)
        self.value = value
    
    def multiplier(self):
        if self.open():
            print('Chest Opened! Time to multiply!')
            print(f'Worth {int(self.value * self.key_multi[self.key])}')


class Crystal(Chest):
    def __init__(self, key, value = 8_000_000):
        super().__init__(key)
        self.value = value
    
    def multiplier(self):
        if self.open():
            print('Chest Opened! Time to multiply!')
            print(f'Worth {int(self.value * self.key_multi[self.key])}')


class EnhancedCrystal(Chest):
    def __init__(self, key, value = 15_000_000):
        super().__init__(key)
        self.value = value
    
    def multiplier(self):
        if self.open():
            print('Chest Opened! Time to multiply!')
            print(f'Worth {int(self.value * self.key_multi[self.key])}')


class Brimstone(Chest):
    def __init__(self, key, value = 35_000_000):
        super().__init__(key)
        self.value = value
    
    def multiplier(self):
        if self.open():
            print('Chest Opened! Time to multiply!')
            print(f'Worth {int(self.value * self.key_multi[self.key])}')


class Larrans(Chest):
    def __init__(self, key, value = 80_000_000):
        super().__init__(key)
        self.value = value
    
    def multiplier(self):
        if self.open():
            print('Chest Opened! Time to multiply!')
            print(f'Worth {int(self.value * self.key_multi[self.key])}')


class Barrows(Chest):
    def __init__(self, key, value = 150_000_000):
        super().__init__(key)
        self.value = value
    
    def multiplier(self):
        if self.open():
            print('Chest Opened! Time to multiply!')
            print(f'Worth {int(self.value * self.key_multi[self.key])}')


class ThirdAge(Chest):
    def __init__(self, key, value = 400_000_000):
        super().__init__(key)
        self.value = value
    
    def multiplier(self):
        if self.open():
            print('Chest Opened! Time to multiply!')
            print(f'Worth {int(self.value * self.key_multi[self.key])}')



    


test_chest = Chest('elite')
# test_chest.open()

muddy_chest = Muddy('elite')

# muddy_chest.open()

muddy_chest.multiplier()