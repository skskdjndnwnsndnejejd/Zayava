
from aiogram import Router, F
from aiogram.types import Message
from keyboards import one_btn
from config import PHOTO_START

start_router = Router()

@start_router.message(F.text == "/start")
async def start_cmd(msg: Message):
    await msg.answer_photo(
        PHOTO_START,
        caption="✨ *Подача анкеты*

_Для использования бота прочитайте правила..._",
        reply_markup=one_btn("Продолжить ▶", "start_next")
    )
