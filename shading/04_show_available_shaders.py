from pxr import Sdr
try:
    reg = Sdr.Registry()
except:
    pass
reg = Sdr.Registry()

# Available shaders
print(reg.GetNodeNames())
# ['HwPtexTexture', 'HwUvTexture', ... ]

# Inputs and outputs of the specific shader
node = reg.GetNodeByName('UsdPreviewSurface')
print(node.GetInputNames())
# ['clearcoat', 'clearcoatRoughness', 'diffuseColor', .. ]
print(node.GetOutputNames())
# ['displacement', 'surface']

# Details of the specific input or output
inDiffuse = node.GetInput('diffuseColor')
inDiffuseType, _ = inDiffuse.GetTypeAsSdfType()
print("diffuseColor's type: {}".format(inDiffuseType))
# diffuseColor's type: color3f
outSurface = node.GetOutput('surface')
outSurfaceType, _ = outSurface.GetTypeAsSdfType()
print("surface's type: {}".format(outSurfaceType))
# surface's type: token