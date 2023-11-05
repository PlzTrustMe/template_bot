from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from infrastructure.database.models.user import User

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext, user: User):
    await state.clear()

    await message.answer(f'Hello, {user.full_name}')
