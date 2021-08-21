from pxr import Usd, UsdGeom

stage = Usd.Stage.CreateNew("camera.usda")
stage.GetRootLayer().subLayerPaths.append("../data/model/monkey.usda")

camera_xform = UsdGeom.Xform.Define(stage, "/Camera")
camera_xform.AddTranslateOp().Set(value=(0,0,10))

usd_default_cam = UsdGeom.Camera.Define(stage, "/Camera/usd_default_cam")

maya_default_cam = UsdGeom.Camera.Define(stage, "/Camera/maya_default_cam")
maya_default_cam.GetHorizontalApertureAttr().Set(36.0)
maya_default_cam.GetVerticalApertureAttr().Set(24.0)
maya_default_cam.GetFocalLengthAttr().Set(35)

stage.Save()