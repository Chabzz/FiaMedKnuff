#Här definierar jag vilka färger och storlekar som ska användas
class Color:

    GRÖN = '#00d464'
    GUL = '#f0ff00'
    RÖD = '#ff0000'
    BLÅ = '#2c84ff'
    DEFAULT = '#fff'
    CYAN = '#43BFDD'
    GRÅ = '#fff'


class Board:

    SQUARE_SIZE = 40
    PANEL_WIDTH = 600
    PANEL_HEIGHT = 640
    BOARD_WIDTH = 640
    BOARD_HEIGHT = 640
    POINTS = [(0, 0), (0, 1), (1, 0), (1, 1)]
    POSITIVE_V = [(6, 2), (8, 1), (6, 13), (8, 12)]
    POSITIVE_H = [(1, 6), (2, 8), (13, 8), (12, 6)]

#Texten längst nere och längst uppe
class Text:

    MADE_BY = 'Made By: Axel Renmark'
    HEADER =  'Fia med knuff'

#Class för att bestämma hur pjäserna ska röra på sig
class Path:

    def __init__(self):
        self.blue_path = []
        self.yellow_path = []
        self.green_path = []
        self.red_path = []

        self.ry = None
        self.by = None 
        self.gx = None
        self.ry = None
        self.count = None

    def update_coordinates(self, ry, by, gx, gy, count):
        self.ry = ry
        self.by = by
        self.gx = gx
        self.gy = gy
        self.count = count

    def start_populating(self):

        #1
        self.update_coordinates(60, 260, 540, 340, 5)
        self.direct(pow_index=0, direction='right')
        #2
        self.update_coordinates(260, 220, 340, 380, 5)
        self.direct(pow_index=3, direction='up')
        #3
        self.update_coordinates(260, 20, 340, 580, 3)
        self.direct(direction='right') 
        #4
        self.update_coordinates(340, 60, 260, 540, 5)
        self.direct(pow_index=0, direction='down')
        #5
        self.update_coordinates(380, 260, 220, 340, 5)
        self.direct(pow_index=3, direction='right')
        #6
        self.update_coordinates(580, 260, 20, 340, 3)
        self.direct(direction='down')
        #7
        self.update_coordinates(540, 340, 60, 260, 5)
        self.direct(pow_index=0, direction='left')
        #8
        self.update_coordinates(340, 380, 260, 220, 5)
        self.direct(pow_index=3, direction='down')
        #9
        self.update_coordinates(340, 580, 260, 20, 3)
        self.direct(direction='left')
        #10
        self.update_coordinates(260, 540, 340, 60, 5)
        self.direct(pow_index=0, direction='up')
        #11
        self.update_coordinates(220, 340, 380, 260, 6)
        self.direct(pow_index=3, direction='left')
        #12
        self.update_coordinates(20, 300, 580, 300, 7)
        self.direct(direction='right')

    def direct_horizontal(self, k, pow_index = -1):

        for i in range(self.count):
            if i == pow_index:
                p = 1
            else:
                p = 0
            self.blue_path.append((self.ry  +  k*i*Board.SQUARE_SIZE, self.by, p))
            self.yellow_path.append((self.by, self.gx  -  k*i*Board.SQUARE_SIZE, p))
            self.green_path.append((self.gx - k*i*Board.SQUARE_SIZE, self.gy, p))
            self.red_path.append((self.gy, self.ry + k*i*Board.SQUARE_SIZE, p))

    def direct_vertical(self, k, pow_index = -1):

        for i in range(self.count):
            if i == pow_index:
                p = 1
            else:
                p = 0
            self.blue_path.append((self.ry, self.by - k*i*Board.SQUARE_SIZE, p))
            self.yellow_path.append((self.by - k*i*Board.SQUARE_SIZE,self.gx, p))
            self.green_path.append((self.gx, self.gy + k*i*Board.SQUARE_SIZE, p))
            self.red_path.append((self.gy + k*i*Board.SQUARE_SIZE, self.ry, p))


    def direct(self, direction, pow_index = -1):
        if direction=='right':
            self.direct_horizontal(1, pow_index=pow_index)
        elif direction=='left':
            self.direct_horizontal(-1, pow_index=pow_index)
        elif direction=='down':
            self.direct_vertical(-1, pow_index=pow_index)
        else:
            self.direct_vertical(1, pow_index=pow_index)

path = Path()
path.start_populating()
