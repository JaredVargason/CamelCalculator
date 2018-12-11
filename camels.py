from enum import Enum
NUM_CAMELS = 5
DICE_MAX = 3

counts = [0] * NUM_CAMELS

class DICE_COLORS(Enum):
    WHITE = 0
    YELLOW = 1
    ORANGE = 2
    GREEN = 3
    BLUE = 4

class Track:
    GRID_LENGTH = 17

    def __init__(self):
        self.grid = [None] * Track.GRID_LENGTH
        self.available_dice = [i for i in DICE_COLORS]

    def __str__(self): 
        lines = []
        line[0] = ['_' for i in range(Track.GRID_LENGTH)]
        

#an input of camelstacks is a list of lists. the position of the camel stack is the index
#camels at the back of the list are considered on top.
exampleStacks = [[DICE_COLORS.WHITE,DICE_COLORS.YELLOW,DICE_COLORS.ORANGE],[DICE_COLORS.GREEN,DICE_COLORS.BLUE]]


def simulate(track):
    for dice_color in available_dice:    
        for dice_result in DICE_MAX:
            simulate()
            

if __name__ == "__main__":
    #simulate(exampleStack)
    track = Track()
    print(track)