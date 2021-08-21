from pxr import Usd, UsdGeom

stage = Usd.Stage.CreateNew("cube_on_plane.usda")
stage.DefinePrim("/CubeOnPlane")

plane_xform = UsdGeom.Xform.Define(stage, "/CubeOnPlane/Plane")
plane_xform.AddScaleOp().Set(value=(10, 1, 10))
plane = UsdGeom.Mesh.Define(stage, "/CubeOnPlane/Plane/plane_geo")
plane.CreatePointsAttr([(-1,0,-1), (-1,0,1), (1,0,1), (1,0,-1)])
plane.CreateFaceVertexCountsAttr([4])
plane.CreateFaceVertexIndicesAttr([0,1,2,3])

cube_xform = UsdGeom.Xform.Define(stage, "/CubeOnPlane/Cube")
cube_xform.AddTranslateOp().Set(value=(-3, 1, 0))
cube_xform.AddRotateYOp().Set(20)
cube = UsdGeom.Cube.Define(stage, "/CubeOnPlane/Cube/cube_geo")

monkey_xform = UsdGeom.Xform.Define(stage, "/CubeOnPlane/Monkey")
monkey_xform.AddTranslateOp().Set(value=(0,2,0))
monkey = UsdGeom.Mesh.Define(stage, "/CubeOnPlane/Monkey/monkey_geo")
monkey.GetPrim().GetReferences().AddReference("../data/model/monkey.usda")
stage.Save()