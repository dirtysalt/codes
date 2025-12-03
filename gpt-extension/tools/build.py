#!/usr/bin/env python3
import json
import os
import shutil
import sys
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
import zlib
import struct

ROOT = Path(__file__).resolve().parents[1]
SRC_FILES = [
    'manifest.json',
    'background.js',
    'sidepanel.html',
    'sidepanel.js',
    'rules.json',
    'options.html',
    'options.js',
    'README.md',
    'AGENTS.md',
]
CONFIG_PATH = ROOT / 'build' / 'hosts.json'
BRAND_PATH = ROOT / 'build' / 'branding.json'
DIST_DIR = ROOT / 'dist'
ASSETS_DIR = ROOT / 'assets'

def read_json(p):
    with open(p, 'r', encoding='utf-8') as f:
        return json.load(f)

def write_json(p, data):
    with open(p, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write('\n')

def ensure_dir(p: Path):
    p.mkdir(parents=True, exist_ok=True)

def sanitize_host(host: str) -> str:
    host = host.strip()
    if host.startswith('http://') or host.startswith('https://'):
        try:
            from urllib.parse import urlparse
            parsed = urlparse(host)
            host = parsed.netloc
        except Exception:
            pass
    return host.lstrip('.').rstrip('/')

def parse_hex_rgba(s, default):
    try:
        s = s.strip().lstrip('#')
        if len(s) == 6:
            r = int(s[0:2], 16)
            g = int(s[2:4], 16)
            b = int(s[4:6], 16)
            a = 255
        elif len(s) == 8:
            r = int(s[0:2], 16)
            g = int(s[2:4], 16)
            b = int(s[4:6], 16)
            a = int(s[6:8], 16)
        else:
            return default
        return (r, g, b, a)
    except Exception:
        return default

def main():
    manifest = read_json(ROOT / 'manifest.json')
    rules = read_json(ROOT / 'rules.json')
    version = manifest.get('version', '0.0.0')

    # Load build-time hosts
    extra_hosts = []
    if CONFIG_PATH.exists():
        cfg = read_json(CONFIG_PATH)
        extra_hosts = [sanitize_host(h) for h in cfg.get('extra_hosts', []) if str(h).strip()]

    # Prepare derived artifacts
    out_dir = DIST_DIR / f"ai-side-panel-{version}"
    if out_dir.exists():
        shutil.rmtree(out_dir)
    ensure_dir(out_dir)

    # Merge host_permissions
    hp = set(manifest.get('host_permissions', []))
    for h in extra_hosts:
        hp.add(f"*://{h}/*")
    manifest['host_permissions'] = sorted(hp)

    # Extend DNR rules for extra hosts, starting at a high ID range
    next_id = max([r.get('id', 0) for r in rules] + [0]) + 1
    for h in extra_hosts:
        rules.append({
            'id': next_id,
            'priority': 1,
            'action': {
                'type': 'modifyHeaders',
                'responseHeaders': [
                    { 'header': 'X-Frame-Options', 'operation': 'remove' },
                    { 'header': 'Content-Security-Policy', 'operation': 'remove' }
                ]
            },
            'condition': {
                'urlFilter': f"||{h}",
                'resourceTypes': ['sub_frame']
            }
        })
        next_id += 1

    # Write files
    for rel in SRC_FILES:
        src = ROOT / rel
        if src.exists():
            shutil.copy2(src, out_dir / rel)

    # Generate friendly "AI buddy" icon PNGs (robot face)
    icon_sizes = [16, 32, 48, 128]
    ensure_dir(ASSETS_DIR)

    def write_chunk(f, chunk_type: bytes, data: bytes):
        f.write(struct.pack('>I', len(data)))
        f.write(chunk_type)
        f.write(data)
        crc = zlib.crc32(chunk_type)
        crc = zlib.crc32(data, crc) & 0xffffffff
        f.write(struct.pack('>I', crc))

    def rgba(r, g, b, a=255):
        return (r & 255, g & 255, b & 255, a & 255)

    def clamp(v, lo, hi):
        return lo if v < lo else hi if v > hi else v

    # Branding colors (overridable by build/branding.json)
    branding_defaults = {
        'bg': (36, 47, 72, 255),
        'head_border': (92, 107, 192, 255),
        'head_fill': (234, 242, 255, 255),
        'eye': (30, 41, 59, 255),
        'mouth': (92, 107, 192, 255),
        'antenna': (92, 107, 192, 255),
    }
    if BRAND_PATH.exists():
        try:
            brand_cfg = read_json(BRAND_PATH)
            for k, v in list(branding_defaults.items()):
                if k in brand_cfg and isinstance(brand_cfg[k], str):
                    branding_defaults[k] = parse_hex_rgba(brand_cfg[k], v)
        except Exception:
            pass

    def render_buddy(w, h, brand=branding_defaults):
        # Colors
        bg = brand['bg']
        head_border = brand['head_border']
        head_fill = brand['head_fill']
        eye = brand['eye']
        mouth = brand['mouth']
        antenna = brand['antenna']

        buf = bytearray(w * h * 4)

        def put_px(x, y, c):
            if 0 <= x < w and 0 <= y < h:
                i = (y * w + x) * 4
                buf[i:i+4] = bytes(c)

        # Fill background
        for y in range(h):
            for x in range(w):
                put_px(x, y, bg)

        cx, cy = (w - 1) / 2.0, (h - 1) / 2.0
        r_outer = 0.40 * w
        r_inner = r_outer - max(2.0, w / 24.0)

        def draw_disc(cx, cy, r, color):
            r2 = r * r
            x0 = int(clamp(cx - r - 1, 0, w - 1))
            x1 = int(clamp(cx + r + 1, 0, w - 1))
            y0 = int(clamp(cy - r - 1, 0, h - 1))
            y1 = int(clamp(cy + r + 1, 0, h - 1))
            for yy in range(y0, y1 + 1):
                for xx in range(x0, x1 + 1):
                    dx = xx + 0.5 - cx
                    dy = yy + 0.5 - cy
                    if dx*dx + dy*dy <= r2:
                        put_px(xx, yy, color)

        # Antenna
        stem_h = h * 0.16
        stem_w = max(1, w // 16)
        stem_x0 = int(cx - stem_w / 2)
        stem_x1 = int(cx + stem_w / 2)
        stem_y0 = int(cy - r_outer - stem_h)
        stem_y1 = int(cy - r_outer)
        for yy in range(stem_y0, stem_y1):
            for xx in range(stem_x0, stem_x1 + 1):
                put_px(xx, yy, antenna)
        draw_disc(cx, stem_y0 - stem_w, stem_w * 0.9, antenna)

        # Head (border then fill)
        draw_disc(cx, cy, r_outer, head_border)
        draw_disc(cx, cy, r_inner, head_fill)

        # Eyes
        eye_r = max(1.0, w / 16.0)
        eye_dx = w * 0.16
        eye_dy = -h * 0.04
        draw_disc(cx - eye_dx, cy + eye_dy, eye_r, eye)
        draw_disc(cx + eye_dx, cy + eye_dy, eye_r, eye)

        # Mouth (slight smile using sampled discs)
        t = max(1.0, w / 24.0)
        rm = w * 0.22
        my = cy + h * 0.10
        import math
        for a in [i * (math.pi / 180.0) for i in range(-36, 37, 2)]:
            x = cx + rm * math.cos(a)
            y = my + rm * math.sin(a) * 0.6
            draw_disc(x, y, t, mouth)

        return bytes(buf)

    def save_png(path: Path, w: int, h: int, raw_rgba: bytes):
        # Minimal PNG writer for RGBA buffer
        raw = bytearray()
        stride = w * 4
        for y in range(h):
            row = raw_rgba[y*stride:(y+1)*stride]
            raw.append(0)  # filter type 0
            raw.extend(row)
        compressed = zlib.compress(bytes(raw), level=9)
        with open(path, 'wb') as f:
            f.write(b"\x89PNG\r\n\x1a\n")
            ihdr = struct.pack('>IIBBBBB', w, h, 8, 6, 0, 0, 0)
            write_chunk(f, b'IHDR', ihdr)
            write_chunk(f, b'IDAT', compressed)
            write_chunk(f, b'IEND', b'')

    built_icons = {}
    for sz in icon_sizes:
        icon_path = ASSETS_DIR / f'icon-{sz}.png'
        rgba_buf = render_buddy(sz, sz)
        save_png(icon_path, sz, sz, rgba_buf)
        built_icons[str(sz)] = f'assets/icon-{sz}.png'

    # Copy assets to dist
    ensure_dir(out_dir / 'assets')
    for sz in icon_sizes:
        shutil.copy2(ASSETS_DIR / f'icon-{sz}.png', out_dir / 'assets' / f'icon-{sz}.png')

    # Add icons in packaged manifest only (avoid breaking local root if assets absent)
    manifest['icons'] = built_icons
    manifest.setdefault('action', {})['default_icon'] = built_icons

    write_json(out_dir / 'manifest.json', manifest)
    write_json(out_dir / 'rules.json', rules)

    # Create zip
    ensure_dir(DIST_DIR)
    zip_path = DIST_DIR / f"ai-side-panel-{version}.zip"
    if zip_path.exists():
        zip_path.unlink()
    with ZipFile(zip_path, 'w', ZIP_DEFLATED) as z:
        for root, _, files in os.walk(out_dir):
            for f in files:
                p = Path(root) / f
                z.write(p, p.relative_to(DIST_DIR))

    print(f"Built: {out_dir}")
    print(f"Packaged: {zip_path}")

if __name__ == '__main__':
    sys.exit(main())
