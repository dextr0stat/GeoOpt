"""
***MESH TRANSFORM***
GeoOpt-02-Varun-Mehta
-----------------------------------
Provides a Scripting Component
Provides a scripting component.
    Inputs:
        m: a mesh
        s: sun vector
    Output:
        a: List of Vectors
        b: List of Points
        c: list of angles
        d: exploded mesh
"""

import Rhino.Geometry as rg
import ghpythonlib.treehelpers as th
import math
import ghpythonlib.components as ghc

#[1]
m.FaceNormals.ComputeFaceNormals()
a = m.FaceNormals

#[2]
centres=[]

for i in range (m.Faces.Count): #can this be done in range (len(m.Faces))? GH crashed
    face_centre= m.Faces.GetFaceCenter(i)
    #print face_centre
    centres.append(face_centre)
#print (centres) everytime I tried printed, Rhino Crashes
b= centres

#[3]
#s is the sun vector
angleList=[]

for i in b:
    angle= rg.Vector3d.VectorAngle(s,rg.Vector3d(i))
    angleList.append(angle)

c= angleList


#[4]
exploded= []
NewMesh= m.Duplicate()

for i in range (NewMesh.Faces.Count):
    face=NewMesh.Faces.ExtractFaces([0])
    exploded.append(face)

d= exploded


#[5]
trans= []
for i in range (len(d)):
    result= i.Transform

trans.append(result)
