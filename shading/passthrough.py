from pxr import Usd, Sdf, UsdGeom, UsdShade

# Create new USD file
stage = Usd.Stage.CreateNew("passthrough.usda")

# Mesh
mesh = UsdGeom.Sphere.Define(stage, "/Simple/Sphere")

# Material
material = UsdShade.Material.Define(stage, '/Simple/Material')

# UsdPreviewSurface Shader in the Material
shader = UsdShade.Shader.Define(stage, '/Simple/Material/Shader')
shader.CreateIdAttr("UsdPreviewSurface")
diffuseColor = shader.CreateInput(
    "diffuseColor", Sdf.ValueTypeNames.Color3f)
diffuseColor.Set((1.0, 0.0, 0.0))

# Connect shader surface -> Material output
surfaceTerminal = material.CreateSurfaceOutput()
shaderOut = shader.CreateOutput(
    'surface', Sdf.ValueTypeNames.Token)
surfaceTerminal.ConnectToSource(shaderOut)

dummyMat = UsdShade.Material.Define(stage, '/Simple/dummyMat')
dummyIn = dummyMat.CreateInput('test', Sdf.ValueTypeNames.Token)
dummyIn.ConnectToSource(surfaceTerminal)
dummyOut = dummyMat.CreateSurfaceOutput()
dummyOut.ConnectToSource(dummyIn)

# Assign material to Mesh
UsdShade.MaterialBindingAPI(mesh).Bind(dummyMat)

# Save as USD file
stage.Save()