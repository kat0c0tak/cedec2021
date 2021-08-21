from pxr import Usd, Sdf, UsdGeom, UsdShade, UsdLux

# Create new USD file
stage = Usd.Stage.CreateNew("cylinder_light.usda")

# Add assets into stage
scene = stage.DefinePrim("/Scene")
scene.GetReferences().AddReference("./monkey_set.usda")

# Light
cylinderLight = UsdLux.CylinderLight.Define(stage, '/Scene/Light/CylinderLight')
cylinderLight.AddTranslateOp().Set(value=(4, 4, 0))
cylinderLight.AddRotateYOp().Set(value=(90))
cylinderLight.AddRotateXOp().Set(value=(-45))
cylinderLight.CreateIntensityAttr().Set(5)

cylinderLight.CreateTreatAsLineAttr().Set(True)
# Save as USD file
stage.Save()