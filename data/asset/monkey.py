from pxr import Usd, Sdf, UsdGeom, UsdShade, UsdLux

# Create new USD file
stage = Usd.Stage.CreateNew("monkey.usda")
stage.SetDefaultPrim(stage.DefinePrim("/Monkey"))

# Monkey model
monkey = UsdGeom.Mesh.Define(stage, "/Monkey/monkey_geom")
monkey.GetPrim().GetReferences().AddReference("../model/monkey.usda")

# Blue Material
blueMat = UsdShade.Material.Define(stage, '/Monkey/monkey_mat')

# UsdPreviewSurface Shader in the Material
# previewShader = UsdShade.Shader.Define(stage, '/Monkey/monkey_mat/PreviewShader')
# previewShader.CreateIdAttr("UsdPreviewSurface")
# previewShader.CreateInput("diffuseColor", Sdf.ValueTypeNames.Color3f).Set((0.6, 0.6, 0.9))

# PxrSurface
surfaceShader = UsdShade.Shader.Define(stage, '/Monkey/monkey_mat/SurfaceShader')
surfaceShader.CreateIdAttr("PxrSurface")
surfaceShader.CreateInput("diffuseColor", Sdf.ValueTypeNames.Color3f).Set((0.6, 0.6, 0.9))

# Connect pbrShader surface -> Material output
# blueMat.CreateSurfaceOutput().ConnectToSource(previewShader.ConnectableAPI(), "surface")
blueMat.CreateSurfaceOutput("ri").ConnectToSource(surfaceShader.ConnectableAPI(), "out")

# Assign blueMat to Mesh
UsdShade.MaterialBindingAPI(monkey).Bind(blueMat)

# Save as USD file
stage.Save()