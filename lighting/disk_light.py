from pxr import Usd, Sdf, UsdGeom, UsdShade, UsdLux

# Create new USD file
stage = Usd.Stage.CreateNew("disk_light.usda")

# Add assets into stage
scene = stage.DefinePrim("/Scene")
scene.GetReferences().AddReference("./monkey_set.usda")

# Light
diskLight = UsdLux.DiskLight.Define(stage, '/Scene/Light/DiskLight')
diskLight.AddTranslateOp().Set(value=(4, 4, 0))
diskLight.AddRotateYOp().Set(value=(90))
diskLight.AddRotateXOp().Set(value=(-45))
diskLight.CreateIntensityAttr().Set(5)

diskLight.CreateRadiusAttr().Set(3)
# Save as USD file
stage.Save()