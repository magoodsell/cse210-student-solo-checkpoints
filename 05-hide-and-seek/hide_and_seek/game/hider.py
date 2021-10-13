import random

# TODO: Define the Hider class here

class Hider:
    """A Code Template for the Hider 
    
    Sterotype: 
        ??
    
    Attributes: 
        location (integer): A random number from 1 to 1000
        distance  (list): A list of numbers 
    """

    def __init__(self):
        """Class Constructor. 

        Abtributes include: 
        self (Hider): An instance of Hider. 
        """
        self.location =  random.randint(1,1000)
        self.distance = [self.location]

        


    def get_hint(self): 
        if self.distance[-1] > self.distance[-2]:
            hint =  print("You are getting colder.")
        elif self.distance[-1] < self.distance[-2]:
            hint = print("Look at that. You are getting closer.")
        elif self.distance[-1] == self.distance[-2]:
            hint =  print("You didn't go anywhere.")
        elif self.distance[-1] == 0:
            hint = print("You found me!")
        return hint 

    def watch(self, location): 
        """
        The watch method keeps track of how far away the seeker is by 
        calculating the difference between their locations. 
        The distance is appended to the corresponding attribute for later use.
        """
        # self.distance.append(self.location)
        distance_away = abs(location - self.location)

        return self.distance.append(distance_away)
        


