from pxr import Usd, Sdf

payload = Usd.Stage.CreateNew("ref1.usda")
prim = payload.DefinePrim("/PayloadPrim")
prim.CreateAttribute("test", Sdf.ValueTypeNames.Int).Set(1)
payload.SetDefaultPrim(prim)
payload.Save()

_stage = Usd.Stage.CreateNew("root_payloads.usda")
prim = _stage.DefinePrim("/RootPrim")
prim.GetPayloads().AddPayload("payload1.usda")
_stage.Save()

stage = Usd.Stage.Open("root_payloads.usda", load=Usd.Stage.LoadNone)
stage.Flatten().Export("flatten_payloads_LoadNone.usda")

stage.Load()
stage.Flatten().Export("flatten_payloads_LoadAll.usda")