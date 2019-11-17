"""Supported platforms."""
import re
from abc import ABC
from typing import Pattern, Union

#: Supported platforms registry
PLATFORMS = {}


class PlatformABC(ABC):
    """Platform data ABC."""

    # Platform's Odesli name
    key: str
    # RegEx to find platform's URL in a message text
    url_re: Union[str, Pattern]
    # Human readable name which will appear in a bot's message
    name: str
    # Order of platform's link in a bot's message
    order: int

    def __init_subclass__(cls, **kwargs):
        """Compile regex and add platform to `PLATFORM` registry."""
        super().__init_subclass__(**kwargs)
        cls.url_re = re.compile(cls.url_re)
        PLATFORMS[cls.key] = cls()


class DeezerPlatform(PlatformABC):
    """Deezer platform."""

    key = 'deezer'
    url_re = r'https?://([a-zA-Z\d-]+\.)*deezer\.com/[^\s.,]*'
    name = 'Deezer'
    order = 0


class GoogleMusicPlatform(PlatformABC):
    """Google Music platform."""

    key = 'google'
    url_re = r'https?://([a-zA-Z\d-]+\.)*play\.google\.com/music/[^\s.,]*'
    name = 'Google Music'
    order = 1


class SoundCloudPlatform(PlatformABC):
    """SoundCloud platform."""

    key = 'soundcloud'
    url_re = r'https?://([a-zA-Z\d-]+\.)*soundcloud\.com/[^\s.,]*'
    name = 'SoundCloud'
    order = 2


class YandexMusicPlatform(PlatformABC):
    """Yandex Music platform."""

    key = 'yandex'
    url_re = r'https?://([a-zA-Z\d-]+\.)*music\.yandex\.(com|ru)/[^\s.,]*'
    name = 'Yandex Music'
    order = 3


class SpotifyPlatform(PlatformABC):
    """Spotify platform."""

    key = 'spotify'
    url_re = r'https?://([a-zA-Z\d-]+\.)*spotify\.com/[^\s.,]*'
    name = 'Spotify'
    order = 4


class YoutubeMusicPlatform(PlatformABC):
    """Youtube Music platform."""

    key = 'youtubeMusic'
    url_re = r'https?://([a-zA-Z\d-]+\.)*music\.youtube\.com/[^\s.,]*'
    name = 'Youtube Music'
    order = 5