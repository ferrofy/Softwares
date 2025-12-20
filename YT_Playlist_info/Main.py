import time
from statistics import mean
from yt_dlp import YoutubeDL
import sys
import os

base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(base_dir)

from FerroFy import Entry, Exit

Entry.Main_Logo()

def Duration(seconds):
    seconds = int(seconds)
    days = seconds // 86400
    seconds %= 86400
    h = seconds // 3600
    seconds %= 3600
    m = seconds // 60
    s = seconds % 60

    parts = []
    if days:
        parts.append(f"{days} days")
    if h:
        parts.append(f"{h} hours")
    if m:
        parts.append(f"{m} min")
    parts.append(f"{s} sec")

    return " | ".join(parts)


def fetch_playlist_flat(url):
    opts = {"quiet": True, "no_warnings": True, "extract_flat": "in_playlist", "cachedir": False, "socket_timeout": 10}
    with YoutubeDL(opts) as ydl:
        info = ydl.extract_info(url, download=False)
    entries = info.get("entries") or []
    return [{"duration": e.get("duration")} for e in entries if e]

def collect_durations(entries):
    durations = []
    for e in entries:
        dur = e.get("duration")
        if dur:
            durations.append(int(dur))
    return durations

def Stats_Duration(durations):
    total = sum(durations)
    avg = mean(durations)
    return {
        "count": len(durations),
        "total": total,
        "average": int(avg),
        "shortest": min(durations),
        "longest": max(durations)
    }

URL = input("Paste Link Of Playlist ---> ")
Total_Video_Completed = int(input("How many videos You completed ---> "))

print("Fetching Playlist...")
entries = fetch_playlist_flat(URL)

if not entries:
    opts = {"quiet": True, "no_warnings": True, "cachedir": False, "socket_timeout": 10}
    with YoutubeDL(opts) as ydl:
        info = ydl.extract_info(URL, download=False)
    entries = [{"duration": e.get("duration")} for e in info.get("entries") if e]

if not entries:
    print("Invalid URL. Check URL Again...")
    sys.exit(1)

durations = collect_durations(entries)

if not durations:
    print("Does Your Playlist Have Any Video ? Or You Sure About Link ?")
    sys.exit(0)

s = Stats_Duration(durations)
total_videos = s["count"]

completed = max(0, min(Total_Video_Completed, total_videos))
completed_time = sum(durations[:completed])
remaining_durations = durations[completed:]
remaining_videos = len(remaining_durations)
remaining_time = sum(remaining_durations)

new_current_average = int(mean(remaining_durations)) if remaining_durations else 0

print("_" * 100)
print("\nPlaylist Stats")
print("_" * 100)
print(f"Total Videos ----> {total_videos}")
print(f"Total Duration ----> {Duration(s['total'])}")
print(f"Average Video Duration ----> {Duration(s['average'])}")
print(f"Shortest ----> {Duration(s['shortest'])}")
print(f"Longest ----> {Duration(s['longest'])}")

print("_" * 100)
print("\nYour Progress")
print("_" * 100)
print(f"Completed Videos ----> {completed}")
print(f"Time Watched ----> {Duration(completed_time)}")
print(f"Remaining Videos ----> {remaining_videos}")
print(f"Remaining Time ----> {Duration(remaining_time)}")
print(f"New Current Average ----> {Duration(new_current_average)}")

Exit.YT()
