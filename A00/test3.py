import Rhino.Geometry as rg
import ghpythonlib.treehelpers as th
import math
import ghpythonlib.components as ghc

#creating a mesh
mes= rg.Mesh()
#print (mes.Vertices)

#A mesh has vertices and faces
# You add the points as vertices through a for loop
for i in x:
    mes.Vertices.Add(i)

b= mes.Vertices
print len(mes.Vertices)

#then you add the faces through AddFace
#https://developer.rhino3d.com/api/RhinoCommon/html/T_Rhino_Geometry_Collections_MeshFaceList.htm
mes.Faces.AddFace(0,1,2,3)

a= mes