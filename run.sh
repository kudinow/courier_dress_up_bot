#!/bin/bash

# Скрипт для запуска бота с логированием

echo "🚀 Starting Yandex.Eda Courier Bot..."
echo "📝 Logs will be saved to bot.log"
echo ""

# Запуск бота с выводом в консоль и файл
python3 -m bot.main 2>&1 | tee bot.log
