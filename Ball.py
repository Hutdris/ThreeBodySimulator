import numpy as np

class Pos:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    def __add__(self, another_pos):
        return Pos(self.x + another_pos.x, self.y + another_pos.y)
    
    def __sub__(self, another_pos):
        return Pos(self.x - another_pos.x, self.y - another_pos.y)
    
    def __mul__(self, scale):
        return Pos(self.x * scale, self.y * scale)

    def __rmul__(self, scale):
        return self * scale
    def __neg__(self):
        return -1 * self
    def __eq__(self, another_pos):
        return self.x == another_pos.x and self.y == another_pos.y
    def __str__(self):
        return "({}, {})".format(self.x, self.y)
    

def dot(pos1, pos2):
    return pos1.x * pos2.x + pos1.y * pos2.y

def distance(pos1, pos2):
    temp_pos = pos1 - pos2
    return dot(temp_pos, temp_pos)

def distance(ball1, ball2):
    return np.linalg.norm(ball1.pos - ball2.pos)

def gravatiy_force(ball1, ball2):
    """
    F = Gm1*m2/r**2
    G: 6.67430*1e-11 m**3/(kg * sec**2)
    https://en.wikipedia.org/wiki/Gravity
    """
    return np.float32(6.67430e-11) * ball1.mass * ball2.mass / np.power(distance(ball1, ball2), 2)

    
class Ball:
    def __init__(self,
                 mass = 1e9,  #kg
                 radius = 1e6,  #meter
                 pos = (0, 0),
                 vec = (0, 0)
                 ):
        self.mass = mass
        self.radius = radius
        self.pos = np.array(list(pos)).reshape(2, 1)
        self.vec = np.array(list(vec)).reshape(2, 1)

if __name__ == "__main__":
    # Should use python test framework
    earth = Ball(5.972E24)
    unit_ball = Ball(1, 1, (6371e3, 0))
    print(gravatiy_force(earth, unit_ball)) # should be 9.81997342852499...