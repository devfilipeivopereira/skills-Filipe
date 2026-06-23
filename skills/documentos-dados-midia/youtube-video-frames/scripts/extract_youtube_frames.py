#!/usr/bin/env python3
"""Download a YouTube video and extract high-quality frames into a local folder."""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Any


def sanitize_slug(value: str, max_len: int = 80) -> str:
    cleaned = re.sub(r"[^\w\s-]", "", value, flags=re.UNICODE)
    cleaned = re.sub(r"\s+", "-", cleaned.strip())
    cleaned = re.sub(r"-{2,}", "-", cleaned).strip("-")
    if not cleaned:
        return "video"
    return cleaned[:max_len].strip("-") or "video"


def parse_timecode_to_seconds(raw: str | None) -> float | None:
    if raw is None:
        return None

    text = raw.strip()
    if not text:
        return None

    if re.fullmatch(r"\d+(\.\d+)?", text):
        return float(text)

    parts = text.split(":")
    if len(parts) > 3:
        raise ValueError(f"Invalid time format: {raw}")

    try:
        nums = [float(part) for part in parts]
    except ValueError as exc:
        raise ValueError(f"Invalid time format: {raw}") from exc

    while len(nums) < 3:
        nums.insert(0, 0.0)

    hours, minutes, seconds = nums
    if minutes >= 60 or seconds >= 60:
        raise ValueError(f"Invalid time format: {raw}")

    return hours * 3600 + minutes * 60 + seconds


def resolve_ffmpeg(ffmpeg_bin: str | None) -> str:
    if ffmpeg_bin:
        if Path(ffmpeg_bin).is_file():
            return str(Path(ffmpeg_bin).resolve())
        found = shutil.which(ffmpeg_bin)
        if found:
            return found
        raise RuntimeError(f"ffmpeg not found at: {ffmpeg_bin}")

    found = shutil.which("ffmpeg")
    if found:
        return found

    try:
        from imageio_ffmpeg import get_ffmpeg_exe  # type: ignore

        ffmpeg_from_pkg = get_ffmpeg_exe()
        if ffmpeg_from_pkg and Path(ffmpeg_from_pkg).exists():
            return ffmpeg_from_pkg
    except Exception:
        pass

    raise RuntimeError(
        "ffmpeg not found. Install ffmpeg in PATH or install imageio-ffmpeg: "
        "python -m pip install imageio-ffmpeg"
    )


def load_yt_dlp() -> Any:
    try:
        from yt_dlp import YoutubeDL  # type: ignore
    except Exception as exc:
        raise RuntimeError(
            "yt-dlp is not installed. Run: python -m pip install yt-dlp"
        ) from exc

    return YoutubeDL


def get_video_info(youtube_dl_cls: Any, url: str) -> dict[str, Any]:
    opts = {
        "quiet": True,
        "no_warnings": True,
        "noplaylist": True,
        "skip_download": True,
    }
    with youtube_dl_cls(opts) as ydl:
        info = ydl.extract_info(url, download=False)

    if isinstance(info, dict) and info.get("entries"):
        entries = [entry for entry in info.get("entries", []) if entry]
        if not entries:
            raise RuntimeError("Could not resolve a valid video from the provided URL")
        info = entries[0]

    if not isinstance(info, dict):
        raise RuntimeError("Could not read video metadata from URL")

    return info


def download_video(
    youtube_dl_cls: Any,
    url: str,
    download_dir: Path,
    ffmpeg_path: str,
    max_height: int | None = None,
) -> tuple[dict[str, Any], Path]:
    download_dir.mkdir(parents=True, exist_ok=True)

    format_selector = "bv*+ba/b"
    if max_height is not None:
        format_selector = (
            f"bv*[height<={max_height}]+ba/"
            f"b[height<={max_height}]/"
            "bv*+ba/b"
        )

    ydl_opts = {
        "noplaylist": True,
        "format": format_selector,
        "merge_output_format": "mp4",
        "outtmpl": str(download_dir / "%(id)s.%(ext)s"),
        "ffmpeg_location": ffmpeg_path,
        "retries": 8,
        "fragment_retries": 8,
        "concurrent_fragment_downloads": 4,
        "quiet": False,
        "no_warnings": True,
        "restrictfilenames": True,
    }

    with youtube_dl_cls(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)

    if isinstance(info, dict) and info.get("entries"):
        entries = [entry for entry in info.get("entries", []) if entry]
        if entries:
            info = entries[0]

    if not isinstance(info, dict):
        raise RuntimeError("Download finished but metadata payload is invalid")

    candidate_paths: list[Path] = []

    for key in ("_filename", "filepath"):
        value = info.get(key)
        if isinstance(value, str):
            candidate_paths.append(Path(value))

    for item in info.get("requested_downloads", []) or []:
        if isinstance(item, dict):
            path_value = item.get("filepath")
            if isinstance(path_value, str):
                candidate_paths.append(Path(path_value))

    for path in candidate_paths:
        resolved = path.resolve() if path.exists() else (download_dir / path.name)
        if resolved.exists() and resolved.is_file():
            return info, resolved

    allowed_exts = {".mp4", ".mkv", ".webm", ".mov", ".m4v"}
    downloaded_files = [
        p for p in download_dir.glob("*") if p.is_file() and p.suffix.lower() in allowed_exts
    ]
    if not downloaded_files:
        raise RuntimeError("Download finished but video file was not found")

    downloaded_files.sort(key=lambda p: p.stat().st_mtime, reverse=True)
    return info, downloaded_files[0]


def calculate_fps(
    fps: float | None,
    target_frames: int | None,
    duration_seconds: float | None,
) -> float:
    if fps is not None:
        if fps <= 0:
            raise ValueError("--fps must be greater than zero")
        return fps

    if target_frames is not None:
        if target_frames <= 0:
            raise ValueError("--target-frames must be greater than zero")
        if duration_seconds and duration_seconds > 0:
            return max(target_frames / duration_seconds, 0.01)

    return 1.0


def compute_clip_duration(
    source_duration: float | None,
    start_seconds: float | None,
    end_seconds: float | None,
) -> float | None:
    if start_seconds is not None and start_seconds < 0:
        raise ValueError("--start must be >= 0")

    if end_seconds is not None and end_seconds <= 0:
        raise ValueError("--end must be > 0")

    if start_seconds is not None and end_seconds is not None and end_seconds <= start_seconds:
        raise ValueError("--end must be greater than --start")

    if source_duration is None:
        if start_seconds is not None and end_seconds is not None:
            return end_seconds - start_seconds
        return None

    start = start_seconds or 0.0
    end = end_seconds if end_seconds is not None else source_duration
    end = min(end, source_duration)
    if end <= start:
        raise ValueError("The selected clip window has zero duration")
    return end - start


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Download a YouTube video and extract high-quality frames "
            "to a local folder."
        )
    )
    parser.add_argument("url", help="YouTube video URL")
    parser.add_argument(
        "--output-root",
        default=".",
        help="Base output directory (default: current directory)",
    )
    parser.add_argument(
        "--folder-name",
        default=None,
        help="Custom output folder name for this extraction",
    )
    parser.add_argument(
        "--fps",
        type=float,
        default=None,
        help="Frames per second to extract (overrides --target-frames)",
    )
    parser.add_argument(
        "--target-frames",
        type=int,
        default=500,
        help=(
            "Approximate total number of frames to extract when duration is known "
            "(default: 500). Ignored when --fps is provided."
        ),
    )
    parser.add_argument(
        "--max-frames",
        type=int,
        default=None,
        help="Hard limit for number of extracted frames",
    )
    parser.add_argument(
        "--image-format",
        choices=["jpg", "png"],
        default="jpg",
        help="Output image format (default: jpg)",
    )
    parser.add_argument(
        "--jpeg-quality",
        type=int,
        default=2,
        help="JPEG quality for ffmpeg (1 best - 31 worst, default: 2)",
    )
    parser.add_argument(
        "--max-height",
        type=int,
        default=None,
        help="Prefer video streams up to this vertical resolution (for example 1080)",
    )
    parser.add_argument(
        "--filename-prefix",
        default="frame",
        help="Prefix for output frame files (default: frame)",
    )
    parser.add_argument(
        "--start",
        default=None,
        help="Start timestamp (seconds or HH:MM:SS)",
    )
    parser.add_argument(
        "--end",
        default=None,
        help="End timestamp (seconds or HH:MM:SS)",
    )
    parser.add_argument(
        "--ffmpeg-bin",
        default=None,
        help="Path to ffmpeg binary (optional)",
    )
    parser.add_argument(
        "--keep-video",
        action="store_true",
        help="Keep the downloaded video file",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Overwrite output folder if it already exists",
    )
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    if args.max_frames is not None and args.max_frames <= 0:
        parser.error("--max-frames must be greater than zero")

    if args.jpeg_quality < 1 or args.jpeg_quality > 31:
        parser.error("--jpeg-quality must be between 1 and 31")

    if args.max_height is not None and args.max_height <= 0:
        parser.error("--max-height must be greater than zero")

    try:
        start_seconds = parse_timecode_to_seconds(args.start)
        end_seconds = parse_timecode_to_seconds(args.end)

        ffmpeg_path = resolve_ffmpeg(args.ffmpeg_bin)
        youtube_dl_cls = load_yt_dlp()

        info = get_video_info(youtube_dl_cls, args.url)
        video_id = str(info.get("id") or "video")
        title = str(info.get("title") or "video")

        output_root = Path(args.output_root).resolve()
        output_root.mkdir(parents=True, exist_ok=True)

        folder_name = args.folder_name or f"{sanitize_slug(title)}-{sanitize_slug(video_id, 24)}"
        job_dir = output_root / folder_name
        video_dir = job_dir / "_video"
        frames_dir = job_dir / "frames"

        if job_dir.exists():
            if not args.overwrite:
                raise RuntimeError(
                    f"Output folder already exists: {job_dir}. "
                    "Use --overwrite or choose --folder-name."
                )
            shutil.rmtree(job_dir)

        frames_dir.mkdir(parents=True, exist_ok=True)
        video_dir.mkdir(parents=True, exist_ok=True)

        print(f"Video: {title}")
        print(f"Output folder: {job_dir}")

        downloaded_info, video_path = download_video(
            youtube_dl_cls,
            args.url,
            video_dir,
            ffmpeg_path,
            args.max_height,
        )

        source_duration = downloaded_info.get("duration") or info.get("duration")
        duration_seconds = float(source_duration) if source_duration else None
        clip_duration = compute_clip_duration(duration_seconds, start_seconds, end_seconds)
        fps = calculate_fps(args.fps, args.target_frames, clip_duration or duration_seconds)

        if args.fps is None and (clip_duration or duration_seconds) is None:
            print(
                "Warning: video duration is unknown; falling back to 1 fps. "
                "Use --fps for explicit control.",
                file=sys.stderr,
            )

        output_pattern = frames_dir / f"{args.filename_prefix}_%06d.{args.image_format}"

        ffmpeg_cmd: list[str] = [
            ffmpeg_path,
            "-hide_banner",
            "-loglevel",
            "error",
            "-stats",
            "-y",
        ]

        if start_seconds is not None:
            ffmpeg_cmd.extend(["-ss", f"{start_seconds:.6f}"])

        ffmpeg_cmd.extend(["-i", str(video_path)])

        if clip_duration is not None:
            ffmpeg_cmd.extend(["-t", f"{clip_duration:.6f}"])

        ffmpeg_cmd.extend(["-vf", f"fps={fps:.8f}"])

        if args.image_format == "jpg":
            ffmpeg_cmd.extend(["-q:v", str(args.jpeg_quality)])

        if args.max_frames is not None:
            ffmpeg_cmd.extend(["-frames:v", str(args.max_frames)])

        ffmpeg_cmd.append(str(output_pattern))

        subprocess.run(ffmpeg_cmd, check=True)

        generated = sorted(frames_dir.glob(f"{args.filename_prefix}_*.{args.image_format}"))
        frame_count = len(generated)
        if frame_count == 0:
            raise RuntimeError("Frame extraction finished but no images were created")

        if not args.keep_video and video_path.exists():
            video_path.unlink(missing_ok=True)

        extracted_rate = fps
        print("")
        print("Done")
        print(f"Frames created: {frame_count}")
        print(f"Extraction fps used: {extracted_rate:.4f}")
        print(f"Frames folder: {frames_dir}")
        if args.keep_video:
            print(f"Video kept at: {video_path}")

        return 0

    except subprocess.CalledProcessError as exc:
        print(f"ffmpeg failed with exit code {exc.returncode}", file=sys.stderr)
        return 1
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
