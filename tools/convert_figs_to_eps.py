from pathlib import Path
from PIL import Image

# Convert the existing figure JPGs to EPS without changing their visual content.
# This is a format conversion: the raster image is embedded in an EPS container.
# It does not recreate the plots as native vector graphics.

ROOT = Path(__file__).resolve().parents[1]
FIG_DIR = ROOT / "figs"

jpg_files = sorted(FIG_DIR.glob("*.jpg"))
if not jpg_files:
    raise SystemExit(f"No JPG figures found in {FIG_DIR}")

for src in jpg_files:
    dst = src.with_suffix(".eps")
    with Image.open(src) as im:
        # EPS export expects RGB/CMYK; preserve pixels while normalizing mode.
        if im.mode not in ("RGB", "CMYK"):
            im = im.convert("RGB")
        im.save(dst, format="EPS")
    print(f"{src.name} -> {dst.name}")

print(f"Converted {len(jpg_files)} JPG figure(s) in {FIG_DIR}")
