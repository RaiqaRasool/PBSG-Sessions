"""Build and verify the participant-only archive. Facilitator helper; no dependencies."""

from pathlib import Path
import re
import zipfile

ROOT = Path(__file__).resolve().parents[1]
KIT = ROOT / "participant-kit"
FILES = [
    "AGENTS.md", "DESIGN-OPTIONS.md", "START-HERE.md", "OPTIONAL-REFERENCE.md",
    "SAMPLE-RESUME.md", "SETUP.md", "CLAUDE.md", "GEMINI.md",
    "references/README.md", "references/sean-halpin.md",
    "references/brittany-chiang.md", "references/cassidy-williams.md",
    "references/maggie-appleton.md", "references/nicky-case.md",
    "references/lynn-fisher.md", "references/josh-comeau.md",
    "references/ram-maheshwari.md",
]

for name in FILES:
    path = KIT / name
    assert path.is_file(), f"Missing participant file: {name}"
    for target in re.findall(r"\]\(([^)]+)\)", path.read_text()):
        if not target.startswith(("https://", "http://", "#")):
            assert (path.parent / target.split("#", 1)[0]).is_file(), (name, target)

archive = ROOT / "portfolio-starter.zip"
with zipfile.ZipFile(archive, "w", zipfile.ZIP_DEFLATED) as bundle:
    for name in sorted(FILES):
        entry = zipfile.ZipInfo(f"my-portfolio/{name}", (2026, 11, 1, 0, 0, 0))
        entry.compress_type = zipfile.ZIP_DEFLATED
        entry.external_attr = 0o100644 << 16
        bundle.writestr(entry, (KIT / name).read_bytes())

with zipfile.ZipFile(archive) as bundle:
    assert bundle.testzip() is None, "Archive integrity check failed"
    assert set(bundle.namelist()) == {f"my-portfolio/{name}" for name in FILES}
    for name in FILES:
        assert bundle.read(f"my-portfolio/{name}") == (KIT / name).read_bytes()

print(f"Verified {len(FILES)} participant files, local links, archive integrity, and source match.")
