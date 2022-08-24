from __future__ import annotations

from django.conf import settings
from rest_framework.settings import APISettings

DEFAULTS = {
    'BACKEND': {
        'LOCATION': 'redis://localhost/'
    },
    'NAMESPACE': 'kobo-system-account',
    'TOKEN_TTL': 60,
    'TOKEN_TTL_EXPIRY_THRESHOLD': 5,
    'TOKEN_LENGTH': 50,
    'ON_BEHALF_HEADER': 'Kobo-System-Account-On-Behalf',
}


class SystemAccountSettings(APISettings):

    @property
    def user_settings(self) -> dict[str, Any]:
        if not hasattr(self, '_user_settings'):
            self._user_settings = getattr(settings, 'SYSTEM_ACCOUNT', {})
        return self._user_settings

    def __getitem__(self, attr: str) -> Any:
        return self.__getattr__(attr)


system_account_settings = SystemAccountSettings(
    user_settings=None, defaults=DEFAULTS, import_strings=None
)
