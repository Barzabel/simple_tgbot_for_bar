from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.types import FSInputFile
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

button_hi = KeyboardButton('menu')

greet_kb = ReplyKeyboardMarkup()
greet_kb.add(button_hi)


start_router = Router()

@start_router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer('hi', reply_markup=greet_kb)

@start_router.message(Command('menu'))
async def send_menu(message: Message):
    menu = FSInputFile('data/menu.pdf')
    await message.reply_document(menu, reply_markup=greet_kb)
    

