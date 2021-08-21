from pxr import Usd, Sdf, UsdGeom

# Create new USD file
stage = Usd.Stage.CreateNew("base1.usda")

# Create new Sphere Prim
sphere = UsdGeom.Sphere.Define(stage, "/Sphere")

# Set attribute
sphere.CreateRadiusAttr().Set(2.0)

# Save as USD file
stage.Save()