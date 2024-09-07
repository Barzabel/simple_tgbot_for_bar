from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.types import FSInputFile
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton



greet_kb = ReplyKeyboardMarkup(keyboard=[
[KeyboardButton(text='Меню', callback_data="menu")]])

start_router = Router()

@start_router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer('hi', reply_markup=greet_kb)


@start_router.message()
async def buttoms(message: Message):
    word_fork = {"Меню":button_menu,}
    function = word_fork.get(message.text, button_menu)
    await function(message)


async def button_menu(message):
        menu = FSInputFile('data/menu.pdf')
        await message.reply_document(menu, reply_markup=greet_kb)