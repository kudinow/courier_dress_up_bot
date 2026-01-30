"""Планировщик отложенной отправки CTA-сообщения с предложением стать курьером."""

import asyncio
import logging
from typing import Optional

from aiogram import Bot

from bot.keyboards.inline import get_courier_signup_keyboard

logger = logging.getLogger(__name__)

CTA_DELAY_SECONDS = 10

# user_id -> asyncio.Task
_pending_tasks: dict[int, asyncio.Task] = {}


def cancel_cta(user_id: int) -> None:
    """Отменяет запланированное CTA-сообщение для пользователя."""
    task = _pending_tasks.pop(user_id, None)
    if task and not task.done():
        task.cancel()
        logger.debug(f"CTA cancelled for user {user_id}")


def schedule_cta(user_id: int, chat_id: int, bot: Bot) -> None:
    """Планирует отправку CTA через CTA_DELAY_SECONDS."""
    cancel_cta(user_id)
    _pending_tasks[user_id] = asyncio.create_task(
        _send_cta(user_id, chat_id, bot)
    )


async def _send_cta(user_id: int, chat_id: int, bot: Bot) -> None:
    try:
        await asyncio.sleep(CTA_DELAY_SECONDS)
        await bot.send_message(
            chat_id=chat_id,
            text=(
                "А чтобы примерить на себя работу курьером — "
                "переходи по ссылке 👇"
            ),
            reply_markup=get_courier_signup_keyboard(),
        )
        logger.info(f"CTA sent to user {user_id}")
    except asyncio.CancelledError:
        pass
    except Exception:
        logger.exception(f"Failed to send CTA to user {user_id}")
    finally:
        _pending_tasks.pop(user_id, None)
