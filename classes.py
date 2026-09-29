from microbit import Image


class IconNames:
    def __init__(self, microbit_image):
        self.inner_image = microbit_image
    HEART = Image.HEART
    SMALL_HEART = Image.HEART_SMALL
    YES = Image.YES
    NO = Image.NO
    HAPPY = Image.HAPPY
    SAD = Image.SAD
    CONFUSED = Image.CONFUSED
    ANGRY = Image.ANGRY
    ASLEEP = Image.ASLEEP
    SURPRISED = Image.SURPRISED
    SILLY = Image.SILLY
    FABULOUS = Image.FABULOUS
    MEH = Image.MEH
    TSHIRT = Image.TSHIRT
    ROLLERSKATE = Image.ROLLERSKATE
    DUCK = Image.DUCK
    HOUSE = Image.HOUSE
    BUTTERFLY = Image.BUTTERFLY
    STICKFIGURE = Image.STICKFIGURE
    GHOST = Image.GHOST
    SWORD = Image.SWORD
    GIRAFFE = Image.GIRAFFE
    SKULL = Image.SKULL
    UMBRELLA = Image.UMBRELLA
    SNAKE = Image.SNAKE
    RABBIT = Image.RABBIT
    COW = Image.COW
    QUARTER_NOTE = Image.MUSIC_CROTCHET
    EIGHT_NOTE = Image.MUSIC_QUAVER
    PITCHFORK = Image.PITCHFORK
    TARGET = Image.TARGET
    TRIANGLE = Image.TRIANGLE
    LEFT_TRIANGLE = Image.TRIANGLE_LEFT
    CHESSBOARD = Image.CHESSBOARD
    DIAMOND = Image.DIAMOND
    SMALL_DIAMOND = Image.DIAMOND_SMALL
    SQUARE = Image.SQUARE
    SMALL_SQUARE = Image.SQUARE_SMALL
    SCISSORS = Image.SCISSORS

class ArrowNames:
    def __init__(self, microbit_image):
        self.inner_image = microbit_image
    NORTH = Image.ARROW_N
    NORTH_EAST = Image.ARROW_NE
    EAST = Image.ARROW_E
    SOUTH_EAST = Image.ARROW_SE
    SOUTH = Image.ARROW_S
    SOUTH_WEST = Image.ARROW_SW
    WEST = Image.ARROW_W
    NORTH_WESt = Image.ARROW_NW
