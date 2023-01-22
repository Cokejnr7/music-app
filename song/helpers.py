from mutagen.mp3 import MP3
import math


def get_duration(file):
    audio = MP3(file)
    duration = audio.info.length
    return format_duration(duration)


def format_duration(duration):
    min = math.floor(math.floor(duration)/60)
    sec = math.floor(duration) % 60
    if sec < 10:
        sec = f'0{sec}'
    return f'{min}:{sec}'
