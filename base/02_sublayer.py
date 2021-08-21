from pxr import Usd, Sdf

sublayer1 = Usd.Stage.CreateNew("sublayer1.usda")
prim = sublayer1.DefinePrim("/Asset")
prim.CreateAttribute("test1", Sdf.ValueTypeNames.Int).Set(1)
sublayer1.Save()

sublayer2 = Usd.Stage.CreateNew("sublayer2.usda")
prim = sublayer2.DefinePrim("/Asset")
prim.CreateAttribute("test2", Sdf.ValueTypeNames.Int).Set(2)
sublayer2.Save()

stage = Usd.Stage.CreateNew("root_sublayer.usda")
stage.GetRootLayer().subLayerPaths.append("sublayer1.usda")
stage.GetRootLayer().subLayerPaths.append("sublayer2.usda")
stage.Save()

stage.Flatten().Export("flatten_sublayer.usda")