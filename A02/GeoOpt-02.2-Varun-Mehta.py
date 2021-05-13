"""
***SUN VECTOR***
GeoOpt-02.2-Varun-Mehta
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

origin=rg.Point3d(0,0,0)
a= sphere= rg.Sphere(origin,1)

b = point= a.PointAt(math.pi, 2*math.pi)

#c1 = rs.CreateVector(b) cross check this part
c = rg.Vector3d.Negate(b-origin)
