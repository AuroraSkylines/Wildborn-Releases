"""Checks a published Wildborn release the way a player's launcher sees it:
anonymous HTTPS downloads of latest.json and the files it lists, compared by
size and SHA-256. Usage: python3 scripts/verify_release.py OWNER/REPO [TAG]
Without TAG it checks releases/latest (what stable players get)."""
import hashlib
import json
import os
import sys
import urllib.error
import urllib.request

repo = sys.argv[1]
tag = sys.argv[2] if len(sys.argv) > 2 else ""
# RELEASE_HOST exists only for local tests of this script.
base = f"{os.environ.get('RELEASE_HOST', 'https://github.com')}/{repo}/releases"
manifest_url = f"{base}/download/{tag}/latest.json" if tag else f"{base}/latest/download/latest.json"
prefix = f"{base}/download/"


def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": "wildborn-release-check"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read()


try:
    m = json.loads(get(manifest_url))
except urllib.error.HTTPError as e:
    sys.exit(f"{manifest_url}: HTTP {e.code} (no published release with a latest.json?)")
print(f"manifest {manifest_url}: {m['product']} {m['version']} ({m['channel']})")
if tag and tag != "v" + m["version"]:
    sys.exit(f"tag {tag} but manifest version {m['version']}")
if m["channel"] == "stable" and "-" in m["version"]:
    sys.exit("stable manifest with a pre-release version")
ok = True
for key in ("game", "installer"):
    a = m.get(key) or {}
    if not a.get("url"):
        if key == "game":
            sys.exit("manifest has no game package")
        continue
    if not a["url"].startswith(prefix):
        sys.exit(f"{key} url outside this repository: {a['url']}")
    data = get(a["url"])
    digest = hashlib.sha256(data).hexdigest()
    good = len(data) == a["size"] and digest == a["sha256"]
    ok &= good
    print(f"{'ok ' if good else 'BAD'} {a['name']}: {len(data)} bytes, sha256 {digest}")
sys.exit(0 if ok else 1)
