# Go playing program

def flatten(list_of_lists):
    flattenlist = [y for x in list_of_lists for y in x]
    return flattenlist


# def liberties(coordinates, color, movelist, libertylist):
#    previous_moves = movelist
#    xcoordinate = coordinates[0] - 1  # Subtract 1 since Python starts at zero
#    ycoordinate = coordinates[1] - 1
#    color = color


# Create go board Class
# Have move function which checks whether move has been previously played and create a new object "group"
class Goban:
    def __init__(self, size):
        self.movelist = []
        self.xsize = size
        self.ysize = size
        self.board = [["0"] * self.ysize for i in range(self.xsize)]  # Creates go board
        self.libs = []
        self.groups = []

    # Define function move
    def move(self, coordinates, color):
        xcoordinate = coordinates[0] - 1  # Subtract 1 since Python starts at zero
        ycoordinate = coordinates[1] - 1
        xycoordinates = (xcoordinate, ycoordinate)

        # Check for liberties
        previous_moves = self.movelist  # flatten(self.movelist)<-apparently no need

        if xycoordinates not in previous_moves and 0 <= xcoordinate < 19 and 0 <= ycoordinate < 19:
            # TODO: check for legality
            self.movelist.append((xcoordinate, ycoordinate))

            liberties = []

            adjacents = []
            for i in (-1, 1):
                adjacents.append((xcoordinate + i, ycoordinate))
                adjacents.append((xcoordinate, ycoordinate + i))

            for adj in adjacents:
                if adj not in previous_moves:
                    liberties.append(adj)

            # check that its a legal move

            self.libs.append(liberties)
            g = Group(xycoordinates, color, liberties)
            self.groups.append(g)  # Lists can contain objects

            # TODO: this is where we check to add to a group or form a new group

            # if I play a stone, I need to remove the liberties of all adjacent groups
            for g in self.groups:
                if xycoordinates in g.liberties:
                    g.liberties.remove(xycoordinates)

            self.board[xcoordinate][ycoordinate] = color  # change board to reflect new stone
        else:
            print("This move is not legal.")
        self.print_me()

    def print_me(self):
        for i in self.board:
            print(i)
        print("\n")


# Create Group class that takes x-y position and color and determines free liberties
class Group:
    def __init__(self, coordinates, color, liberties):
        self.coords = [coordinates]
        self.color = color
        self.liberties = liberties


myboard = Goban(19)
for i in myboard.board:
    print(i)
print("\n")
myboard.move((4, 4), "b")
myboard.move((4, 3), "w")
myboard.move((5, 4), "b")
myboard.move((5, 3), "w")
myboard.move((20, 2), "b")
myboard.move((2, 20), "w")
# print(myboard.board)
# print(myboard.movelist)
print(len(myboard.libs))
# print(myboard.movelist[0])
# print(myboard.libs)
print(myboard.groups[0].liberties)
print(myboard.groups[1].liberties)
print(myboard.groups[2].liberties)
print(myboard.groups[3].liberties)
