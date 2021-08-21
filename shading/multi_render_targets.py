from pxr import Usd, Sdf, UsdGeom, UsdShade

# Create new USD file
stage = Usd.Stage.CreateNew("multi_render_targets.usda")

# Mesh
mesh = UsdGeom.Sphere.Define(stage, "/Simple/Sphere")

# Material
material = UsdShade.Material.Define(stage, '/Simple/Material')

# UsdPreviewSurface Shader in the Material
previewSurface = UsdShade.Shader.Define(stage, '/Simple/Material/previewSurface')
previewSurface.CreateIdAttr("UsdPreviewSurface")
previewSurface.CreateInput("diffuseColor", Sdf.ValueTypeNames.Color3f).Set((1.0, 0.0, 0.0))

# PxrSurface Shader in the Material
pxrSurface = UsdShade.Shader.Define(stage, '/Simple/Material/pxrSurface')
pxrSurface.CreateIdAttr("PxrSurface")
pxrSurface.CreateInput("diffuseColor", Sdf.ValueTypeNames.Color3f).Set((0.0, 1.0, 0.0))

# Connect shader surface -> Material output
glSurfaceTerminal = material.CreateSurfaceOutput("glslfx")
previewSurfaceOut = previewSurface.CreateOutput('surface', Sdf.ValueTypeNames.Token)
glSurfaceTerminal.ConnectToSource(previewSurfaceOut)

# Connect shader surface -> Material output
riSurfaceTerminal = material.CreateSurfaceOutput("ri")
pxrSurfaceOut = pxrSurface.CreateOutput('surface', Sdf.ValueTypeNames.Token)
riSurfaceTerminal.ConnectToSource(pxrSurfaceOut)

# Assign material to Mesh
UsdShade.MaterialBindingAPI(mesh).Bind(material)

# Save as USD file
stage.Save()