from pxr import Usd, Sdf, UsdGeom, UsdShade, UsdLux

# Create new USD file
stage = Usd.Stage.CreateNew("shadow_light.usda")

# Add assets into stage
scene = stage.DefinePrim("/Scene")
scene.GetReferences().AddReference("./monkey_set.usda")

# Light
distantLight = UsdLux.DistantLight.Define(stage, '/Scene/Light/DistantLight')
distantLight.AddRotateYOp().Set(value=(90))
distantLight.AddRotateXOp().Set(value=(-45))
distantLight.CreateIntensityAttr().Set(10000)
distantLight.CreateAngleAttr().Set(1)

# ShadowAPI
api = UsdLux.ShadowAPI(distantLight)
api.CreateShadowColorAttr().Set(value=(0.0, 1.0, 0.0))

# Save as USD file
stage.Save()