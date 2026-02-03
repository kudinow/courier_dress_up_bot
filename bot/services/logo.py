import logging
from typing import Optional

logger = logging.getLogger(__name__)

# URL логотипа в Yandex Cloud Storage
LOGO_URL = "https://storage.yandexcloud.net/courier-dress-up-bot/logo_yandex_eda_offline.png"


def get_logo_url() -> Optional[str]:
    """Возвращает URL логотипа."""
    return LOGO_URL
