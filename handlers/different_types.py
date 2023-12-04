from aiogram import Router, F
from aiogram.types import Message

router = Router()


@router.message(F.text)
async def message_with_text(message: Message):
    await message.answer("Вы некорректно ввели команду !")


@router.message(F.sticker)
async def message_with_sticker(message: Message):
    await message.answer("Вы отправили красивый смайлик! Но к сожалению это не одна из команд.")


@router.message(F.animation)
async def message_with_gif(message: Message):
    await message.answer("Крутая гифка! Но к сожалению это не одна из команд.")
