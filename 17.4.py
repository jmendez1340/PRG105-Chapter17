class Point(object):
    def __init__(self, x=0, y=0):           # using init makes it easier to instantiate objects
        self.x = x
        self.y = y

    def __str__(self):
        return '(%d, %d)' % (self.x, self.y)    # returns string representation of object
        # use %d because we just want numbers written like 0 not 00.

    def __add__(self, other):
        x = self.x + other.x        # will combine two different x points by using 'other.x'
        y = self.y + other.y        # will combine two different y points by using 'other.y'
        return x,y

Firstpoint = Point(7, 2)
Secondpoint = Point(9, 6)

print Firstpoint + Secondpoint