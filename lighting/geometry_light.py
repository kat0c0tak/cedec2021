from pxr import Usd, Sdf, UsdGeom, UsdShade, UsdLux

# Create new USD file
stage = Usd.Stage.CreateNew("geometry_light.usda")

# Add assets into stage
scene = stage.DefinePrim("/Scene")
scene.GetReferences().AddReference("./monkey_set.usda")

# Light
geometryLight = UsdLux.GeometryLight.Define(stage, '/Scene/Light/GeometryLight')
geometryLight.CreateGeometryRel().SetTargets(["/Scene/Monkey"])

# Save as USD file
stage.Save()