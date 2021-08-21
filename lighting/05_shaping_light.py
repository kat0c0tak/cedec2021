from pxr import Usd, Sdf, UsdGeom, UsdShade, UsdLux

# Create new USD file
stage = Usd.Stage.CreateNew("shaping_light.usda")

# Add assets into stage
scene = stage.DefinePrim("/Scene")
scene.GetReferences().AddReference("./monkey_set.usda")

# Light
sphereLight = UsdLux.SphereLight.Define(stage, '/Scene/Light/DiskLight')
sphereLight.AddTranslateOp().Set(value=(0, 4, 0))
sphereLight.AddRotateYOp().Set(value=(90))
sphereLight.AddRotateXOp().Set(value=(-90))
sphereLight.CreateIntensityAttr().Set(5)

api = UsdLux.ShapingAPI(sphereLight)
api.CreateShapingConeAngleAttr().Set(30)

# Save as USD file
stage.Save()