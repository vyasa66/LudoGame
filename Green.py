from random import randint


class Green:
    """ Red class for player with red goti """

    def __init__(self):
        self.open = -1
        self.x = 0
        self.y = 0
        self.z = 0
        self.position = 0
        self.remainder = 56
        self.previous_position = 0
        self.last_postiveRemainder = 0
        self.firstmove = True
        self.xcord1 = 320
        self.ycord1 = 40
        self.xcord2 = 360
        self.ycord2 = 80

    def path(self):
        if self.position == 0:
            self.xcord1 = 320
            self.ycord1 = 40
            self.xcord2 = 360
            self.ycord2 = 80
        if self.position == 1:
            self.xcord1 = 320
            self.ycord1 = 80
            self.xcord2 = 360
            self.ycord2 = 120
        if self.position == 2:
            self.xcord1 = 320
            self.ycord1 = 120
            self.xcord2 = 360
            self.ycord2 = 160
        if self.position == 3:
            self.xcord1 = 320
            self.ycord1 = 160
            self.xcord2 = 360
            self.ycord2 = 200
        if self.position == 4:
            self.xcord1 = 320
            self.ycord1 = 200
            self.xcord2 = 360
            self.ycord2 = 240
        if self.position == 5:
            self.xcord1 = 360
            self.ycord1 = 240
            self.xcord2 = 400
            self.ycord2 = 280
        if self.position == 6:
            self.xcord1 = 400
            self.ycord1 = 240
            self.xcord2 = 440
            self.ycord2 = 280
        if self.position == 7:
            self.xcord1 = 440
            self.ycord1 = 240
            self.xcord2 = 480
            self.ycord2 = 280
        if self.position == 8:
            self.xcord1 = 480
            self.ycord1 = 240
            self.xcord2 = 520
            self.ycord2 = 280
        if self.position == 9:
            self.xcord1 = 520
            self.ycord1 = 240
            self.xcord2 = 560
            self.ycord2 = 280
        if self.position == 10:
            self.xcord1 = 560
            self.ycord1 = 240
            self.xcord2 = 600
            self.ycord2 = 280
        if self.position == 11:
            self.xcord1 = 560
            self.ycord1 = 280
            self.xcord2 = 600
            self.ycord2 = 320
        if self.position == 12:
            self.xcord1 = 560
            self.ycord1 = 320
            self.xcord2 = 600
            self.ycord2 = 360
        if self.position == 13:
            self.xcord1 = 520
            self.ycord1 = 320
            self.xcord2 = 560
            self.ycord2 = 360
        if self.position == 14:
            self.xcord1 = 480
            self.ycord1 = 320
            self.xcord2 = 520
            self.ycord2 = 360
        if self.position == 15:
            self.xcord1 = 440
            self.ycord1 = 320
            self.xcord2 = 480
            self.ycord2 = 360
        if self.position == 16:
            self.xcord1 = 400
            self.ycord1 = 320
            self.xcord2 = 440
            self.ycord2 = 360
        if self.position == 17:
            self.xcord1 = 360
            self.ycord1 = 320
            self.xcord2 = 400
            self.ycord2 = 360
        if self.position == 18:
            self.xcord1 = 320
            self.ycord1 = 360
            self.xcord2 = 360
            self.ycord2 = 400
        if self.position == 19:
            self.xcord1 = 320
            self.ycord1 = 400
            self.xcord2 = 360
            self.ycord2 = 440
        if self.position == 20:
            self.xcord1 = 320
            self.ycord1 = 440
            self.xcord2 = 360
            self.ycord2 = 480
        if self.position == 21:
            self.xcord1 = 320
            self.ycord1 = 480
            self.xcord2 = 360
            self.ycord2 = 520
        if self.position == 22:
            self.xcord1 = 320
            self.ycord1 = 520
            self.xcord2 = 360
            self.ycord2 = 560
        if self.position == 23:
            self.xcord1 = 320
            self.ycord1 = 560
            self.xcord2 = 360
            self.ycord2 = 600
        if self.position == 24:
            self.xcord1 = 280
            self.ycord1 = 560
            self.xcord2 = 320
            self.ycord2 = 600
        if self.position == 25:
            self.xcord1 = 240
            self.ycord1 = 560
            self.xcord2 = 280
            self.ycord2 = 600
        if self.position == 26:
            self.xcord1 = 240
            self.ycord1 = 520
            self.xcord2 = 280
            self.ycord2 = 560
        if self.position == 27:
            self.xcord1 = 240
            self.ycord1 = 480
            self.xcord2 = 280
            self.ycord2 = 520
        if self.position == 28:
            self.xcord1 = 240
            self.ycord1 = 440
            self.xcord2 = 280
            self.ycord2 = 480
        if self.position == 29:
            self.xcord1 = 240
            self.ycord1 = 400
            self.xcord2 = 280
            self.ycord2 = 440
        if self.position == 30:
            self.xcord1 = 240
            self.ycord1 = 360
            self.xcord2 = 280
            self.ycord2 = 400
        if self.position == 31:
            self.xcord1 = 200
            self.ycord1 = 320
            self.xcord2 = 240
            self.ycord2 = 360
        if self.position == 32:
            self.xcord1 = 160
            self.ycord1 = 320
            self.xcord2 = 200
            self.ycord2 = 360
        if self.position == 33:
            self.xcord1 = 120
            self.ycord1 = 320
            self.xcord2 = 160
            self.ycord2 = 360
        if self.position == 34:
            self.xcord1 = 80
            self.ycord1 = 320
            self.xcord2 = 120
            self.ycord2 = 360
        if self.position == 35:
            self.xcord1 = 40
            self.ycord1 = 320
            self.xcord2 = 80
            self.ycord2 = 360
        if self.position == 36:
            self.xcord1 = 0
            self.ycord1 = 320
            self.xcord2 = 40
            self.ycord2 = 360
        if self.position == 37:
            self.xcord1 = 0
            self.ycord1 = 280
            self.xcord2 = 40
            self.ycord2 = 320

        if self.position == 38:
            self.xcord1 = 0
            self.ycord1 = 240
            self.xcord2 = 40
            self.ycord2 = 280
        if self.position == 39:
            self.xcord1 = 40
            self.ycord1 = 240
            self.xcord2 = 80
            self.ycord2 = 280

        if self.position == 40:
            self.xcord1 = 80
            self.ycord1 = 240
            self.xcord2 = 120
            self.ycord2 = 280
        if self.position == 41:
            self.xcord1 = 120
            self.ycord1 = 240
            self.xcord2 = 160
            self.ycord2 = 280
        if self.position == 42:
            self.xcord1 = 160
            self.ycord1 = 240
            self.xcord2 = 200
            self.ycord2 = 280
        if self.position == 43:
            self.xcord1 = 200
            self.ycord1 = 240
            self.xcord2 = 240
            self.ycord2 = 280
        if self.position == 44:
            self.xcord1 = 240
            self.ycord1 = 200
            self.xcord2 = 280
            self.ycord2 = 240
        if self.position == 45:
            self.xcord1 = 240
            self.ycord1 = 160
            self.xcord2 = 280
            self.ycord2 = 200
        if self.position == 46:
            self.xcord1 = 240
            self.ycord1 = 120
            self.xcord2 = 280
            self.ycord2 = 160
        if self.position == 47:
            self.xcord1 = 240
            self.ycord1 = 80
            self.xcord2 = 280
            self.ycord2 = 120
        if self.position == 48:
            self.xcord1 = 240
            self.ycord1 = 40
            self.xcord2 = 280
            self.ycord2 = 80
        if self.position == 49:
            self.xcord1 = 240
            self.ycord1 = 0
            self.xcord2 = 280
            self.ycord2 = 40
        if self.position == 50:
            self.xcord1 = 280
            self.ycord1 = 0
            self.xcord2 = 320
            self.ycord2 = 40

        if self.position == 51:
            self.xcord1 = 280
            self.ycord1 = 40
            self.xcord2 = 320
            self.ycord2 = 80
        if self.position == 52:
            self.xcord1 = 280
            self.ycord1 = 80
            self.xcord2 = 320
            self.ycord2 = 120
        if self.position == 53:
            self.xcord1 = 280
            self.ycord1 = 120
            self.xcord2 = 320
            self.ycord2 = 160
        if self.position == 54:
            self.xcord1 = 280
            self.ycord1 = 160
            self.xcord2 = 320
            self.ycord2 = 200
        if self.position == 55:
            self.xcord1 = 280
            self.ycord1 = 200
            self.xcord2 = 320
            self.ycord2 = 240
        if self.position == 56:
            self.xcord1 = 280
            self.ycord1 = 240
            self.xcord2 = 320
            self.ycord2 = 280

        return self.xcord1, self.ycord1, self.xcord2, self.ycord2

    def roll(self, minimum=1, maximum=6):
        """ Rolling of Dice"""
        self.x = self.y = self.z = 0
        self.x = randint(minimum, maximum)
        if self.x == 6:
            self.y = randint(minimum, maximum)
            if self.y == 6:
                self.z = randint(minimum, maximum - 1)
        # print( self.x, self.y, self.z)

    def roll_cancel(self, minimum=1, maximum=6):
        """ Rolling of Dice"""
        self.x = self.y = self.z = 0
        return self.x, self.y, self.z

    def move(self):
        """Move of the Goti"""
        self.position += self.x
        self.position += self.y
        self.position += self.z
        return self.position

    def opening(self):
        """Open the goti from start with 6 """
        self.open = 0
        self.position = self.y + self.z
        return self.open

    def button_click():
        current = self.roll()
        # e.insert(0,str(current) + str(number))
        print(current)
