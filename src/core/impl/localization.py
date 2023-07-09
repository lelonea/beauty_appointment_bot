import glob
import json

from core.api.base_localization import BaseLocalization
from settings import LOCALE_PATHS, DEFAULT_LANGUAGE


class Localization(BaseLocalization):
    __instance = None


    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
        return cls.__instance


    def __init__(self):
        if hasattr(self, "_locales"):
            return

        self._locales = self._load_locales()

    @staticmethod
    def _load_locales() -> dict[str, dict[str, str]]:
        languages = glob.glob(LOCALE_PATHS + "/*.json")
        locales = {}
        for language in languages:
            with open(language, "r") as f:
                lang_name = language.split("/")[-1].split(".")[0]
                locales[lang_name] = json.load(f)
        return locales

    def get(self, key: str, language: str = DEFAULT_LANGUAGE) -> str:
        return self._locales.get(language, {}).get(key, key)
