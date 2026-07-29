#!/usr/bin/env python3
"""Find likely player bases in a Minecraft Bedrock .mcworld save.

The script is read-only. It scores saved chunks by groups of blocks commonly
found together in a long-lived base, then merges nearby interesting chunks.
"""

from __future__ import annotations

import argparse
import json
import math
import shutil
import sys
import tempfile
import threading
import webbrowser
import zipfile
from collections import Counter, deque
from dataclasses import dataclass, field
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Iterable
from urllib.parse import parse_qs, urlparse

import numpy as np


# Exact universal block base names. Amulet normally translates Bedrock names to
# the universal_minecraft namespace, so matching only the part after ':' also
# makes this tolerant of harmless namespace differences.
EXACT_WEIGHTS: dict[str, float] = {
    # Storage is the strongest general signal of a long-lived base.
    "chest": 12, "trapped_chest": 14, "barrel": 10, "ender_chest": 14,
    "shulker_box": 10,
    # Utility and progression blocks.
    "crafting_table": 6, "furnace": 7, "blast_furnace": 9, "smoker": 8,
    "anvil": 10, "chipped_anvil": 9, "damaged_anvil": 8,
    "enchanting_table": 16, "brewing_stand": 12, "grindstone": 7,
    "stonecutter": 6, "loom": 5, "cartography_table": 5,
    "smithing_table": 8, "fletching_table": 4, "composter": 3,
    "beacon": 25, "conduit": 20, "respawn_anchor": 12,
    # Living/transport/redstone evidence.
    "bed": 11, "nether_portal": 8, "lodestone": 14,
    "hopper": 9, "dispenser": 6, "dropper": 6, "observer": 6,
    "piston": 5, "sticky_piston": 7, "repeater": 6, "comparator": 8,
    "lever": 3, "target": 4, "daylight_detector": 4,
    "rail": 2, "powered_rail": 4, "detector_rail": 3, "activator_rail": 3,
    "torch": 0.22, "soul_torch": 0.25, "lantern": 1.2, "soul_lantern": 1.2,
    "bell": 3, "flower_pot": 1.5, "armor_stand": 5,
}

# Suffix matching covers coloured beds/shulker boxes and material-specific signs.
SUFFIX_WEIGHTS: tuple[tuple[str, float], ...] = (
    ("_bed", 11), ("_shulker_box", 10), ("_sign", 1.5),
    ("_hanging_sign", 2), ("_wall_sign", 1.5), ("_button", 0.5),
    ("_pressure_plate", 0.5), ("_door", 0.35), ("_trapdoor", 0.35),
)

# These are useful only in combination. A naturally generated village may have
# several, so diversity and strong-block bonuses below matter more than raw sum.
CATEGORY: dict[str, str] = {
    "chest": "storage", "trapped_chest": "storage", "barrel": "storage",
    "ender_chest": "storage", "shulker_box": "storage",
    "crafting_table": "utility", "furnace": "utility", "blast_furnace": "utility",
    "smoker": "utility", "anvil": "utility", "enchanting_table": "progression",
    "brewing_stand": "progression", "beacon": "progression", "conduit": "progression",
    "bed": "living", "nether_portal": "transport", "lodestone": "transport",
    "hopper": "redstone", "observer": "redstone", "piston": "redstone",
    "sticky_piston": "redstone", "repeater": "redstone", "comparator": "redstone",
    "rail": "transport", "powered_rail": "transport",
    "torch": "lighting", "lantern": "lighting", "soul_torch": "lighting",
    "soul_lantern": "lighting",
}


@dataclass
class ChunkEvidence:
    cx: int
    cz: int
    score: float = 0.0
    weighted_y: float = 0.0
    y_weight: float = 0.0
    blocks: Counter[str] = field(default_factory=Counter)
    categories: set[str] = field(default_factory=set)

    @property
    def y(self) -> float | None:
        return self.weighted_y / self.y_weight if self.y_weight else None


def base_name(namespaced_name: str) -> str:
    return namespaced_name.rsplit(":", 1)[-1]


def block_weight(name: str) -> float:
    if name in EXACT_WEIGHTS:
        return EXACT_WEIGHTS[name]
    for suffix, weight in SUFFIX_WEIGHTS:
        if name.endswith(suffix):
            return weight
    return 0.0


def category_for(name: str) -> str | None:
    if name in CATEGORY:
        return CATEGORY[name]
    if name.endswith("_bed"):
        return "living"
    if name.endswith("_shulker_box"):
        return "storage"
    if name.endswith(("_sign", "_hanging_sign", "_wall_sign")):
        return "decoration"
    if name.endswith(("_button", "_pressure_plate")):
        return "redstone"
    return None


def safe_extract_mcworld(source: Path, target: Path) -> Path:
    """Extract a mcworld without allowing paths to escape the temp directory."""
    with zipfile.ZipFile(source) as archive:
        root = target.resolve()
        for info in archive.infolist():
            destination = (target / info.filename).resolve()
            if destination != root and root not in destination.parents:
                raise ValueError(f"Unsafe path in archive: {info.filename}")
        archive.extractall(target)

    candidates = [target, *[p.parent for p in target.rglob("level.dat")]]
    for candidate in candidates:
        if (candidate / "level.dat").is_file() and (candidate / "db").is_dir():
            return candidate
    raise ValueError("This archive does not contain a Bedrock level.dat and db directory")


def scan_chunk(chunk, cx: int, cz: int) -> ChunkEvidence:
    evidence = ChunkEvidence(cx, cz)
    palette_cache: dict[int, tuple[str, float, str | None]] = {}

    for cy in chunk.blocks.sub_chunks:
        array = chunk.blocks.get_sub_chunk(cy)
        ids, counts = np.unique(array, return_counts=True)
        for palette_id, count_value in zip(ids.tolist(), counts.tolist()):
            palette_id = int(palette_id)
            cached = palette_cache.get(palette_id)
            if cached is None:
                name = base_name(chunk.block_palette[palette_id].namespaced_name)
                cached = (name, block_weight(name), category_for(name))
                palette_cache[palette_id] = cached
            name, weight, category = cached
            if weight <= 0:
                continue
            count = int(count_value)
            # Cap abundant cheap blocks so thousands of torches/doors cannot
            # overwhelm rare, meaningful base equipment.
            effective_count = min(count, 64 if weight < 1 else 32)
            contribution = weight * effective_count
            evidence.score += contribution
            evidence.blocks[name] += count
            if category:
                evidence.categories.add(category)

            positions = np.argwhere(array == palette_id)
            if positions.size:
                mean_y = cy * 16 + float(positions[:, 1].mean())
                evidence.weighted_y += mean_y * contribution
                evidence.y_weight += contribution

    # A real base usually mixes storage, living, utilities, transport, and/or
    # redstone. This bonus reduces single-feature village/mineshaft false hits.
    evidence.score += 9.0 * max(0, len(evidence.categories) - 1) ** 1.45
    if "storage" in evidence.categories and "utility" in evidence.categories:
        evidence.score += 22
    if "storage" in evidence.categories and "living" in evidence.categories:
        evidence.score += 16
    return evidence


def connected_components(chunks: dict[tuple[int, int], ChunkEvidence], gap: int):
    remaining = set(chunks)
    while remaining:
        start = remaining.pop()
        component = [start]
        queue = deque([start])
        while queue:
            cx, cz = queue.popleft()
            for nx in range(cx - gap, cx + gap + 1):
                for nz in range(cz - gap, cz + gap + 1):
                    point = (nx, nz)
                    if point in remaining:
                        remaining.remove(point)
                        queue.append(point)
                        component.append(point)
        yield [chunks[p] for p in component]


def summarise_cluster(component: list[ChunkEvidence]) -> dict:
    total = sum(c.score for c in component)
    # Keep weak neighbouring chunks useful without allowing a huge low-grade
    # settlement to beat a compact, equipment-rich base.
    peak = max(c.score for c in component)
    score = peak + 0.55 * (total - peak) + 10 * math.log2(len(component) + 1)
    x = sum((c.cx * 16 + 8) * c.score for c in component) / total
    z = sum((c.cz * 16 + 8) * c.score for c in component) / total
    y_items = [(c.y, c.y_weight) for c in component if c.y is not None]
    y = (sum(v * w for v, w in y_items) / sum(w for _, w in y_items)) if y_items else None
    blocks: Counter[str] = Counter()
    categories: set[str] = set()
    for c in component:
        blocks.update(c.blocks)
        categories.update(c.categories)
    return {
        "score": round(score, 1),
        "x": round(x), "y": None if y is None else round(y), "z": round(z),
        "chunk_count": len(component),
        "chunk_bounds": {
            "min_x": min(c.cx for c in component) * 16,
            "max_x": max(c.cx for c in component) * 16 + 15,
            "min_z": min(c.cz for c in component) * 16,
            "max_z": max(c.cz for c in component) * 16 + 15,
        },
        "categories": sorted(categories),
        "evidence": blocks.most_common(12),
        "chunks": [
            {"cx": c.cx, "cz": c.cz, "score": round(c.score, 1),
             "y": None if c.y is None else round(c.y)}
            for c in sorted(component, key=lambda item: item.score, reverse=True)
        ],
    }


def find_bases(world_dir: Path, dimension: str, min_chunk_score: float,
               cluster_gap: int, progress_every: int) -> tuple[list[dict], int, int, list[dict]]:
    try:
        import amulet
    except ImportError as exc:
        raise RuntimeError("amulet-core is missing; run this script with 'uv run'") from exc

    level = amulet.load_level(str(world_dir))
    interesting: dict[tuple[int, int], ChunkEvidence] = {}
    signals: list[dict] = []
    failures = 0
    scanned = 0
    try:
        coordinates = list(level.all_chunk_coords(dimension))
        total = len(coordinates)
        print(f"Scanning {total:,} saved chunks in {dimension}...", file=sys.stderr)
        for cx, cz in coordinates:
            scanned += 1
            try:
                evidence = scan_chunk(level.get_chunk(cx, cz, dimension), cx, cz)
                if evidence.score > 0:
                    signals.append({"cx": cx, "cz": cz, "score": round(evidence.score, 1)})
                if evidence.score >= min_chunk_score:
                    interesting[(cx, cz)] = evidence
            except Exception as exc:  # corrupt/unsupported chunks should not kill a scan
                failures += 1
                if failures <= 5:
                    print(f"Warning: skipped chunk ({cx}, {cz}): {exc}", file=sys.stderr)
            if progress_every and scanned % progress_every == 0:
                print(f"  {scanned:,}/{total:,}; {len(interesting):,} interesting", file=sys.stderr)
    finally:
        level.close()

    clusters = [summarise_cluster(c) for c in connected_components(interesting, cluster_gap)]
    clusters.sort(key=lambda item: item["score"], reverse=True)
    return clusters, scanned, failures, signals


class BaseFinderHandler(BaseHTTPRequestHandler):
    """Small local-only HTTP API; uploaded worlds never leave this process."""

    server_version = "MCBaseFinder/1.0"

    def log_message(self, fmt: str, *args) -> None:
        print(f"[web] {self.address_string()} - {fmt % args}", file=sys.stderr)

    def send_bytes(self, status: int, body: bytes, content_type: str) -> None:
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def send_json(self, status: int, payload: dict) -> None:
        self.send_bytes(status, json.dumps(payload, ensure_ascii=False).encode(),
                        "application/json; charset=utf-8")

    def do_GET(self) -> None:
        if urlparse(self.path).path not in ("/", "/index.html"):
            self.send_json(404, {"error": "not found"})
            return
        html_path = Path(__file__).with_name("web.html")
        try:
            self.send_bytes(200, html_path.read_bytes(), "text/html; charset=utf-8")
        except OSError as exc:
            self.send_json(500, {"error": f"cannot read web interface: {exc}"})

    def do_POST(self) -> None:
        parsed = urlparse(self.path)
        if parsed.path != "/api/scan":
            self.send_json(404, {"error": "not found"})
            return
        try:
            length = int(self.headers.get("Content-Length", "0"))
            if length <= 0:
                raise ValueError("empty upload")
            if length > 12 * 1024**3:
                raise ValueError("world is larger than the 12 GiB safety limit")
            params = parse_qs(parsed.query)
            top = max(1, min(100, int(params.get("top", ["15"])[0])))
            min_score = max(0.0, float(params.get("min_score", ["18"])[0]))
            gap = max(0, min(8, int(params.get("gap", ["1"])[0])))
            dimension = params.get("dimension", ["minecraft:overworld"])[0]
            allowed = {"minecraft:overworld", "minecraft:the_nether", "minecraft:the_end"}
            if dimension not in allowed:
                raise ValueError("invalid dimension")

            with tempfile.TemporaryDirectory(prefix="mc-base-web-") as temp_name:
                temp = Path(temp_name)
                archive_path = temp / "upload.mcworld"
                remaining = length
                with archive_path.open("wb") as output:
                    while remaining:
                        block = self.rfile.read(min(1024 * 1024, remaining))
                        if not block:
                            raise ValueError("upload ended before Content-Length")
                        output.write(block)
                        remaining -= len(block)
                if not zipfile.is_zipfile(archive_path):
                    raise ValueError("selected file is not a ZIP-based .mcworld archive")
                world_dir = safe_extract_mcworld(archive_path, temp / "world")
                results, scanned, failures, signals = find_bases(
                    world_dir, dimension, min_score, gap, 500)
                self.send_json(200, {
                    "chunks_scanned": scanned, "chunks_failed": failures,
                    "dimension": dimension, "signals": signals,
                    "candidates": results[:top],
                })
        except (ValueError, RuntimeError, zipfile.BadZipFile) as exc:
            self.send_json(400, {"error": str(exc)})
        except Exception as exc:
            print(f"Web scan failed: {exc}", file=sys.stderr)
            self.send_json(500, {"error": f"scan failed: {exc}"})


def serve(host: str, port: int, open_browser: bool) -> int:
    html_path = Path(__file__).with_name("web.html")
    if not html_path.is_file():
        print(f"Error: missing web interface: {html_path}", file=sys.stderr)
        return 1
    server = ThreadingHTTPServer((host, port), BaseFinderHandler)
    url_host = "127.0.0.1" if host in ("0.0.0.0", "::") else host
    url = f"http://{url_host}:{server.server_port}/"
    print(f"Minecraft Base Finder: {url}", file=sys.stderr)
    print("Press Ctrl-C to stop. Files are processed locally.", file=sys.stderr)
    if open_browser:
        threading.Timer(0.35, lambda: webbrowser.open(url)).start()
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.", file=sys.stderr)
    finally:
        server.server_close()
    return 0


def parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description="Rank likely main-base locations in a Minecraft Bedrock .mcworld save.")
    p.add_argument("world", type=Path, nargs="?",
                   help=".mcworld file or extracted Bedrock world directory")
    p.add_argument("--dimension", default="minecraft:overworld",
                   choices=("minecraft:overworld", "minecraft:the_nether", "minecraft:the_end"))
    p.add_argument("--top", type=int, default=15, help="number of candidates to show (default: 15)")
    p.add_argument("--min-chunk-score", type=float, default=18,
                   help="ignore chunks below this evidence score (default: 18)")
    p.add_argument("--cluster-gap", type=int, default=1,
                   help="merge candidates this many chunks apart (default: 1)")
    p.add_argument("--progress-every", type=int, default=500,
                   help="progress interval in chunks; 0 disables it (default: 500)")
    p.add_argument("--json", action="store_true", help="print machine-readable JSON")
    p.add_argument("--serve", action="store_true", help="start the local web interface")
    p.add_argument("--host", default="127.0.0.1", help="web bind address (default: 127.0.0.1)")
    p.add_argument("--port", type=int, default=8765, help="web port (default: 8765)")
    p.add_argument("--no-browser", action="store_true", help="do not open a browser automatically")
    return p


def main() -> int:
    args = parser().parse_args()
    if args.serve:
        if not 0 <= args.port <= 65535:
            print("Error: --port must be between 0 and 65535", file=sys.stderr)
            return 2
        return serve(args.host, args.port, not args.no_browser)
    if args.world is None:
        print("Error: provide a .mcworld file or use --serve", file=sys.stderr)
        return 2
    source = args.world.expanduser().resolve()
    if not source.exists():
        print(f"Error: world does not exist: {source}", file=sys.stderr)
        return 2
    if args.top < 1 or args.cluster_gap < 0 or args.min_chunk_score < 0:
        print("Error: --top must be positive; score and gap cannot be negative", file=sys.stderr)
        return 2

    temp_dir: Path | None = None
    try:
        if source.is_file():
            if not zipfile.is_zipfile(source):
                raise ValueError("input file is not a ZIP-based .mcworld archive")
            temp_dir = Path(tempfile.mkdtemp(prefix="mc-base-finder-"))
            world_dir = safe_extract_mcworld(source, temp_dir)
        else:
            world_dir = source

        results, scanned, failures, signals = find_bases(
            world_dir, args.dimension, args.min_chunk_score,
            args.cluster_gap, args.progress_every)
        results = results[:args.top]

        if args.json:
            print(json.dumps({"world": str(source), "dimension": args.dimension,
                              "chunks_scanned": scanned, "chunks_failed": failures,
                              "candidates": results}, ensure_ascii=False, indent=2))
        else:
            print(f"\nLikely bases ({len(results)} shown; {scanned:,} chunks scanned):")
            if not results:
                print("No candidates found. Try --min-chunk-score 8")
            for rank, item in enumerate(results, 1):
                y = "?" if item["y"] is None else str(item["y"])
                evidence = ", ".join(f"{name}×{count}" for name, count in item["evidence"][:8])
                bounds = item["chunk_bounds"]
                print(f"\n{rank:>2}. score {item['score']:>7.1f}  near X={item['x']}, Y={y}, Z={item['z']}")
                print(f"    area X {bounds['min_x']}..{bounds['max_x']}, "
                      f"Z {bounds['min_z']}..{bounds['max_z']} ({item['chunk_count']} chunks)")
                print(f"    evidence: {evidence or 'none'}")
            if failures:
                print(f"\nWarning: {failures} chunks could not be decoded.", file=sys.stderr)
        return 0
    except (ValueError, RuntimeError, zipfile.BadZipFile) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    finally:
        if temp_dir is not None:
            shutil.rmtree(temp_dir, ignore_errors=True)


if __name__ == "__main__":
    raise SystemExit(main())
