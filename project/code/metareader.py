import json

exported_meta = {}

def connect(appjson):
 with open(appjson["meta_path"], "r") as f:
  meta = json.load(f)
  exported_meta["title"] = meta["title"]
  exported_meta["version"] = meta["version"]
  exported_meta["desc"] = meta["desc"]
  exported_meta["program"] = meta["program"]