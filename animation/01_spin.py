from pxr import Usd, UsdGeom

stage = Usd.Stage.CreateNew("spin.usda")
stage.SetStartTimeCode(0)
stage.SetEndTimeCode(100)

spin_xform = UsdGeom.Xform.Define(stage, "/spin")
spin = spin_xform.AddRotateYOp()
spin.Set(time=0, value=0)
spin.Set(time=100, value=360)

monkey_geo = UsdGeom.Mesh.Define(stage, "/spin/monkey_geo")
monkey_geo.GetPrim().GetReferences().AddReference("../data/model/monkey.usda")

stage.Save()