import random
from game import constants
from game.actor import Actor
from game.point import Point

# TODO: Define the Food class here...
    # then comment out the calls to this class in the director. 

class Food(Actor):
    """
    Responsiblility of the food class is to generate food. 

    Sterotype: 
        ???


    """

    def __init__(self):
        super().__init__()

        self.points = 0 
        self.set_text('0')

        self.set_height(constants.DEFAULT_SQUARE_LENGTH)
        self.set_width(constants.DEFAULT_SQUARE_LENGTH)
        self.reset()

    

    def get_points(self):
        """
        Generates a random number that gets passed into the food box. 
        """
        # I think I will need to call the constants and 
        # then call other things from point to get a random point on the gui
        # will need to call actor.get_text() to insert into get_text the random number
        
        return self._points

    def reset(self):
        '''
        
        '''
        self._points = random.randint(1, 10)
        self.set_text(str(self._points))

        x = random.randint(1, constants.MAX_X - 2)
        y = random.randint(1, constants.MAX_Y - 2)
        position = Point(x, y)
        self.set_position(position)



