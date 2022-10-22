from enum import Enum
class Block(Enum):
    START = 1
    END = 2
    WALL = 3
    EMPTY = 4

WIDTH = 500
HEIGHT = 500
levels = [
    [
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
]