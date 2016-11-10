class Kangaroo(object):

    def __init__ ( self ):
        self.pouch_contents = [] # [] is an empty list

    def put_in_pouch(self, other ):
        self.pouch_contents.append(other)       # Appending adds contents to the pouch

    def __str__ ( self ):
        return "Kangaroo object" + str(self.pouch_contents)

# Variables kanga and roo
kanga = Kangaroo()
roo = Kangaroo()

roo.put_in_pouch(raw_input('Enter something: '))
# Not sure if you wanted it to be blank so I made it a raw input
print "kanga =",kanga
print "roo =",roo