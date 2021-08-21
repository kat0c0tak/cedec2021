from pxr import Usd, Sdf, UsdGeom, UsdShade, UsdLux

# Create new USD file
stage = Usd.Stage.CreateNew("rect_light.usda")

# Add assets into stage
scene = stage.DefinePrim("/Scene")
scene.GetReferences().AddReference("./monkey_set.usda")

# Light
rectLight = UsdLux.RectLight.Define(stage, '/Scene/Light/RectLight')
rectLight.AddTranslateOp().Set(value=(2, 2, 0))
rectLight.AddRotateYOp().Set(value=(90))
rectLight.AddRotateXOp().Set(value=(-45))
rectLight.CreateIntensityAttr().Set(5)

rectLight.CreateWidthAttr().Set(6)
rectLight.CreateHeightAttr().Set(0.5)

# Save as USD file
stage.Save()