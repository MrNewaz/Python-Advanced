class Point:
    default_color = 'Red'

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def zero(cls):
        cls(0, 0)

    def draw(self):
        print(f'points ({self.x}):({self.y})')


point = Point.zero()
