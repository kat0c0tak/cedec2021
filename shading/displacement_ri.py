from pxr import Usd, Sdf, UsdGeom, UsdShade

# Create new USD file
stage = Usd.Stage.CreateNew("displacement_ri.usda")

# Mesh
mesh = UsdGeom.Mesh.Define(stage, "/Texture/Plane")
mesh.GetPrim().GetReferences().AddReference("../data/model/plane.usda")
mesh.CreatePrimvar(
    "ri:attributes:displacementbound:sphere", 
    Sdf.ValueTypeNames.Float, 
).Set(0.1)

# Material
material = UsdShade.Material.Define(stage, '/Texture/Material')

# Read UV
stReader = UsdShade.Shader.Define(stage, '/Texture/Material/stReader')
stReader.CreateIdAttr('UsdPrimvarReader_float2')
stReader.CreateInput('varname', Sdf.ValueTypeNames.Token).Set('st')

# Diffuse texture
diffuseTextureSampler = UsdShade.Shader.Define(stage,'/Texture/Material/diffuseTexture')
diffuseTextureSampler.CreateIdAttr('UsdUVTexture')
diffuseTextureSampler.CreateInput('file', Sdf.ValueTypeNames.Asset).Set("../data/texture/gravel/diff.png")
diffuseTextureSampler.CreateInput("st", Sdf.ValueTypeNames.Float2).ConnectToSource(stReader.ConnectableAPI(), 'result')
diffuseTextureSampler.CreateOutput('rgb', Sdf.ValueTypeNames.Float3)

# Displacement texture
displacementTextureSampler = UsdShade.Shader.Define(stage,'/Texture/Material/displacementTexture')
displacementTextureSampler.CreateIdAttr('UsdUVTexture')
displacementTextureSampler.CreateInput('file', Sdf.ValueTypeNames.Asset).Set("../data/texture/gravel/disp.png")
displacementTextureSampler.CreateInput("st", Sdf.ValueTypeNames.Float2).ConnectToSource(stReader.ConnectableAPI(), 'result')
displacementTextureSampler.CreateOutput('r', Sdf.ValueTypeNames.Float)

# Normal texture
normalTextureSampler = UsdShade.Shader.Define(stage,'/Texture/Material/normalTexture')
normalTextureSampler.CreateIdAttr('UsdUVTexture')
normalTextureSampler.CreateInput('file', Sdf.ValueTypeNames.Asset).Set("../data/texture/gravel/nor.png")
normalTextureSampler.CreateInput("st", Sdf.ValueTypeNames.Float2).ConnectToSource(stReader.ConnectableAPI(), 'result')
normalTextureSampler.CreateOutput('rgb', Sdf.ValueTypeNames.Float3)

# Roughtness texture
roughnessTextureSampler = UsdShade.Shader.Define(stage,'/Texture/Material/roughnessTexture')
roughnessTextureSampler.CreateIdAttr('UsdUVTexture')
roughnessTextureSampler.CreateInput('file', Sdf.ValueTypeNames.Asset).Set("../data/texture/gravel/rough.png")
roughnessTextureSampler.CreateInput("st", Sdf.ValueTypeNames.Float2).ConnectToSource(stReader.ConnectableAPI(), 'result')
roughnessTextureSampler.CreateOutput('rgb', Sdf.ValueTypeNames.Float3)

# PxrSurface Shader
pxrSurface = UsdShade.Shader.Define(stage, '/Texture/Material/pxrSurface')
pxrSurface.CreateIdAttr("PxrSurface")
pxrSurface.CreateInput("diffuseColor", Sdf.ValueTypeNames.Color3f).ConnectToSource(diffuseTextureSampler.ConnectableAPI(), 'rgb')
pxrSurface.CreateInput("normal", Sdf.ValueTypeNames.Color3f).ConnectToSource(normalTextureSampler.ConnectableAPI(), 'rgb')
pxrSurface.CreateInput("roughness", Sdf.ValueTypeNames.Color3f).ConnectToSource(roughnessTextureSampler.ConnectableAPI(), 'rgb')

# PxrDisplace shader
pxrDisplace = UsdShade.Shader.Define(stage, '/Texture/Material/DisplacementShader')
pxrDisplace.CreateIdAttr("PxrDisplace")
pxrDisplace.CreateInput('dispAmount', Sdf.ValueTypeNames.Float).Set(0.05)
pxrDisplace.CreateInput("dispScalar", Sdf.ValueTypeNames.Float).ConnectToSource(displacementTextureSampler.ConnectableAPI(), 'r')

material.CreateSurfaceOutput("ri").ConnectToSource(pxrSurface.ConnectableAPI(), "surface")
material.CreateDisplacementOutput("ri").ConnectToSource(pxrDisplace.ConnectableAPI(), "displacement")

# Assign material to Mesh
UsdShade.MaterialBindingAPI(mesh).Bind(material)

# Save as USD file
stage.Save()