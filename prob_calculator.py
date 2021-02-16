import random, copy

class Hat:
    
    # Initiate contents list and dictionary
    def __init__(self, **ball_counts):
        self.contents = []
        self.dict = {}
        for colour, count in ball_counts.items():
            self.contents += [colour]*count
            self.dict.update({colour:count})
    
    # Function to draw a random list of values from the object instance
    def draw(self, number):
        if number >= len(self.contents):
            random_choices = random.sample(self.contents,k=len(self.contents))
            self.contents.clear()
        else: 
            random_choices = random.sample(self.contents,k=number)
            for choice in random_choices:
                self.contents.remove(choice)
        return random_choices

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    # Use hat.draw to draw the correct amount of balls the specified amount of times
    count = 0
    for i in range(num_experiments):
        # Make a copy of the hat object so it can be re-used for each draw
        hat_copy = copy.deepcopy(hat)
        # Create a variable for each draw
        one_draw = hat_copy.draw(num_balls_drawn)
        # Make a dictionary with the drawn values
        one_draw_dict = {}
        for i in one_draw:
            if i not in one_draw_dict:
                one_draw_dict[i] = 1
            else:
                one_draw_dict[i] += 1
        # Check if the expected balls are in the draw
        i_count = 0
        for i in expected_balls:
            if i in one_draw_dict and one_draw_dict[i] >= expected_balls[i]:
                i_count += 1
            else: continue
        if i_count == len(expected_balls):
            count += 1
    # Return the probability
    return count/num_experiments

    
# Testers
hat = Hat(yellow=5,red=1,green=3,blue=9,test=1)
probability = experiment(hat=hat, expected_balls={"yellow":2,"blue":3,"test":1}, num_balls_drawn=20, num_experiments=100)
print(probability)
