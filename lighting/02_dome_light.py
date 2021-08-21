from pxr import Usd, Sdf, UsdGeom, UsdShade, UsdLux

# Create new USD file
stage = Usd.Stage.CreateNew("dome_light.usda")

scene = stage.DefinePrim("/Scene")
scene.GetReferences().AddReference("./monkey_set.usda")

# Light
domeLight = UsdLux.DomeLight.Define(stage, '/Scene/Light/DomeLight')
domeLight.CreateTextureFileAttr('../data/texture/hdri/lilienstein_1k.tex')

# Portal Light
# It's not supported by Renderman now
# portalLight = UsdLux.PortalLight.Define(stage, '/Root/Light/PortalLight')
# portalLight.AddTranslateOp().Set(value=(0, 5, 0))
# domeLight.CreatePortalsRel().SetTargets(["/Root/Light/PortalLight"])

# Save as USD file
stage.Save()