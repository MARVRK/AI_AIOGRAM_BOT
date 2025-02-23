import asyncio
import sys

from aiogram.filters import Command
from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, User



from app.db.db_logic import create_user, fetch_all, delete
from app.keyboard.admin_keyboard import init_buttons
from app.services.generate_ai import gpt_4o
from app.data.loader import bot

router = Router()


class LoopState(StatesGroup):
    reply = State()


@router.message(Command("init"))
async def init(message: Message):
    init_data = fetch_all(message.from_user.username)
    await gpt_4o(init_data.data_conversation)


@router.message(Command("start"))
async def start(message: Message, state: FSMContext):
    keyboard = InlineKeyboardMarkup(inline_keyboard=init_buttons())
    await message.answer(f"Hello {message.from_user.username} in {message.date}", reply_markup=keyboard)
    await state.set_state(LoopState.reply)


@router.message(LoopState.reply)
async def reply_loop(message: Message):
    user_text = str(message.text)
    init_data = fetch_all(message.from_user.username)
    if init_data is None:
        last_conversation = []
        await message.answer("This is conversation is empty")
    else:
        last_conversation = init_data.data_conversation[-1:]

    last_conversation.append({"role": "user", "content": user_text})
    message_for_ia = await gpt_4o(last_conversation)
    answer = await message.answer(text=f"{message_for_ia.choices[0].message.content}")
    last_conversation.append({"role": "assistant", "content": answer.text})
    create_user(user_id=message.from_user.username, data_conversation=last_conversation, role="ADMIN")

@router.callback_query()
async def check_button(call: CallbackQuery):
    if call.data == "reset":
        delete(user_id=call.from_user.username)
        await call.message.answer(text=f"Db for user {call.from_user.username} has been cleared")

    if call.data == "shutdown":
        await call.message.answer(text="Goodbye!")
        await bot.session.close()
        await asyncio.sleep(1)
        sys.exit(0)