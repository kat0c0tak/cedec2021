from pxr import Usd, Sdf, UsdGeom, UsdShade, UsdLux

# Create new USD file
stage = Usd.Stage.CreateNew("cube_set.usda")
stage.SetDefaultPrim(stage.DefinePrim("/Cube_set"))

# Floor model
floor = UsdGeom.Xform.Define(stage, "/Cube_set/Ground")
floor.GetPrim().GetReferences().AddReference("./ground.usda")

# Cube
cube = UsdGeom.Xform.Define(stage, "/Cube_set/Cube")
UsdGeom.Cube.Define(stage, "/Cube_set/Cube/cube_geom")
cube.AddTranslateOp().Set(value=(-3, 1, 0))
cube.AddRotateYOp().Set(20)

# Red Material
redMat = UsdShade.Material.Define(stage, '/Cube_set/Cube/cube_mat')

# UsdPreviewSurface
# previewShader = UsdShade.Shader.Define(stage, '/Cube_set/Cube/cube_mat/PreviewShader')
# previewShader.CreateIdAttr("UsdPreviewSurface")
# previewShader.CreateInput("diffuseColor", Sdf.ValueTypeNames.Color3f).Set((0.8, 0.6, 0.6))

# PxrSurface
surfaceShader = UsdShade.Shader.Define(stage, '/Cube_set/Cube/cube_mat/SurfaceShader')
surfaceShader.CreateIdAttr("PxrSurface")
surfaceShader.CreateInput("diffuseColor", Sdf.ValueTypeNames.Color3f).Set((0.8, 0.6, 0.6))

# Connect pbrShader surface -> Material output
# redMat.CreateSurfaceOutput().ConnectToSource(previewShader.ConnectableAPI(), "surface")
redMat.CreateSurfaceOutput("ri").ConnectToSource(surfaceShader.ConnectableAPI(), "out")

# Assign redMat to Mesh
UsdShade.MaterialBindingAPI(cube).Bind(redMat)

# Save as USD file
stage.Save()