
from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from config import PHOTO_BUILD_READY, MODERATOR_ID

builds_router = Router()
waiting_for_title = {}
waiting_for_photo = {}

@builds_router.callback_query(F.data.startswith("build_"))
async def build_start(cb: CallbackQuery):
    build_type = cb.data.replace("build_", "")
    waiting_for_title[cb.from_user.id] = build_type
    await cb.message.edit_caption(
        f"🦠 *{build_type.title()}*

Введите название билда ⬇️"
    )

@builds_router.message(F.text & F.from_user.id.in_(waiting_for_title.keys()))
async def get_title(msg: Message):
    waiting_for_photo[msg.from_user.id] = {
        "type": waiting_for_title[msg.from_user.id],
        "title": msg.text
    }
    del waiting_for_title[msg.from_user.id]
    await msg.answer("Отправьте фото для билда 📷")

@builds_router.message(F.photo & F.from_user.id.in_(waiting_for_photo.keys()))
async def get_build_photo(msg: Message):
    data = waiting_for_photo[msg.from_user.id]
    del waiting_for_photo[msg.from_user.id]

    caption = (
        f"🧾 *Новая заявка*
"
        f"От @{msg.from_user.username}
"
        f"Тип: {data['type']}
"
        f"Название: {data['title']}"
    )
    await msg.bot.send_photo(MODERATOR_ID, msg.photo[-1].file_id, caption=caption)

    await msg.answer("Ваша заявка отправлена модерации!")

@builds_router.message(F.from_user.id.in_(waiting_for_photo.keys()))
async def wrong_file(msg: Message):
    await msg.answer("Ошибка 🚫 Отправьте фото!")
