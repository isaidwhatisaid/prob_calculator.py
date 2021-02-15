import random

class Hat:

    def __init__(self, **ball_counts):
        self.contents = []
        for colour, count in ball_counts.items():
            self.contents += [colour]*count
    
    def draw(self, number):
        if number >= len(self.contents):
            random_choices = random.sample(self.contents,k=len(self.contents))
            self.contents.clear()
        else: 
            random_choices = random.sample(self.contents,k=number)
            for choice in random_choices:
                self.contents.remove(choice)
        return random_choices

    

hat = Hat(yellow=3, blue=2, green=6)
print(hat.contents)
print(hat.draw(10))
print(hat.contents)