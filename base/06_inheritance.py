from pxr import Usd, Sdf

stage = Usd.Stage.CreateNew("inheritance.usda")
classA = stage.CreateClassPrim("/ClassA")
classA.CreateAttribute("test", Sdf.ValueTypeNames.Int).Set(1)
prim = stage.DefinePrim("/RootPrim")
prim.GetInherits().AddInherit(classA.GetPath())
stage.Save()

stage.Flatten().Export("flatten_inheritance.usda")

print stage.GetRootLayer().ExportToString()