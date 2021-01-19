"""
Main interface for CastController.
"""

import os
import traceback

import pychromecast


__all__ = [
    "play",
    "pause",
]


CAST = None
MC = None


def play():
    MC.play()


def pause():
    MC.pause()


def toggle():
    if MC.is_playing:
        MC.pause()
    else:
        MC.play()


def start(url, content_type):
    MC.play_media(url, content_type=content_type)


def stop():
    MC.stop()


def seek(abs=None, rel=None):
    if abs is not None:
        MC.seek(float(abs))
    elif rel is not None:
        MC.seek(round(float(rel) * MC.status.duration))


def volume(rel):
    CAST.set_volume(float(rel))


def status():
    try:
        MC.update_status()  # TODO: FIXME (unknown cause)
    except pychromecast.error.UnsupportedNamespace:
        print(traceback.format_exc())

    return {
        'duration': MC.status.duration,
        'current_time': MC.status.current_time,
        'player_state': MC.status.player_state,
        'volume_level': CAST.status.volume_level,
    }


def init():
    global CAST, MC

    chromecast_ip = os.environ.get("CHROMECAST_IP", None)

    if chromecast_ip:
        print("[ ] Using provided CHROMECAST_IP")
        cast = pychromecast.Chromecast(chromecast_ip)
    else:
        print("[ ] No CHROMECAST_IP env var provided, scanning for Chromecasts...")
        (services, browser) = pychromecast.discovery.discover_chromecasts()
        pychromecast.discovery.stop_discovery(browser)
        print(f"Found {len(services)}")

        chromecast_nickname = services[0][3]
        (chromecasts, browser) = pychromecast.get_listed_chromecasts(friendly_names=[chromecast_nickname])
        cast = chromecasts[0]

    cast.wait()
    print(cast.device)
    print(cast.status)

    mc = cast.media_controller

    CAST = cast
    MC = mc


init()
