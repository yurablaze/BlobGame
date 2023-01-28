import random

WIDTH = 800
HEIGHT = 600
WHITE = (255, 255, 255) # (RED, GREEN, BLUE)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

class Blob():
    def __init__(self, color):
        self.size = random.randint(4, 8)
        self.color = color
        self.x, self.y = random.randint(10, WIDTH-10), random.randint(10, HEIGHT-10)
    def move(self):
        self.x += random.randrange(-1, 2)
        self.y += random.randrange(-1, 2)
        if self.x<10:
            self.x = 10
        elif self.x>WIDTH-10:
            self.x=WIDTH-10
        if self.y<10:
            self.y = 10
        elif self.y>HEIGHT-10:
            self.y=HEIGHT-10
    def isReal(self):
        if self.size<=0:
            del self
    def is_touching(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        dd = pow( pow(dx, 2) + pow(dy, 2) , 0.5)
        if self.size+other.size >= dd:
            return True
        else:
            return False

class RedBlob(Blob):
    def __init__(self):
        super().__init__(RED)
    def __add__(self, other_blob):
        if isinstance(other_blob, RedBlob):
            self.size += other_blob.size
            other_blob.size = 0

class BlueBlob(Blob):
    def __init__(self):
        super().__init__(BLUE)
    def __add__(self, other_blob):
        """
            blue+red --> minus size
            blue+blue --> plus size
        """
        if isinstance(other_blob, RedBlob):
            new_blue_size = self.size - other_blob.size
            if new_blue_size<=0:
                #print("Red with Blue colision +=SIZE")
                other_blob.size -= self.size
                self.size=0
            else:
                self.size -= other_blob.size
                other_blob.size=0
            #print("Red with Blue colision")
            #self.isReal()
            #other_blob.isReal()
        else:
            #print("Blue with Blue colision")
            self.size += other_blob.size
            other_blob.size = 0
            #del other_blob
"""
obj1 = RedBlob()
obj2 = BlueBlob()

obj1 + obj2
"""