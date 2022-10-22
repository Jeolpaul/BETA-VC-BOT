import asyncio
import platform
from sys import version as pyver

from pyrogram import filters
from pyrogram.errors import MessageIdInvalid
from pyrogram.types import CallbackQuery, InputMediaPhoto, Message
from YukkiMusic import app
from .http import get, SOURCE


@app.on_callback_query()
async def callback(bot, msg):
   data = msg.data
   if data == "dev":
         users = await get("https://api.github.com/repos/Jeolpaul/MUSICBYPASS/contributors")
         list_of_users = ""
         count = 1
         for user in users:
             list_of_users += (f"**{count}.** [{user['login']}]({user['html_url']})\n")       
             count += 1 
         await msg.message.edit(
             text=SOURCE.format(dev=list_of_users),
             reply_markup=InlineKeyboardMarkup( [[
                  InlineKeyboardButton("👨‍💻 Developer", user_id=5558249587),
                  ]]
                  )
             )
