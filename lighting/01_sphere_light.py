from pxr import Usd, Sdf, UsdGeom, UsdShade, UsdLux

# Create new USD file
stage = Usd.Stage.CreateNew("sphere_light.usda")

scene = stage.DefinePrim("/Scene")
scene.GetReferences().AddReference("./monkey_set.usda")

# Light
sphereLight = UsdLux.SphereLight.Define(stage, '/Scene/Light/SphereLight')
sphereLight.AddTranslateOp().Set(value=(-1, 3, 1))
sphereLight.CreateIntensityAttr().Set(10)

# Save as USD file
stage.Save()