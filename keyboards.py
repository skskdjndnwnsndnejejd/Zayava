
from aiogram.utils.keyboard import InlineKeyboardBuilder

def one_btn(text, data):
    kb = InlineKeyboardBuilder()
    kb.button(text=text, callback_data=data)
    return kb.as_markup()

def multi_btn(btns):
    kb = InlineKeyboardBuilder()
    for text, data in btns:
        kb.button(text=text, callback_data=data)
    kb.adjust(1)
    return kb.as_markup()
