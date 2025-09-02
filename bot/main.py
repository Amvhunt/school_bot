import logging
from aiogram import Bot, Dispatcher, executor, types
from bot.handlers import admin, teacher, committee, parent

import os
API_TOKEN = os.getenv("BOT_TOKEN", "YOUR_TOKEN_HERE")

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Команди старт
@dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message):
    user_role = "admin"  # Тут логіка визначення ролі користувача
    if user_role == "admin":
        await admin.admin_menu(message)
    elif user_role == "teacher":
        await teacher.teacher_menu(message)
    elif user_role == "committee":
        await committee.committee_menu(message)
    elif user_role == "parent":
        await parent.parent_menu(message)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
