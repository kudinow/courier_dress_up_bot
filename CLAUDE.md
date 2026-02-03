# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Telegram bot that transforms user photos into Yandex.Eda courier images using AI. Users select a style (male/female), send a photo, and receive a photorealistic portrait in courier uniform.

## Commands

```bash
# Run locally
python3 -m bot.main

# Run with logging
./run.sh                    # or: python3 -m bot.main 2>&1 | tee bot.log

# Install dependencies
pip install -r requirements.txt
```

## Architecture

```
User → Telegram → aiogram Bot → OpenRouter (GPT-5.2) → kie.ai (nano-banana-edit) → User
```

**Key Flow:**
1. User selects gender style via inline keyboard
2. User sends photo
3. `openai_client` generates a courier-themed prompt using `PROMPT_SYSTEM` + `PROMPT_CRITICAL_SUFFIX`
4. `kie_client` transforms photo via kie.ai API (create task → poll status → download result)
5. Second pass adds Yandex.Eda logo to the image
6. Result sent back with regeneration options

## Key Files

- [bot/config.py](bot/config.py) - Settings via pydantic-settings, `PROMPT_SYSTEM` and `PROMPT_CRITICAL_SUFFIX` constants
- [bot/handlers/start.py](bot/handlers/start.py) - `/start` command, gender selection, regeneration callbacks
- [bot/handlers/photo.py](bot/handlers/photo.py) - Photo processing, calls to AI services
- [bot/services/openai_client.py](bot/services/openai_client.py) - OpenRouter API client for prompt generation
- [bot/services/kie_client.py](bot/services/kie_client.py) - kie.ai API client (task creation, polling, image download)
- [bot/services/user_limits.py](bot/services/user_limits.py) - User limits (3 free generations), admin bypass, data persistence

## Configuration

Environment variables in `.env` (see `.env.example`):
- `BOT_TOKEN` - Telegram bot token
- `KIE_API_KEY` / `KIE_API_URL` - kie.ai credentials
- `OPENROUTER_API_KEY` / `OPENROUTER_BASE_URL` - OpenRouter (GPT) credentials
- `DEBUG` - Enable debug logging

## Data Storage

- FSM state: In-memory (`MemoryStorage`) - resets on restart
- User data: `user_generations.json` - generation counts, last photo URL, selected gender
- Production path: `/opt/photoshoot_ai/user_generations.json`

## Server & Deployment

**Server:** `89.169.181.230` (Яндекс.Облако)
**User:** `kudinow`
**Bot location:** `/home/kudinow/bot/`
**Python:** `/home/kudinow/bot/venv/bin/python`

### SSH подключение
```bash
ssh -i ~/.ssh/id_ed25519 kudinow@89.169.181.230
```

### Управление ботом на сервере
```bash
# Проверить статус (найти PID)
ssh -i ~/.ssh/id_ed25519 kudinow@89.169.181.230 "ps aux | grep 'bot.main' | grep -v grep"

# Остановить бота (заменить PID)
ssh -i ~/.ssh/id_ed25519 kudinow@89.169.181.230 "pkill -f 'bot.main'"

# Запустить бота
ssh -i ~/.ssh/id_ed25519 kudinow@89.169.181.230 "cd /home/kudinow/bot && nohup ./venv/bin/python -m bot.main > bot.log 2>&1 &"

# Посмотреть логи
ssh -i ~/.ssh/id_ed25519 kudinow@89.169.181.230 "tail -50 /home/kudinow/bot/bot.log"
```

**Важно:** Бот запущен как обычный процесс, НЕ через systemd. Файл `photoshoot_ai.service` есть, но сервис не установлен.

See [DEPLOY.md](DEPLOY.md) for full deployment instructions.
