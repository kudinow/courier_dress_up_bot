from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

COURIER_SIGNUP_URL = (
    "https://eda.yandex.ru/partner/perf/"
    "?utm_medium=cpc&utm_source=tg-hr&utm_campaign=courier_dressup_bot"
)


def get_courier_signup_keyboard() -> InlineKeyboardMarkup:
    """Клавиатура с кнопкой регистрации курьером"""
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(
                text="🚴 Стать курьером",
                url=COURIER_SIGNUP_URL,
            ),
        ],
    ])


def get_gender_keyboard() -> InlineKeyboardMarkup:
    """Клавиатура выбора пола"""
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="👨 Мужской", callback_data="gender_male"),
            InlineKeyboardButton(text="👩 Женский", callback_data="gender_female"),
        ],
    ])


def get_restart_keyboard(has_last_photo: bool = False) -> InlineKeyboardMarkup:
    """Клавиатура для повторной генерации"""
    buttons = []

    if has_last_photo:
        buttons.append([
            InlineKeyboardButton(
                text="🔄 Сгенерировать заново",
                callback_data="regenerate"
            ),
        ])

    buttons.append([
        InlineKeyboardButton(
            text="✨ Попробовать другое фото",
            callback_data="restart"
        ),
    ])

    return InlineKeyboardMarkup(inline_keyboard=buttons)
