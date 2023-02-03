"""
This is a echo bot.
It echoes any incoming text messages.
"""

import logging

import aiogram.utils
import aiogram.utils.markdown as md
import os

from aiogram import Bot, Dispatcher, executor, types
from pytube import YouTube

API_TOKEN = '5915305402:AAEepx05lktT-dotxZ1Rx1V5jB9XAlJCCxg'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")



@dp.message_handler()
async def echo(message: types.Message):
    link = message.text.strip()
    yt = YouTube(link)
    video = yt.streams.filter(file_extension='mp4').first()
    video.download()
    output = video.get_file_path()
    print(output)

    await bot.send_message(chat_id=message.chat.id, text=f"Video  is downloading...")
    await bot.send_video(chat_id=message.chat.id, video=open(f"{output}", 'rb'))


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)