import random
from game.move import Move

# TODO: Define the Board class here

#to_string() - give a string representation 
#apply(move) - apply the move
#is_empty() - evaluate 

# what is the purpose of the board class 
# what is it's sterotype

class Board:
    """
    Purpose of the Board is to keep track of the pieces at play. 

    Sterotype: information holder, coordinator

    Attributes:

    """

    def __init__(self):
        """
        The class constructor 
        """
        self.decision = Move()
        # self._prepare

    def prepare():
        """
        sets up the board with a random number of piles (2 - 5) 
        containing a random number of stones (1 - 9).
        """

        num_pile = random.randint(2, 5)

        pile_number = []
        for i in range(num_pile):
            i += 1
            pile_number.append(i)

        for i in range(1):
            print("-" * 20)
            for s in range(num_pile):
                stones = random.randint(1, 9)
                num_stones = "O" * stones
                print(f"{pile_number[s]}: {num_stones}")
            print("-" * 20)
        pass 

    
    def to_string(self):
        """
        Converts the board data to its string representation and returns it to the caller.

        Needs to return a string
        """
        pass 


    def apply(self, decision):
        """
        Applies a move to the playing surface.
        """
        pass


    def is_empty(self):
        """
        Determines if all the stones have been removed from the board. 
        It returns True if the board has no stones on it; false if otherwise.

        # Thinking it will need to loop through the number of piles and get count
        if count == 0:
            return empty
        else:
            keep playing 
        
        """
        pass



