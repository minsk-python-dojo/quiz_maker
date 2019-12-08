import json
from dataclasses import dataclass
from exceptions import SettingsAttributesError


@dataclass
class AppSettings:
    attempts_per_session: int
    attempts_per_question: int

    @classmethod
    def from_file(cls, settings_path: str):
        with open(settings_path) as settings_file:
            settings: dict = json.load(settings_file)
        attempts_per_session = settings.get('attempts_per_session')
        attempts_per_question = settings.get('attempts_per_question')
        if not all((attempts_per_session, attempts_per_question)):
            raise SettingsAttributesError(
                'Missing "attempts_per_session" or "attempts_per_question" attributes in settings.json'
            )
        app_settings = cls(attempts_per_session, attempts_per_question)
        return app_settings
