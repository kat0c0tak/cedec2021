from pxr import Usd, UsdGeom

stage = Usd.Stage.CreateNew("xformable.usda")

xform = UsdGeom.Xform.Define(stage, "/Xform")
xform.AddRotateXOp().Set(90)
xform.AddTranslateOp().Set((2,0,0))

mesh = UsdGeom.Cone.Define(stage, "/Xform/Cone")
mesh.CreateAxisAttr("Y")
mesh.CreateHeightAttr(2)

stage.Save()