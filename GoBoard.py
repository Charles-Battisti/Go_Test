# Go playing program

def flatten(list_of_lists):
    flattenlist = [y for x in list_of_lists for y in x]
    return flattenlist

#def liberties(coordinates, color, movelist, libertylist):
#    previousmoves = movelist
#    xcoordinate = coordinates[0] - 1  # Subtract 1 since Python starts at zero
#    ycoordinate = coordinates[1] - 1
#    color = color


# Create go board Class
# Have move function which checks whether move has been previously played and create a new object "group"
class Goban:
    def __init__(self, size):
        self.movelist=[]
        self.xsize = size
        self.ysize = size
        self.g = [["0"]*self.ysize for i in range(self.xsize)] #Creates go board
        self.numlibs = []
        self.groups = []

    #Define function move
    def move(self, coordinates, color):
        xycoordinates = coordinates
        xcoordinate = coordinates[0] - 1 #Subtract 1 since Python starts at zero
        ycoordinate = coordinates[1] - 1
        color = color

        #Check for liberties
        previousmoves = self.movelist #flatten(self.movelist)<-apparently no need
        if xycoordinates not in previousmoves and xcoordinate < 19 and ycoordinate < 19:
            self.movelist.append((xcoordinate, ycoordinate))
            numofliberties = []
            plusxmove = (xcoordinate + 1, ycoordinate)
            minusxmove = (xcoordinate - 1, ycoordinate)
            plusymove = (xcoordinate, ycoordinate + 1)
            minusymove = (xcoordinate, ycoordinate - 1)
            if plusxmove not in previousmoves:
                numofliberties.append(plusxmove)
            if minusxmove not in previousmoves:
                numofliberties.append(minusxmove)
            if plusymove not in previousmoves:
                numofliberties.append(plusymove)
            if minusymove not in previousmoves:
                numofliberties.append(minusymove)
            self.numlibs.append(numofliberties.copy())
            self.groups.append(Group(coordinates, color, numofliberties.copy()))  # Lists can contain objects
            count = 0 #use count/count2 to select the correct liberties to remove from numlibs list
            for i in range(len(self.groups)): #self.numlibs: #i returns all items in row (set), not each item in all of numlibs
                count2 = 0
                index = self.groups[i].liberties
                for j in range(len(index)):
                    if (xcoordinate, ycoordinate) == index[count2]:
                        print(self.groups[i].liberties[count2])
                        #del self.numlibs[i][j] #Since item deleted in numlibs, do not add 1 to count2
                        del self.groups[i].liberties[count2]
                    else:
                        count2 += 1
                count += 1
            self.g[xcoordinate][ycoordinate] = color #change board to reflect new stone
        else:
            print("This move has already been played!!")

        for i in self.g:
            print(i)
        print("\n")



#Create Group class that takes x-y position and color and determines free liberties
class Group:
    def __init__(self, coordinates, color, liberties):
        self.xcoordinate = coordinates[0] - 1
        self.ycoordinate = coordinates[1] - 1
        self.color = color
        self.liberties = liberties

myboard = Goban(19)
for i in myboard.g:
    print(i)
print("\n")
myboard.move((4,4),"b")
myboard.move((4,3),"w")
myboard.move((5,4),"b")
myboard.move((5,3),"w")
myboard.move((20,2),"b")
myboard.move((2,20),"w")
#print(myboard.g)
#print(myboard.movelist)
print(len(myboard.numlibs))
#print(myboard.movelist[0])
#print(myboard.numlibs)
print(myboard.groups[0].liberties)
print(myboard.groups[1].liberties)
print(myboard.groups[2].liberties)
print(myboard.groups[3].liberties)
