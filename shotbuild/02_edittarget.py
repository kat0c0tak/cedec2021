from pxr import Usd, Sdf

# Create stage
stage = Usd.Stage.CreateNew("edittarget.usda")
stage.DefinePrim("/PrimOnRoot")

# Create layer
layer = Sdf.Layer.CreateNew("edittarget_layer.usda")

# Add the layer as sublayer on RootLayer
stage.GetRootLayer().subLayerPaths.append(layer.identifier)

# Set current EditTarget layer
stage.SetEditTarget(Usd.EditTarget(layer))

# Create prim on the layer
stage.DefinePrim("/PrimOnLayer")

stage.Save()