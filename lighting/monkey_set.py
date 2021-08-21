from pxr import Usd, Sdf, UsdGeom, UsdShade, UsdLux

# Create new USD file
stage = Usd.Stage.CreateNew("monkey_set.usda")
stage.SetDefaultPrim(stage.DefinePrim("/Monkey_set"))

# Floor model
floor = UsdGeom.Mesh.Define(stage, "/Monkey_set/Floor")
floor.GetPrim().GetReferences().AddReference("../data/model/plane.usda")

# Monkey model
monkey = UsdGeom.Mesh.Define(stage, "/Monkey_set/Monkey")
monkey.GetPrim().GetReferences().AddReference("../data/model/monkey.usda")
monkey.AddTranslateOp().Set(value=(0, 1, 0))

# Cube
cube = UsdGeom.Cube.Define(stage, "/Monkey_set/Cube")
cube.AddTranslateOp().Set(value=(-3, 1, 0))
cube.AddRotateYOp().Set(20)

# Red Material
redMat = UsdShade.Material.Define(stage, '/Monkey_set/Material/RedMat')

# UsdPreviewSurface
previewShader = UsdShade.Shader.Define(stage, '/Monkey_set/Material/RedMat/PreviewShader')
previewShader.CreateIdAttr("UsdPreviewSurface")
previewShader.CreateInput("diffuseColor", Sdf.ValueTypeNames.Color3f).Set((0.8, 0.6, 0.6))

# PxrSurface
surfaceShader = UsdShade.Shader.Define(stage, '/Monkey_set/Material/RedMat/SurfaceShader')
surfaceShader.CreateIdAttr("PxrSurface")
surfaceShader.CreateInput("diffuseColor", Sdf.ValueTypeNames.Color3f).Set((0.8, 0.6, 0.6))

# Connect pbrShader surface -> Material output
redMat.CreateSurfaceOutput().ConnectToSource(previewShader.ConnectableAPI(), "surface")
redMat.CreateSurfaceOutput("ri").ConnectToSource(surfaceShader.ConnectableAPI(), "out")

# Assign redMat to Mesh
UsdShade.MaterialBindingAPI(cube).Bind(redMat)

# Blue Material
blueMat = UsdShade.Material.Define(stage, '/Monkey_set/Material/BlueMat')

# UsdPreviewSurface Shader in the Material
previewShader = UsdShade.Shader.Define(stage, '/Monkey_set/Material/BlueMat/PreviewShader')
previewShader.CreateIdAttr("UsdPreviewSurface")
previewShader.CreateInput("diffuseColor", Sdf.ValueTypeNames.Color3f).Set((0.6, 0.6, 0.9))

# PxrSurface
surfaceShader = UsdShade.Shader.Define(stage, '/Monkey_set/Material/BlueMat/SurfaceShader')
surfaceShader.CreateIdAttr("PxrSurface")
surfaceShader.CreateInput("diffuseColor", Sdf.ValueTypeNames.Color3f).Set((0.6, 0.6, 0.9))

# Connect pbrShader surface -> Material output
blueMat.CreateSurfaceOutput().ConnectToSource(previewShader.ConnectableAPI(), "surface")
blueMat.CreateSurfaceOutput("ri").ConnectToSource(surfaceShader.ConnectableAPI(), "out")

# Assign blueMat to Mesh
UsdShade.MaterialBindingAPI(monkey).Bind(blueMat)

# Save as USD file
stage.Save()