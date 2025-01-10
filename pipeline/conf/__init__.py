import importlib
import os
from typing import Any

from pipeline.conf.schemas import SettingsSchema

ENVIRONMENT_VARIABLE = "SETTINGS_MODULE"


class Settings:
    def __init__(self, settings_module: str):
        self.config = SettingsSchema()
        self.load_settings(settings_module)

    def load_settings(self, settings_module: str) -> None:
        mod = importlib.import_module(settings_module)

        for setting in dir(mod):
            if setting.isupper():
                setting_value: Any = getattr(mod, setting)
                setattr(self, setting, setting_value)

    def __getattr__(self, name: str) -> Any:
        return getattr(self.config, name)

    def to_dict(self) -> dict[str, Any]:
        return self.config.model_dump()


settings_module = os.environ.get(ENVIRONMENT_VARIABLE, "config.settings.default")
settings = Settings(settings_module)
