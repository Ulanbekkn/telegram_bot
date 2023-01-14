from config import bot, ADMINS
from aiogram import types, Dispatcher
from random import choice

async def echo(message: types.Message):
    bad_words = ["дурак", "fuck", "еблан", "эшек"]
    username = f"@{message.from_user.username}" \
        if message.from_user.username is not None else message.from_user.first_name
    for word in bad_words:
        if word in message.text.lower().replace(" ", ""):
            if message.from_user.id not in ADMINS:
                await message.answer(f"Не матерись {username}")
                await bot.send_message(message.from_user.id, f"Сам {message.text}\n"
                                                             f"Не пиши такое в группу!")
            else:
                await message.answer("Вам можно, мой хозяин")

    # if message.text.startswith("."):
    #     await bot.pin_chat_message(message.chat.id, message.message_id)

    if message.text == "dice":
        await bot.send_dice(message.chat.id, emoji="⚽️")

    if message.text.startswith("game"):
        if message.from_user.id in ADMINS:
            animation = choice(["⚽️", "🏀", "🎯", "🎳", "🎰", "🎲"])
            await bot.send_dice(message.chat.id, emoji=animation)
        else:
            await message.answer(f"У вас нет прав администатора!")

def register_handlers_extra(dp: Dispatcher):
    dp.register_message_handler(echo)
