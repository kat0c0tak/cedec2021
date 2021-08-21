from pxr import Usd, Sdf

ref = Usd.Stage.CreateNew("ref1.usda")
prim = ref.DefinePrim("/ReferencedPrim")
prim.CreateAttribute("test", Sdf.ValueTypeNames.Int).Set(1)
ref.SetDefaultPrim(prim)
ref.Save()

stage = Usd.Stage.CreateNew("root_references.usda")
prim = stage.DefinePrim("/RootPrim")
prim.GetReferences().AddReference("ref1.usda")
stage.Save()

stage.Flatten().Export("flatten_references.usda")