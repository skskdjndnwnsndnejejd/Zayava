
from aiogram import Router, F
from aiogram.types import Message
from keyboards import multi_btn
from config import PHOTO_MENU

menu_router = Router()

@menu_router.message(F.text == "/menu")
async def menu_cmd(msg: Message):
    await msg.answer_photo(
        PHOTO_MENU,
        caption="📂 *Главное меню*
Выберите билд:",
        reply_markup=multi_btn([
            ("Chimera", "build_chimera"),
            ("Lazarus", "build_lazarus")
        ])
    )
