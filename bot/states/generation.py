from aiogram.fsm.state import State, StatesGroup


class GenerationStates(StatesGroup):
    """Состояния для процесса генерации фото курьера"""

    choosing_gender = State()         # Выбираем пол для промпта
    awaiting_photo = State()          # Ждём фото от пользователя
    processing = State()              # Обрабатываем через API
