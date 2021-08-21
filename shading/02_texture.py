from pxr import Usd, Sdf, UsdGeom, UsdShade

# Create new USD file
stage = Usd.Stage.CreateNew("texture.usda")

# Mesh
mesh = UsdGeom.Mesh.Define(stage, "/Texture/plane")
mesh.GetPrim().GetReferences().AddReference("../data/model/plane.usda")

# Material
material = UsdShade.Material.Define(stage, '/Texture/Material')

# Read UV
stReader = UsdShade.Shader.Define(stage, '/Texture/Material/stReader')
stReader.CreateIdAttr('UsdPrimvarReader_float2')
stReader.CreateInput('varname', Sdf.ValueTypeNames.Token).Set('st')
stReaderOut = stReader.CreateOutput('result', Sdf.ValueTypeNames.Float2)

# Diffuse texture
diffTexture = UsdShade.Shader.Define(stage,'/Texture/Material/diffTexture')
diffTexture.CreateIdAttr('UsdUVTexture')
diffTexture.CreateInput('file', Sdf.ValueTypeNames.Asset).Set("../data/texture/gravel/diff.png")
diffTexture.CreateInput("st", Sdf.ValueTypeNames.Float2).ConnectToSource(stReaderOut)
diffTextureOut = diffTexture.CreateOutput('rgb', Sdf.ValueTypeNames.Float3)

# UsdPreviewSurface Shader
previewSurface = UsdShade.Shader.Define(stage, '/Texture/Material/previewSurface')
previewSurface.CreateIdAttr("UsdPreviewSurface")
previewSurface.CreateInput("diffuseColor", Sdf.ValueTypeNames.Color3f).ConnectToSource(diffTextureOut)
previewSurfaceOut = previewSurface.CreateOutput("surface", Sdf.ValueTypeNames.Token)

# Connect shader surface -> Material output
material.CreateSurfaceOutput().ConnectToSource(previewSurfaceOut)

# Assign material to Mesh
UsdShade.MaterialBindingAPI(mesh).Bind(material)

# Save as USD file
stage.Save()