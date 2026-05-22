# Globals for the directions
EAST = "east"
NORTH = "north"
WEST = "west"
SOUTH = "south"


class Robot:
    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):
        self.direction = direction
        self.coordinates = (x_pos, y_pos)

    def turn_right(self):
        directions = [NORTH, EAST, SOUTH, WEST]
        idx = directions.index(self.direction)
        self.direction = directions[(idx + 1) % 4]

    def turn_left(self):
        directions = [NORTH, WEST, SOUTH, EAST]
        idx = directions.index(self.direction)
        self.direction = directions[(idx + 1) % 4]

    def advance(self):
        x, y = self.coordinates

        if self.direction == NORTH:
            y += 1
        elif self.direction == EAST:
            x += 1
        elif self.direction == SOUTH:
            y -= 1
        elif self.direction == WEST:
            x -= 1

        self.coordinates = (x, y)

    def move(self, instructions):
        for command in instructions:
            if command == 'R':
                self.turn_right()
            elif command == 'L':
                self.turn_left()
            elif command == 'A':
                self.advance()
