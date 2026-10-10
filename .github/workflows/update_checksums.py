"""Refresh every <!-- SHA256:START --> block from the Dynex Wallet release files."""
import hashlib, json, os, re, glob, urllib.request
OWNER, APP, TAG = "Dynex-project", "Dynex-Desktop-Wallet", os.environ.get("TAG", "v2.2.3")
TOKEN = os.environ.get("GITHUB_TOKEN", "")
API = f"https://api.github.com/repos/{OWNER}/{APP}"
def req(url, data=None, method="GET"):
    h = {"Accept": "application/vnd.github+json", "User-Agent": "dynex-checksums"}
    if TOKEN: h["Authorization"] = "Bearer " + TOKEN
    r = urllib.request.Request(url, data=data, headers=h, method=method)
    return urllib.request.urlopen(r, timeout=600)
rel = json.load(req(f"{API}/releases/tags/{TAG}"))
order = {"windows": 0, "macos": 1, "linux": 2}
rows = []
for a in sorted(rel["assets"], key=lambda a: min([v for k, v in order.items() if k in a["name"]] or [9])):
    n = a["name"]
    if not re.search(r"\.(exe|dmg|zip)$", n): continue
    h = hashlib.sha256()
    with urllib.request.urlopen(a["browser_download_url"], timeout=1200) as f:
        for chunk in iter(lambda: f.read(1 << 20), b""): h.update(chunk)
    plat = "Windows" if "windows" in n else "macOS" if "macos" in n else "Linux"
    rows.append(f"| {plat} | [`{n}`]({a['browser_download_url']}) | `{h.hexdigest()}` |")
    print(n, h.hexdigest())
block = "<!-- SHA256:START -->\n| Platform | File | SHA-256 |\n|---|---|---|\n" + "\n".join(rows) + "\n<!-- SHA256:END -->"
pat = re.compile(r"<!-- SHA256:START -->.*?<!-- SHA256:END -->", re.S)
changed = 0
for p in glob.glob("**/*.md", recursive=True):
    t = open(p, encoding="utf-8").read()
    n = pat.sub(block, t)
    if n != t: open(p, "w", encoding="utf-8").write(n); changed += 1
print("files changed:", changed)
if os.environ.get("UPDATE_RELEASE") == "1" and rel.get("body") and pat.search(rel["body"]):
    nb = pat.sub(block, rel["body"])
    if nb != rel["body"]:
        req(f"{API}/releases/{rel['id']}", json.dumps({"body": nb}).encode(), "PATCH"); print("release body updated")
