from pxr import Usd, Sdf, UsdGeom, UsdShade

# Create new USD file
stage = Usd.Stage.CreateNew("displacement.usda")

# Mesh
mesh = UsdGeom.Mesh.Define(stage, "/Texture/Plane")
mesh.GetPrim().GetReferences().AddReference("../data/model/plane.usda")

# Material
material = UsdShade.Material.Define(stage, '/Texture/Material')

# Read UV
stReader = UsdShade.Shader.Define(stage, '/Texture/Material/stReader')
stReader.CreateIdAttr('UsdPrimvarReader_float2')
stReader.CreateInput('varname', Sdf.ValueTypeNames.Token).Set('st')
stReaderOut = stReader.CreateOutput('result', Sdf.ValueTypeNames.Float2)

# Diffuse texture
diffuseTexture = UsdShade.Shader.Define(stage,'/Texture/Material/diffuseTexture')
diffuseTexture.CreateIdAttr('UsdUVTexture')
diffuseTexture.CreateInput('file', Sdf.ValueTypeNames.Asset).Set("../data/texture/gravel/diff.png")
diffuseTexture.CreateInput("st", Sdf.ValueTypeNames.Float2).ConnectToSource(stReaderOut)
diffuseTextureRGB = diffuseTexture.CreateOutput('rgb', Sdf.ValueTypeNames.Float3)

# Displacement texture
displacementTexture = UsdShade.Shader.Define(stage,'/Texture/Material/displacementTexture')
displacementTexture.CreateIdAttr('UsdUVTexture')
displacementTexture.CreateInput('file', Sdf.ValueTypeNames.Asset).Set("../data/texture/gravel/disp.png")
displacementTexture.CreateInput("st", Sdf.ValueTypeNames.Float2).ConnectToSource(stReaderOut)
displacementTextureR = displacementTexture.CreateOutput('r', Sdf.ValueTypeNames.Float)

# Normal texture
normalTexture = UsdShade.Shader.Define(stage,'/Texture/Material/normalTexture')
normalTexture.CreateIdAttr('UsdUVTexture')
normalTexture.CreateInput('file', Sdf.ValueTypeNames.Asset).Set("../data/texture/gravel/nor.png")
normalTexture.CreateInput("st", Sdf.ValueTypeNames.Float2).ConnectToSource(stReaderOut)
normalTextureRGB = normalTexture.CreateOutput('rgb', Sdf.ValueTypeNames.Float3)

# Roughtness texture
roughTexture = UsdShade.Shader.Define(stage,'/Texture/Material/roughnessTexture')
roughTexture.CreateIdAttr('UsdUVTexture')
roughTexture.CreateInput('file', Sdf.ValueTypeNames.Asset).Set("../data/texture/gravel/rough.png")
roughTexture.CreateInput("st", Sdf.ValueTypeNames.Float2).ConnectToSource(stReaderOut)
roughTextureRGB = roughTexture.CreateOutput('rgb', Sdf.ValueTypeNames.Float3)

# UsdPreviewSurface Shader in the Material
previewSurface = UsdShade.Shader.Define(stage, '/Texture/Material/previewSurface')
previewSurface.CreateIdAttr("UsdPreviewSurface")
previewSurface.CreateInput("diffuseColor", Sdf.ValueTypeNames.Color3f).ConnectToSource(diffuseTextureRGB)
previewSurface.CreateInput("displacement", Sdf.ValueTypeNames.Float).ConnectToSource(displacementTextureR)
previewSurface.CreateInput("normal", Sdf.ValueTypeNames.Color3f).ConnectToSource(normalTextureRGB)
previewSurface.CreateInput("roughness", Sdf.ValueTypeNames.Color3f).ConnectToSource(roughTextureRGB)
previewSurfaceOut = previewSurface.CreateOutput('sourface', Sdf.ValueTypeNames.Token)
previewSurfaceOutDisp = previewSurface.CreateOutput('displacement', Sdf.ValueTypeNames.Token)

# Connect shader surface -> Material output
material.CreateSurfaceOutput().ConnectToSource(previewSurfaceOut)
material.CreateDisplacementOutput().ConnectToSource(previewSurfaceOutDisp)

# Assign material to Mesh
UsdShade.MaterialBindingAPI(mesh).Bind(material)

# Save as USD file
stage.Save()