from aiogram.types.inline_keyboard_button import InlineKeyboardButton

button = InlineKeyboardButton

def init_buttons():
    kb = [
        [button(text="Reset", callback_data="reset")],
        [button(text="Shutdown", callback_data="shutdown")]
    ]
    return kb
