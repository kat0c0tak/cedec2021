from pxr import Usd, Sdf, UsdGeom, UsdShade

# Create new USD file
stage = Usd.Stage.CreateNew("simple.usda")

# Mesh
mesh = UsdGeom.Sphere.Define(stage, "/Simple/Sphere")

# Material
material = UsdShade.Material.Define(stage, '/Simple/Material')

# UsdPreviewSurface Shader in the Material
shader = UsdShade.Shader.Define(stage, '/Simple/Material/Shader')
shader.CreateIdAttr("UsdPreviewSurface")
shader.CreateInput(
    "diffuseColor",
    Sdf.ValueTypeNames.Color3f
).Set((1.0, 0.0, 0.0))
shaderOut = shader.CreateOutput(
    'surface', Sdf.ValueTypeNames.Token)

# Connect shader surface -> Material output
material.CreateSurfaceOutput().ConnectToSource(shaderOut)

# Assign material to Mesh
UsdShade.MaterialBindingAPI(mesh).Bind(material)

# Save as USD file
stage.Save()