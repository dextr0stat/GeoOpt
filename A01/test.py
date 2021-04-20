import Rhino.Geometry as rg
a= gridbox= []

for i in range(10):
    for j in range(10):
        for k in range (10):
            pt= rg.Point3d(i,j,k)
            gridbox.append(pt)
