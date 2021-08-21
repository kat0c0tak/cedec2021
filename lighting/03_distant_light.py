from pxr import Usd, Sdf, UsdGeom, UsdShade, UsdLux

# Create new USD file
stage = Usd.Stage.CreateNew("distant_light.usda")

# Add assets into stage
scene = stage.DefinePrim("/Scene")
scene.GetReferences().AddReference("./monkey_set.usda")

# Light
distantLight = UsdLux.DistantLight.Define(stage, '/Scene/Light/DistantLight')
distantLight.AddRotateYOp().Set(value=(90))
distantLight.AddRotateXOp().Set(value=(-45))
distantLight.CreateIntensityAttr().Set(10000)

# Higher values soften the shadow and increase the amount of light
# The default value is 0.53 as the same as Sun
distantLight.CreateAngleAttr().Set(1)

# Save as USD file
stage.Save()