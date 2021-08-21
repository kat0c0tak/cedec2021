from pxr import Usd, Sdf, UsdGeom, UsdShade

# Create new USD file
stage = Usd.Stage.CreateNew("simple_material_input.usda")

# Mesh
mesh = UsdGeom.Sphere.Define(stage, "/Simple/Sphere")

# Material
material = UsdShade.Material.Define(stage, '/Simple/Material')
materialDiffIn = material.CreateInput(
    "diff", Sdf.ValueTypeNames.Color3f)
materialDiffIn.Set((1.0, 0.0, 0.0))

# UsdPreviewSurface Shader in the Material
shader = UsdShade.Shader.Define(stage, '/Simple/Material/Shader')
shader.CreateIdAttr("UsdPreviewSurface")
diffuseColor = shader.CreateInput(
    "diffuseColor", Sdf.ValueTypeNames.Color3f)
diffuseColor.ConnectToSource(materialDiffIn)

# Connect shader surface -> Material output
surfaceTerminal = material.CreateSurfaceOutput()
shaderOut = shader.CreateOutput(
    'surface', Sdf.ValueTypeNames.Token)
surfaceTerminal.ConnectToSource(shaderOut)

# Assign material to Mesh
UsdShade.MaterialBindingAPI(mesh).Bind(material)

# Save as USD file
stage.Save()