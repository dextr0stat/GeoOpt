import Rhino.Geometry as rg

grid= []
for i in range (int(x)):
    for j in range (int(y)):
        grid.append (rg.Point3d(i,j,0))

a= grid

b= rg.Line(grid[1],grid[27])

c= b.BoundingBox

#b= line.BoundingBox