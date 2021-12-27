
GRID_SIZE = 10

class Octogrid:

    def __init__(self, darr):
        self.grid = darr
        self.flashes = 0
        self.flashLocations = []

    def cleanup(self):
        for x, y in self.flashLocations:
            self.grid[x][y] = 0
        self.flashLocations = []
        # print('FLASH LOCATIONS RESET TO 0')

    def energize(self, x, y):
        self.grid[x][y] += 1
        # print(self.grid)
        if self.willFlashAt(x, y):
            self.flash(x, y)

    def willFlashAt(self, x, y) -> bool:
        return (self.grid[x][y] > 9) and ((x, y) not in self.flashLocations)
        
    def flash(self, x, y):
        # print("flashed at", x, ",", y)
        self.flashes += 1
        
        self.flashLocations.append((x, y))

        for xDiff in [-1, 0, 1]:
            for yDiff in [-1, 0, 1]:
                if (xDiff == 0 and yDiff == 0) or (x + xDiff < 0) or (y + yDiff < 0) or (x + xDiff >= GRID_SIZE) or (y + yDiff >= GRID_SIZE): 
                    continue
                else:
                    self.energize(x + xDiff, y + yDiff)
               
    def step(self):
        for x in range(GRID_SIZE):
            for y in range(GRID_SIZE):
                self.energize(x, y)
        self.cleanup()

with open("11.txt", "r") as f:

    content = f.read()
    grid = [[int(y) for y in x] for x in content.split("\n")]
    
    stepCount = 3
    octogrid = Octogrid(grid)

    for i in range(stepCount):
        octogrid.step()


    print(octogrid.grid)
    print(octogrid.flashes)

    
