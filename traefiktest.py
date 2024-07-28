import sys
import requests
from datetime import datetime

def req(u,k,v):
  try:
  
    h = {}
    r = requests.head(u, verify=False, headers= ({k:v} if k else {}))
    return r.status_code
  except requests.ConnectionError:
    return None




p = ""
r = {"allow":0, "deny": 0, "error": 0}
k= sys.argv[2] if len(sys.argv) == 4 else ""
v= sys.argv[3] if len(sys.argv) == 4 else ""
while True:
  sts = req(sys.argv[1],k,v)
  dt = datetime.now().strftime("%m/%d/%Y %H:%M:%S")
  if dt != p:
    if p:
      print(p,r)
    r = {"allow":0, "deny": 0, "error": 0}
  p = dt
  if not sts:
    r["error"] += 1
    continue
  if str(sts) == "429":
    r["deny"] += 1
  else:  
    r["allow"] += 1
