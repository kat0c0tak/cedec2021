from pxr import Usd, Sdf, UsdGeom, UsdShade, UsdLux

# Create new USD file
stage = Usd.Stage.CreateNew("collection_light.usda")

# Add assets into stage
scene = stage.DefinePrim("/Scene")
scene.GetReferences().AddReference("./cubes_set.usda")

# Red light
redLight = UsdLux.SphereLight.Define(stage, '/Scene/Light/SphereLight1')
redLight.AddTranslateOp().Set(value=(-1.5, 8, 0))
redLight.CreateIntensityAttr().Set(100)
redLight.CreateColorAttr().Set(value=(1.0, 0.0, 0.0))

# Blue light
blueLight = UsdLux.SphereLight.Define(stage, '/Scene/Light/SphereLight2')
blueLight.AddTranslateOp().Set(value=(-0.5, 8, 0))
blueLight.CreateIntensityAttr().Set(100)
blueLight.CreateColorAttr().Set(value=(0.0, 0.0, 1.0))

# Light link collection
api = blueLight.GetLightLinkCollectionAPI()
api.CreateExcludesRel().SetTargets(["/Scene/Cube1"])

# Save as USD file
stage.Save()