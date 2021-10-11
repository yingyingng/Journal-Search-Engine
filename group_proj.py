import json
import os

f = open("master.json", encoding = "utf8")
pub = json.loads(f.read())

print(pub)