class Point(object):
    def __init__(self, x=0, y=0):           # using init makes it easier to instantiate objects
        self.x = x
        self.y = y

    def __str__(self):
        return '(%d, %d)' % (self.x, self.y)    # returns string representation of object
        # use %d because we just want numbers written like 0 not 00.


point = Point(7,9)      # Just going to use the same numbers as before for consistency
print point

point = Point(16)
print point

point = Point(32, 45)
print point