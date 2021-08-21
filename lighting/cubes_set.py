from pxr import Usd, Sdf, UsdGeom, UsdShade, UsdLux

# Create new USD file
stage = Usd.Stage.CreateNew("cubes_set.usda")
stage.SetDefaultPrim(stage.DefinePrim("/Cubes_set"))

# Floor model
floor = UsdGeom.Mesh.Define(stage, "/Cubes_set/Floor")
floor.GetPrim().GetReferences().AddReference("../data/model/plane.usda")

# Cube
cube1 = UsdGeom.Cube.Define(stage, "/Cubes_set/Cube1")
cube1.AddTranslateOp().Set(value=(0, 1, 0))

# Cube
cube2 = UsdGeom.Cube.Define(stage, "/Cubes_set/Cube2")
cube2.AddTranslateOp().Set(value=(-3, 1, 0))
cube2.AddRotateYOp().Set(20)

# White Material
whiteMat = UsdShade.Material.Define(stage, '/Cubes_set/Material/WhiteMat')

# UsdPreviewSurface
previewShader = UsdShade.Shader.Define(stage, '/Cubes_set/Material/WhiteMat/PreviewShader')
previewShader.CreateIdAttr("UsdPreviewSurface")
previewShader.CreateInput("diffuseColor", Sdf.ValueTypeNames.Color3f).Set((0.9, 0.9, 0.9))

# PxrSurface
surfaceShader = UsdShade.Shader.Define(stage, '/Cubes_set/Material/WhiteMat/SurfaceShader')
surfaceShader.CreateIdAttr("PxrSurface")
surfaceShader.CreateInput("diffuseColor", Sdf.ValueTypeNames.Color3f).Set((0.9, 0.9, 0.9))

# Connect pbrShader surface -> Material output
whiteMat.CreateSurfaceOutput().ConnectToSource(previewShader.ConnectableAPI(), "surface")
whiteMat.CreateSurfaceOutput("ri").ConnectToSource(surfaceShader.ConnectableAPI(), "out")

# Assign blueMat to Mesh
UsdShade.MaterialBindingAPI(cube1).Bind(whiteMat)
UsdShade.MaterialBindingAPI(cube2).Bind(whiteMat)

# Save as USD file
stage.Save()