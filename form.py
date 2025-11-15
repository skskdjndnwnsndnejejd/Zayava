
from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from keyboards import multi_btn
from config import PHOTO_FORM, MODERATOR_ID

form_router = Router()
user_data = {}

@form_router.callback_query(F.data == "form_start")
async def form_step1(cb: CallbackQuery):
    user_data[cb.from_user.id] = {}
    await cb.message.edit_caption(
        "📝 *Анкета*

_Сколько времени вы находитесь в команде?_",
        reply_markup=multi_btn([
            ("Сегодня", "form_t1"),
            ("5-15 дней", "form_t2"),
            ("15-30 дней", "form_t3"),
            ("30+ дней", "form_t4")
        ])
    )

@form_router.callback_query(F.data.startswith("form_t"))
async def form_step2(cb: CallbackQuery):
    times = {
        "form_t1": "Сегодня",
        "form_t2": "5-15 дней",
        "form_t3": "15-30 дней",
        "form_t4": "30+ дней"
    }
    user_data[cb.from_user.id]["team_time"] = times[cb.data]

    await cb.message.edit_caption(
        "📝 *Анкета*

_Сколько времени готовы уделять работе?_",
        reply_markup=multi_btn([
            ("1-2 часа", "form_w1"),
            ("2-4 часа", "form_w2"),
            ("4-6 часов", "form_w3"),
            ("6+ часов", "form_w4")
        ])
    )

@form_router.callback_query(F.data.startswith("form_w"))
async def form_step3(cb: CallbackQuery):
    w = {
        "form_w1": "1-2 часа",
        "form_w2": "2-4 часа",
        "form_w3": "4-6 часов",
        "form_w4": "6+ часов"
    }
    user_data[cb.from_user.id]["work_time"] = w[cb.data]

    await cb.message.edit_caption(
        "📝 *Анкета*

_На какой профит рассчитываете?_",
        reply_markup=multi_btn([
            ("0-15$", "form_p1"),
            ("15-50$", "form_p2"),
            ("50-500$", "form_p3"),
            ("500$+", "form_p4")
        ])
    )

@form_router.callback_query(F.data.startswith("form_p"))
async def form_finish(cb: CallbackQuery):
    p = {
        "form_p1": "0-15$",
        "form_p2": "15-50$",
        "form_p3": "50-500$",
        "form_p4": "500$+"
    }
    uid = cb.from_user.id
    user_data[uid]["profit"] = p[cb.data]

    await cb.message.edit_caption(
        "📝 *Анкета*

Ваша анкета отправлена модерации!",
    )

    text = (
        f"📨 *Анкета №{uid}*

"
        f"1. Юзернейм: @{cb.from_user.username}
"
        f"2. В команде: {user_data[uid]['team_time']}
"
        f"3. Время работы: {user_data[uid]['work_time']}
"
        f"4. Профит: {user_data[uid]['profit']}
"
    )

    await cb.bot.send_message(MODERATOR_ID, text)
