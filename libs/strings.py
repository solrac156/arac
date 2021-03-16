"""
libs.strings

By default, uses 'en-us.json' file inside the 'strings' top-level folder.

If language changes, set 'libs.strings.default_locale' and run 'libs.strings.refresh()'
"""
import json


accepted_locales = ["en-us", "es-es"]
default_locale = "en-us"
cached_strings = {}


def refresh() -> None:
    global cached_strings
    with open(f"strings/{default_locale}.json") as f:
        cached_strings = json.load(f)


def gettext(name: str) -> str:
    return cached_strings[name]


def set_default_locale(locale: str) -> None:
    global default_locale
    default_locale = locale


refresh()
