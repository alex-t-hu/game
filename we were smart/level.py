from enum import Enum
class Block(Enum):
    START = 1
    END = 2
    WALL = 3
    EMPTY = 4

class Level:
    def __init__(self):
        self.dimension = 3
        self.grid = [
            [
                Block.START, Block.WALL, Block.EMPTY
            ],
            [
                Block.EMPTY, Block.EMPTY, Block.EMPTY
            ],
            [
                Block.EMPTY, Block.EMPTY, Block.END
            ]
        ]