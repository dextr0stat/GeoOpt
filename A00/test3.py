import Rhino.Geometry as rg
import ghpythonlib.treehelpers as th
import math
import ghpythonlib.components as ghc

#creating a mesh
mes= rg.Mesh()
#print (mes.Vertices)

for i in x:
    mes.Vertices.Add(i)

print len(mes.Vertices)

mes.Faces.AddFace(0,1,2,3)

a= mes