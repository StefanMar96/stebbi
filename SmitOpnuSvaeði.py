import random

class SmitOpnuSvaeði:
    def roll_dice():
        number = random.randint(1, 100)
        if number >= 30:
            #print("True")
            return True
        else:
            #print("False")
            return False
