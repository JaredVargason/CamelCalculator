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

class Track:
    GRID_LENGTH = 10#default 19
    FINISH_SQUARE = GRID_LENGTH - 3 

    def __init__(self):
        self.grid = [[]] * Track.GRID_LENGTH
        #self.grid[0] = [dc for dc in COLORS]
        self.grid[0] = [COLORS.YELLOW, COLORS.WHITE]
        self.grid[1] = [COLORS.BLUE]
        self.grid[2] = [COLORS.ORANGE, COLORS.GREEN]
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
                if len(space) > i:
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
        camelStack = [] 
        for i, space in enumerate(self.grid): 
                for j, camel in enumerate(space):
                    if color == camel:
                        stackIndex = i
                        camelStack = space[j:len(space)]
                        self.grid[i] = space[0:j]

        newIndex = (stackIndex + result) % self.GRID_LENGTH
        self.grid[newIndex] = self.grid[newIndex] + camelStack
    
    def undo_die_roll(self, color, result):
        if color in self.available_dice:
            return
        
        self.available_dice.append(color)

        stackIndex = -1
        camelStack = [] 
        for i, space in enumerate(self.grid):
            if type(space) == list:
                for j, camel in enumerate(space):
                    if color == camel:
                        stackIndex = i
                        camelStack = space[j:len(space)]
                        self.grid[i] = space[0:j]
        
        newIndex = (stackIndex - result) % self.GRID_LENGTH
        self.grid[newIndex] = self.grid[newIndex] + camelStack

    def refill_dice(self):
        self.available_dice = [dc for dc in COLORS]

    def first_place(self):
        #for i in range(Track.GRID_LENGTH-1, -1, -1):
        for space in self.grid[::-1]:
            if space:
                return space[-1]
        return None    

    def last_place(self):
        for space in self.grid:
            if space:
                return space[0]
        return None

    def won_game(self):
        for space in self.grid[self.FINISH_SQUARE::-1]:
            if space:
                return space[-1]
        return None


counts = [0] * NUM_CAMELS
def simulateLeg(track):
    if len(track.available_dice) == 0:
        lead = track.first_place()
        global counts
        counts[lead] += 1
        
    for die in track.available_dice:    
        for dice_result in DICE_VALS:
            track.apply_die_roll(die, dice_result)
            simulateLeg(track)
            track.undo_die_roll(die, dice_result)

'''def simulateGame(track):
    if len(track.available_dice) == 0:
        track.refill_dice()
        
    for die in track.available_dice:
        for dice_result in DICE_VALS:
            track.apply_die_roll(die, dice_result)
            camel = track.won_game()
            if camel:
                counts[camel] += 1
            else:
                simulateGame(track)
            track.undo_die_roll(die, dice_result)
'''

if __name__ == "__main__":
    track = Track()
    #track.apply_die_roll(COLORS.BLUE, 1)
    #track.apply_die_roll(COLORS.WHITE, 1)
    #print(track)
    #print(track.first_place())
    simulateLeg(track)
    print(track)
    print ([str(dc) for dc in COLORS])
    print(counts) 
    probabilities = [item / sum(counts) for item in counts]
    print(probabilities)

