import random

class Chest:
    keys = {
        'elite': random.randint(0, 100),
        'master': random.randint(0, 100),
        'insane': random.randint(0, 100),
        'ultimate': random.randint(0, 100)
    }
    def __init__(self, key):
        self.key = key

    def open(self):
        isOpen = False
        if self.key == 'elite':
            if self.keys['elite'] > 40:
                print(self.keys['elite'])
                isOpen = True
        if isOpen:
            print('Chest Cracked!')


class Muddy(Chest):
    def __init__(self, key):
        super().__init__(key)
    


test_chest = Chest('elite')
# test_chest.open()

muddy_chest = Muddy('elite')

muddy_chest.open()