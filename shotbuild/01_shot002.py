from pxr import Usd, UsdGeom, UsdLux, Sdf

SHOT_NAME = "Shot002"
SHOT_PATH = "/{}".format(SHOT_NAME)

# Shot
stage = Usd.Stage.CreateNew(SHOT_NAME+".usda")
stage.SetStartTimeCode(1)
stage.SetEndTimeCode(200)


# Create layer and set EditTarget
layout_layer = Sdf.Layer.CreateNew(SHOT_NAME+"_layout.usda")
stage.GetRootLayer().subLayerPaths.append(layout_layer.identifier)
stage.SetEditTarget(Usd.EditTarget(layout_layer))
# Create prims
UsdGeom.Scope.Define(stage, SHOT_PATH)
UsdGeom.Scope.Define(stage, SHOT_PATH+"/Asset")
UsdGeom.Scope.Define(stage, SHOT_PATH+"/Character")
UsdGeom.Scope.Define(stage, SHOT_PATH+"/Camera")
UsdGeom.Scope.Define(stage, SHOT_PATH+"/Light")
cube_set_xform = UsdGeom.Xform.Define(stage, SHOT_PATH+"/Asset/Cube_set")
cube_set_xform.GetPrim().GetReferences().AddReference("../data/asset/cube_set.usda")
monkey_xform = UsdGeom.Xform.Define(stage, SHOT_PATH+"/Character/Monkey")
monkey_xform.GetPrim().GetReferences().AddReference("../data/asset/monkey.usda")
camera_xform = UsdGeom.Xform.Define(stage, SHOT_PATH+"/Camera/RenderCamera")
camera_xform.AddTranslateOp().Set(value=(0, 2, 15))
camera = UsdGeom.Camera.Define(stage, SHOT_PATH+"/Camera/RenderCamera/renderCamera_cam")


# Animation
anim_layer = Sdf.Layer.CreateNew(SHOT_NAME+"_anim.usda")
stage.GetRootLayer().subLayerPaths.append(anim_layer.identifier)
stage.SetEditTarget(Usd.EditTarget(anim_layer))
monkey_over = stage.OverridePrim(SHOT_PATH+"/Character/Monkey")
monkey_xform = UsdGeom.Xform(monkey_over)
monkey_xform.AddTranslateOp().Set(value=(0, 2, 0))
spin = monkey_xform.AddRotateYOp(opSuffix="spin")
spin.Set(time=1, value=0)
spin.Set(time=100, value=359)


# Lighting
lighting_layer = Sdf.Layer.CreateNew(SHOT_NAME+"_lighting.usda")
stage.GetRootLayer().subLayerPaths.append(lighting_layer.identifier)
stage.SetEditTarget(Usd.EditTarget(lighting_layer))
domeLight = UsdLux.DomeLight.Define(stage, SHOT_PATH+"/Light/Dome")
domeLight.CreateTextureFileAttr("../data/texture/hdri/lilienstein.tex")
domeLightSpin = domeLight.AddRotateYOp()
domeLightSpin.Set(time=101, value=90)
domeLightSpin.Set(time=200, value=450)
distantLight = UsdLux.DistantLight.Define(stage, SHOT_PATH+"/Light/Distant")
distantLight.AddRotateXOp().Set(value=(-45))
distantLight.CreateIntensityAttr().Set(100000)
distantLightSpin = distantLight.AddRotateYOp()
distantLightSpin.Set(time=101, value=90)
distantLightSpin.Set(time=200, value=450)


# Save all layers
stage.Save()