from pxr import Usd
stage = Usd.Stage.CreateNew("variantsets.usda")
prim = stage.DefinePrim("/RootPrim")
varSet = prim.GetVariantSets().AddVariantSet("TestVariant")
varSet.AddVariant("AAA")
varSet.AddVariant("BBB")
varSet.SetVariantSelection("AAA")

varEditTarget = varSet.GetVariantEditTarget()
with Usd.EditContext(stage, varEditTarget):
	stage.DefinePrim("/RootPrim/test")

stage.Save()
stage.Flatten().Export("flatten_variantsets.usda")

print stage.GetRootLayer().ExportToString()
print stage.Flatten().ExportToString()
