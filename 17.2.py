class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def print_point(self):
        print "x =", self.x, ",",
        print "y =", self.y

point = Point(7,9)         # By not assigning anything for x or y they are assumed to be 0
point.print_point()

point = Point(16)       # If you just want an x just write a value
                        # for a Y you need to write (0,"number you want")
point.print_point()

point = Point(32, 45)
point.print_point()