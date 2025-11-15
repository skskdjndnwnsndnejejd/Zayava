
from aiogram import Router, F
from aiogram.types import CallbackQuery
from keyboards import one_btn
from config import PHOTO_RULES
import asyncio

rules_router = Router()

@rules_router.callback_query(F.data == "start_next")
async def rules_step1(cb: CallbackQuery):
    await cb.message.edit_media(
        media={"type": "photo", "media": PHOTO_RULES},
        reply_markup=None
    )
    await cb.message.edit_caption(
        "📘 *Правила*

_Пожалуйста ознакомьтесь..._",
        reply_markup=one_btn("Продолжить ▶", "rules_next_1")
    )

@rules_router.callback_query(F.data == "rules_next_1")
async def rules_step2(cb: CallbackQuery):
    await asyncio.sleep(0.2)
    await cb.message.edit_caption(
        "📘 *Правила*

*Глава 1: Бот и Модерация*
"
        "1.1 ...
1.2 ...
1.3 ...
1.4 ...
1.5 ...
",
        reply_markup=one_btn("Далее 1/2 ▶", "rules_next_2")
    )

@rules_router.callback_query(F.data == "rules_next_2")
async def rules_step3(cb: CallbackQuery):
    await cb.message.edit_caption(
        "📘 *Правила*

*Глава 2: Чат и Общение*
"
        "2.1 ...
2.2 ...
2.3 ...
2.4 ...
"
        "2.5 ...
2.6 ...
2.7 ...
2.8 ...
2.9 ...
",
        reply_markup=one_btn("Далее 2/2 ▶", "form_start")
    )
