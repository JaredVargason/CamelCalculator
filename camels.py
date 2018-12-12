from enum import IntEnum

NUM_CAMELS = 5
DICE_VALS = [1,2,3]

class COLORS(IntEnum):
    WHITE = 0
    YELLOW = 1
    ORANGE = 2
    GREEN = 3
    BLUE = 4

    def __str__(self):
        return str(self.name)[0]

class Tile(IntEnum):
    FORWARD = 1 
    BACKWARD = -1 

    def __str(self):
        if self == self.FORWARD:
            return '+'
        else:
            return '-'

#exampleStacks = [[COLORS.WHITE,COLORS.YELLOW,COLORS.ORANGE],[COLORS.GREEN,COLORS.BLUE]]
class Track:
    GRID_LENGTH = 17

    def __init__(self):
        self.grid = [None] * Track.GRID_LENGTH
        self.grid[0] = [dc for dc in COLORS]
        self.available_dice = [i for i in COLORS]

    def __str__(self): 
        lines = []
        labels = [str(i + 1).zfill(2) for i in range(Track.GRID_LENGTH)]
        lines.append([i[1] for i in labels])
        lines.append([i[0] for i in labels])
        lines.append(['_' for i in range(Track.GRID_LENGTH)])

        for i, line in enumerate(lines):
            lines[i] = ''.join(line)

        for i in range(0, 5): 
            line = []
            for j in range(Track.GRID_LENGTH):
                space = self.grid[j]
                if space and type(space) == list and len(space) > i:
                    line.append(space[i].__str__())
                else:
                    line.append(' ')
            
            lines.append(''.join(line))

        return '\n'.join([line for line in lines[::-1]])
    
    def apply_die_roll(self, color, result):
        if color not in self.available_dice:
            return

        self.available_dice.remove(color)
        #get the stack corresponding to the color
        stackIndex = -1 
        camelStack = None
        for i, space in enumerate(self.grid): 
            if type(space) == list: 
                for j, camel in enumerate(space):
                    if color == camel:
                        stackIndex = i
                        camelStack = space[j:len(space)]
                        self.grid[i] = space[0:j]

        newIndex = (stackIndex + result) % self.GRID_LENGTH
        self.grid[newIndex] = self.grid[newIndex] + camelStack if self.grid[newIndex] else camelStack
        print(self.grid, stackIndex, camelStack, newIndex)
    
    def undo_die_roll(self, color, result):
        if color in self.available_dice:
            return
        
        self.available_dice.append(color)

        stackIndex = -1
        camelStack = None
        for i, space in enumerate(self.grid):
            if type(space) == list:
                for j, camel in enumerate(space):
                    if color == camel:
                        stackIndex = i
                        camelStack = space[j:len(space)]
                        self.grid[i] = space[0:j]
        
        newIndex = (stackIndex - result) % self.GRID_LENGTH
        self.grid[newIndex] = self.grid[newIndex] + camelStack if self.grid[newIndex] else camelStack
        print(self.grid, stackIndex, camelStack, newIndex)

    def first_place(self):
        for i in range(Track.GRID_LENGTH-1, -1, -1):
            space = self.grid[i] 
            if space and type(space) == list:
                    return space[len(space) - 1]

counts = [0] * NUM_CAMELS
def simulate(track):
    if len(track.available_dice) == 0:
        lead = track.first_place()
        global counts
        counts[lead] += 1
        
    for die in track.available_dice:    
        for dice_result in DICE_VALS:
            track.apply_die_roll(die, dice_result)
            simulate(track)
            track.undo_die_roll(die, dice_result)

            


if __name__ == "__main__":
    track = Track()
    #track.apply_die_roll(COLORS.BLUE, 1)
    #track.apply_die_roll(COLORS.WHITE, 1)
    #print(track)
    #print(track.first_place())
    simulate(track)
    print(counts) 