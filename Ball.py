
class Pos:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    def __add__(self, another_pos):
        return Pos(self.x + another_pos.x, self.y + another_pos.y)
    
    def __sub__(self, another_pos):
        return Pos(self.x - another_pos.x, self.y - another_pos.y)

    def __str__(self):
        return "({}, {})".format(self.x, self.y)
    
def dot(pos1, pos2):
    return pos1.x * pos2.x + pos1.y * pos2.y
    
class Ball:
    def __init__(self, mass = 1, ):
        self.mass = mass


if __name__ == "__main__":
    # Should use python test framework
    p1 = Pos(1, 2)
    p2 = Pos(1, 2)
    p3 = p1 + p2
    p4 = p1 - p2
    print(p3, p4)
    print(dot(p1, p2))
